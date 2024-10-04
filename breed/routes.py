from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from breed.models import Breed
from breed.schemas import BreedSchema, BreedCreate
from src.database import get_db
from breed.crud import create_breed, get_breed_by_name

app_breed = APIRouter(tags=['breeds'], prefix='/breeds')


@app_breed.get("/breed")
def get_breeds(db: Session = Depends(get_db)):
    return db.query(Breed).all()


@app_breed.get("/breed/{breed_id}")
def get_breed(breed_id: int, db: Session = Depends(get_db)):
    return db.query(Breed).filter(Breed.id == breed_id).first()


@app_breed.post("/breed", response_model=BreedSchema)
def create_breed(breed: BreedCreate = Depends(), db: Session = Depends(get_db)):
    db_breed = get_breed_by_name(db, name=breed.name)
    if db_breed:
        raise HTTPException(status_code=400, detail="Breed already exists")
    return create_breed(db=db, breed=breed)
