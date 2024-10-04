from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from kittens.models import Kitten
from kittens.schemas import KittenSchema, KittenCreate
from src.database import get_db

app_kitten = APIRouter(tags=['kittens'], prefix='/kittens')


@app_kitten.get("/kitten")
def get_breeds(db: Session = Depends(get_db)):
    return db.query(Kitten).all()


@app_kitten.get("/breed/{breed_id}")
def get_breed(breed_id: int, db: Session = Depends(get_db)):
    return db.query(Kitten).filter(Kitten.id == breed_id).first()


@app_kitten.post("/breed", response_model=KittenSchema)
def create_breed(breed: KittenCreate = Depends(), db: Session = Depends(get_db)):
    db_breed = get_breed_by_name(db, name=breed.name)
    if db_breed:
        raise HTTPException(status_code=400, detail="Breed already exists")
    return create_breed(db=db, breed=breed)
