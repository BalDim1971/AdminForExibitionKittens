from sqlalchemy.orm import Session

from breed.models import Breed
from breed import schemas


def get_breed_by_name(db: Session, name: str):
    return db.query(Breed).filter(Breed.name == name).first()


def get_breed_by_id(db: Session, id: int):
    return db.query(Breed).filter(Breed.id == id).first()


def create_breed(db: Session, breed: schemas.BreedCreate):
    db_breed = Breed(name=breed.name)
    db.add(db_breed)
    db.commit()
    db.refresh(db_breed)
    return db_breed


def delete_breed(db: Session, breed_id: int):
    """
    Удалить породу по id. Надо ли удалять котят?
    :param db: Ссылка на сессию БД.
    :param breed_id: Id породы.
    :return:
    """
    db_breed = get_breed_by_id(db, breed_id)
    if db_breed:
        db.delete(db_breed)
        db.commit()
    return db_breed
