from app.database.db_utils import get_connection

def find_user_by_email(email):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM User WHERE email = %s", (email,))
            return cursor.fetchone()
    finally:
        connection.close()

def create_user(user_data):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("""
                INSERT INTO User (first_name, middle_name, last_name, email, password, login_date, nationality)
                VALUES (%s, %s, %s, %s, %s, %s, NULL)
            """, (
                user_data['first_name'],
                user_data.get('middle_name'),
                user_data['last_name'],
                user_data['email'],
                user_data['password'],
                user_data['login_date']
            ))
            connection.commit()
            user_id = cursor.lastrowid
            return user_id
    finally:
        connection.close()

def insert_role_specific(user_id, role):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            if role == "Organizer":
                cursor.execute("INSERT INTO Event_Organiser (user_id) VALUES (%s)", (user_id,))
            elif role == "Attendee":
                cursor.execute("INSERT INTO Event_Attendee (user_id) VALUES (%s)", (user_id,))
            elif role == "Admin":
                cursor.execute("INSERT INTO Panel_Admin (user_id) VALUES (%s)", (user_id,))
            connection.commit()
    finally:
        connection.close()
