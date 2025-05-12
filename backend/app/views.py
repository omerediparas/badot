from flask import Flask, jsonify, request
from .models import db, Room, Booking
from . import init_app

app = init_app()

@app.route('/rooms', methods=['GET'])
def get_rooms():
    rooms = Room.query.all()
    return jsonify([room.as_dict() for room in rooms])

@app.route('/book', methods=['POST'])
def book_room():
    data = request.json
    guest_name = data['guest_name']
    room_id = data['room_id']
    check_in = data['check_in']
    check_out = data['check_out']
    
    room = Room.query.get(room_id)
    if room.is_booked:
        return jsonify({"error": "Room already booked"}), 400
    
    booking = Booking(guest_name=guest_name, room_id=room_id, check_in=check_in, check_out=check_out)
    db.session.add(booking)
    room.is_booked = True
    db.session.commit()

    return jsonify({"message": "Room booked successfully"})

if __name__ == '__main__':
    app.run(debug=True)
