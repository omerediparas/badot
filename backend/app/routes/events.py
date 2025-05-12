from flask import Blueprint, jsonify
from app.models import Event
from app import db

bp = Blueprint('events', __name__, url_prefix='/api/events')

@bp.route('/', methods=['GET'])
def get_events():
    events = Event.query.all()
    result = []
    for event in events:
        result.append({
            "id": event.id,
            "name": event.name,  
            "category": event.category,
            "date": event.date.strftime('%Y-%m-%d'),
            "venue": event.venue, 
            "price": event.price,
            "image_url": event.image_url
        })
    return jsonify(result)
