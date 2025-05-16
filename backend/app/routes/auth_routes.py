from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from app.utils.jwt_utils import generate_token
from app.utils.response_utils import error_response
from app.database.user_operations import find_user_by_email, create_user, insert_role_specific
from app.roles import ALL_ROLES
from app.database.db_utils import get_connection

auth_bp = Blueprint("auth", __name__, url_prefix="/api/auth")

@auth_bp.route('/signup', methods=['POST','OPTIONS'])
def register_user():

    if request.method == 'OPTIONS':
        return '', 200 
    
    data = request.get_json()
    required = ['role', 'first_name', 'last_name', 'email', 'password', 'confirmPassword']

    if not all(data.get(f) for f in required):
        return error_response('All fields except Middle Name are required')

    if data['password'] != data['confirmPassword']:
        return error_response('Passwords do not match')

    if data['role'] not in ALL_ROLES:
        return error_response('Invalid role')

    if find_user_by_email(data['email']):
        return error_response('Email already in use', 409)

    hashed_password = generate_password_hash(data['password'])

    user_data = {
        **data,
        'password': hashed_password,
        'login_date': datetime.utcnow()
    }

    user_id = create_user(user_data)
    insert_role_specific(user_id, data['role'])

    return jsonify({
        'message': 'Registration successful',
        'user': {
            'user_id': user_id,
            'role': data['role'],
            'email': data['email'],
            'first_name': data['first_name'],
            'last_name': data['last_name']
        }
    }), 201

@auth_bp.route('/signin', methods=['POST','OPTIONS'])
def login_user():

    if request.method == 'OPTIONS':
        return '', 200 
    
    data = request.get_json()
    email, password, role = data.get('email'), data.get('password'), data.get('role')

    if not email or not password or not role:
        return error_response('Email, password, and role are required')

    user = find_user_by_email(email)
    if not user or not check_password_hash(user['password'], password):
        return error_response('Invalid email or password', 401)

    user_id = user['user_id']

    # Role validation
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            if role == "Admin":
                cursor.execute("SELECT * FROM Panel_Admin WHERE user_id = %s", (user_id,))
            elif role == "Organizer":
                cursor.execute("SELECT * FROM Event_Organiser WHERE user_id = %s", (user_id,))
            elif role == "Attendee":
                cursor.execute("SELECT * FROM Event_Attendee WHERE user_id = %s", (user_id,))
            if not cursor.fetchone():
                return error_response(f'User is not registered as {role}', 403)

            # Update login_date
            cursor.execute("UPDATE User SET login_date = %s WHERE user_id = %s", (datetime.utcnow(), user_id))
            connection.commit()
    finally:
        connection.close()

    token = generate_token(user_id, role)
    return jsonify({
        'token': token,
        'user': {
            'user_id': user_id,
            'role': role,
            'first_name': user['first_name'],
            'middle_name': user.get('middle_name'),
            'last_name': user['last_name'],
            'email': user['email'],
        }
    }), 200
