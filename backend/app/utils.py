from jose import jwt
from passlib.context import CryptContext
import psycopg2
from psycopg2 import OperationalError
import os
from dotenv import load_dotenv


load_dotenv()
SECRET_KEY = os.getenv("SECRET")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
REFRESH_TOKEN_EXPIRE_DAYS = 7



def check_postgres_connection():
    try:
        connection = psycopg2.connect(
            dbname=os.getenv('POSTGRES_DATABASE'),
            user=os.getenv('POSTGRES_USER'),
            password=os.getenv('POSTGRES_PASSWORD'),
            host=os.getenv('POSTGRES_HOST'),
            port=os.getenv('DOCKER_POSTGRES_PORT'),
        )
        connection.close()
        return True
    except OperationalError as e:
        return str(e)