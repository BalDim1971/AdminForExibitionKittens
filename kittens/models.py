from sqlalchemy import Column, Integer, String

from breed.models import Base


class Kitten(Base):
    """
    Модель котенка.
    Атрибуты:
    id - идентификатор котенка;
    color - цвет котенка;
    age - возраст котенка, полные месяца;
    description - описание котенка;
    breed_id - идентификатор породы.
    """
    __tablename__: str = 'kittens'
    
    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    color = Column(String)
    age = Column(Integer)
    description = Column(String)
    breed_id = Column(Integer)
