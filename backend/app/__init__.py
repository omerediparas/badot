from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')
    print("App created") 
    CORS(app)
    db.init_app(app)

    from app.routes import events
    app.register_blueprint(events.bp) 

    with app.app_context():
        db.create_all()

    return app
