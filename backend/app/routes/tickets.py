from flask import Blueprint, jsonify
from app.models import Ticket
from app.database.db_utils import get_connection

bp = Blueprint('tickets', __name__, url_prefix='/api/tickets')

@bp.route('/all', methods=['GET'])
def get_tickets():
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM tickets")
            tickets = cursor.fetchall()
        return jsonify(tickets)
    finally:
        connection.close()

    
