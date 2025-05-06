from typing import Generator
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from .db import session

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="home")

def get_db() -> Generator:
    try:
        db = session.SessionLocal()
        yield db
    finally:
        db.close()

