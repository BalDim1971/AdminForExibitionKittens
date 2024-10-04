from pydantic import BaseModel


class BreedBase(BaseModel):
    name: str


class BreedCreate(BaseModel):
    name: str


class BreedSchema(BreedBase):
    id: int
    
    class Config:
        from_attributes: bool = True
