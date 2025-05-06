from fastapi import FastAPI, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
import app.db.models as models
from app.deps import get_db
import app.schemas as schemas
from pydantic import UUID4
from typing import List


router = APIRouter()

# from the frontend the methods will be reached like: /api/{tableName}/{method}
# for example: /api/users/add, /api/users/delete/{user_id}, /api/users/all

@router.post("/add/", response_model=schemas.User)
def create_sistem(user: schemas.UserCreate, db: Session = Depends(get_db)):
    # check if the name is unique
    db_user = (
        db.query(models.User).filter(models.User.username == user.username).first()
    )
    if db_user:
        raise HTTPException(status_code=400, detail="Bu isimde bir kullanıcı zaten var")
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@router.delete("/delete/{user_id}", response_model=schemas.User)
def delete_sistem(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="Kullanıcı bulunamadı")
    db.delete(db_user)
    db.commit()
    return db_user


# from the frontend the get methods will be reached like: localhost:8000/api/{tableName}/{method}
# for example: localhost:8000/api/users/all
@router.get("/all/", response_model=List[schemas.User])
def get_all_sistems(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    return users
