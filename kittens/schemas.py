from pydantic import BaseModel


class KittenCreate(BaseModel):
    color: str
    age: int
    description: str
    breed_id: int


class KittenUpdate(BaseModel):
    color: str
    age: int
    description: str
    breed_id: int


class KittenSchema(KittenCreate):
    id: int
    
    class Config:
        from_attributes: bool = True
