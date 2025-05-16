import jwt, os
from datetime import datetime, timedelta

SECRET_KEY = os.getenv("SECRET_KEY")

def generate_token(user_id, role):
    payload = {
        'user_id': user_id,
        'role': role,
        'exp': datetime.utcnow() + timedelta(hours=2)
    }
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")
