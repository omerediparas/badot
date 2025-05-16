from flask import Blueprint, jsonify, request
from app.database.db_utils import get_connection

bp = Blueprint('event', __name__, url_prefix='/api/event')

@bp.route('/all', methods=['GET'])
def get_events():
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            query = """
                SELECT 
                    e.event_id,
                    e.name,
                    e.type,
                    e.date,
                    e.description,
                    e.active_status,
                    e.rating,
                    e.user_id,
                    e.venue_id,
                    e.rules,
                    e.image_url,
                    v.name AS venue_name,
                    v.city AS venue_city,
                    v.state AS venue_state
                FROM Event e
                JOIN Venue v ON e.venue_id = v.venue_id
            """
            cursor.execute(query)
            events = cursor.fetchall()
            for event in events:
                if isinstance(event['date'], (str, bytes)):
                    continue
                event['date'] = event['date'].strftime('%Y-%m-%d %H:%M:%S')
        return jsonify(events)
    finally:
        connection.close()


@bp.route('/create', methods=['POST'])
def create_event():
    data = request.get_json()

    required_fields = [
        'name', 'type', 'date', 'description', 'active_status',
        'rating', 'user_id', 'venue_id', 'rules', 'image_url'
    ]
    if not all(field in data for field in required_fields):
        return jsonify({'error': 'Missing required fields'}), 400

    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            query = """
                INSERT INTO Event (
                    name, type, date, description, active_status, rating,
                    user_id, venue_id, rules, image_url
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(query, (
                data['name'],
                data['type'],
                data['date'],
                data['description'],
                data['active_status'],
                data['rating'],
                data['user_id'],
                data['venue_id'],
                data['rules'],
                data['image_url']
            ))
            connection.commit()
            return jsonify({'message': 'Event created successfully'}), 201
    finally:
        connection.close()
