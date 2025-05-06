from sqlalchemy import ( Column, String, Text, Integer, ForeignKey, Date, Float, Boolean, Table, ARRAY )
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from typing import Dict
import uuid

Base = declarative_base()

# TO BE WRITTEN....

# EXAMPLE
class User(Base):
    __tablename__ = 'users'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = Column(String(50), unique=True, nullable=False)
    password = Column(String(50), nullable=False)
