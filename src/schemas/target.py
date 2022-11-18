from typing import Optional, List
from pydantic import BaseModel
from .response import Pagination
from models import Broker

class TargetInDBBase(BaseModel):
    url: str
    id_broker_target: int

    class Config:
        orm_mode = True
        

class TargetCreate(TargetInDBBase):
    url: str

class TargetUpdate(TargetCreate):
    id: int
    url: Optional[str]

class Target(TargetInDBBase):
    id: int

class TargetListPag(Pagination):
    data: List[Target]

    class Config:
        orm_mode = True