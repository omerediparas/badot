from pydantic import BaseModel, UUID4, Field
from typing import List, Optional, Dict

# TO BE WRITTEN....


# # EXAMPLE
class UserBase(BaseModel):
    username: str
    password: str


class UserCreate(UserBase):
    pass

class User(UserBase):
    id: UUID4

    class Config:
        from_attributes = True
