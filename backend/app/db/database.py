from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from .base import Base
import os
from dotenv import load_dotenv


load_dotenv()
DATABASE_URL = f"postgresql://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}@{os.getenv('POSTGRES_HOST')}:{os.getenv('DOCKER_POSTGRES_PORT')}/{os.getenv('POSTGRES_DATABASE')}"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def init_db():
    Base.metadata.create_all(bind=engine)

    db: Session = SessionLocal()

    db.close()