from flask import Blueprint, jsonify
from app.models import Event
from app.db_utils import get_connection

bp = Blueprint('events', __name__, url_prefix='/api/events')

@bp.route('/all', methods=['GET'])
def get_events():
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM events")
            events = cursor.fetchall()
            for event in events:
                event['date'] = event['date'].strftime('%Y-%m-%d')
        return jsonify(events)
    finally:
        connection.close()

@bp.route("/create", methods=['POST'])
def create_event():
    #TODO
    pass

