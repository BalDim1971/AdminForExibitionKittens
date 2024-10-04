"""
CRUD операции для работы с моделью "Котенок"
"""

from sqlalchemy.orm import Session

from kittens.models import Kitten
from kittens.schemas import KittenCreate, KittenUpdate


def get_kitten_by_id(db: Session, id: int) -> Kitten:
    """
    Получить котенка по id. Если такой котенок не найден, вернуть None
    :param db: Ссылка на сессию БД.
    :param id: ID котенка.
    :return: Данные котенка.
    """
    return db.query(Kitten).filter(Kitten.id == id).first()


def create_kitten(db: Session, kitten: KittenCreate) -> Kitten:
    """
    Создать котенка.
    :param db: Ссылка на сессию БД.
    kitten: Данные котенка.
    
    """
    db_kitten = Kitten(**kitten.model_dump())
    db.add(db_kitten)
    db.commit()
    db.refresh(db_kitten)
    return db_kitten


def update_kitten(db: Session, id: int, kitten: KittenUpdate)-> Kitten:
    db_kitten = get_kitten_by_id(db, id)
    if db_kitten:
        for field, value in kitten.dict().items():
            setattr(db_kitten, field, value)
        db.commit()
        db.refresh(db_kitten)
    return db_kitten


def delete_kitten(db: Session, id: int) -> Kitten:
    db_kitten = get_kitten_by_id(db, id)
    if db_kitten:
        db.delete(db_kitten)
        db.commit()
    return db_kitten
