
from datetime import datetime
from app import db


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(120), unique=True)
    wallet_balance = db.Column(db.Float, default=0.0)
    #followed = db.relationship('OrganizerFollow', back_populates='user')

class Event(db.Model):
    __tablename__ = 'events'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    category = db.Column(db.String(50))
    date = db.Column(db.DateTime)
    venue = db.Column(db.String(128))
    price = db.Column(db.Float)
    image_url = db.Column(db.String(255))

class Ticket(db.Model):
    __tablename__ = "tickets"
    id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer, db.ForeignKey('events.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    seat_number = db.Column(db.String(10))
    guest_name = db.Column(db.String(128))
