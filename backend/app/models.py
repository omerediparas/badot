from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Room(db.Model):
    __tablename__ = 'rooms'
    
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer, unique=True)
    type = db.Column(db.String(50))
    price = db.Column(db.Integer)
    is_booked = db.Column(db.Boolean, default=False)

class Booking(db.Model):
    __tablename__ = 'bookings'
    
    id = db.Column(db.Integer, primary_key=True)
    guest_name = db.Column(db.String(100))
    room_id = db.Column(db.Integer, db.ForeignKey('rooms.id'))
    check_in = db.Column(db.String(50))
    check_out = db.Column(db.String(50))

    room = db.relationship("Room", backref="bookings")
