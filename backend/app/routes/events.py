from flask import Blueprint, jsonify
from app.models import Event

bp = Blueprint('events', __name__, url_prefix='/api/events')

@bp.route('/', methods=['GET'])
def get_events():
    events = Event.query.all()
    return jsonify([
        {
            "id": e.id,
            "name": e.name,
            "category": e.category,
            "date": e.date.strftime('%Y-%m-%d'),
            "venue": e.venue,
            "price": e.price,
            "image_url": e.image_url
        } for e in events
    ])
