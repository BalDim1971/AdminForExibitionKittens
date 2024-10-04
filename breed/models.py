from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class Breed(Base):
    """
    Порода котят.
    Атрибуты:
    id - идентификатор породы;
    name - название породы.
    """
    __tablename__: str = 'breeds'
    
    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    name = Column(String, unique=True)
