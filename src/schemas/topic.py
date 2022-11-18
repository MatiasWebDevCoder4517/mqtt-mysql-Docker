from typing import Optional, List
from pydantic import BaseModel
from .response import Pagination
from models import Broker

class TopicInDBBase(BaseModel):
    topic: str
    qos: int
    id_broker_topic: int

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True

class TopicCreate(TopicInDBBase):
    topic: str
    qos: int

class TopicUpdate(TopicCreate):
    id: int
    topic: Optional[str]
    qos: Optional[int]

class Topic(TopicInDBBase):
    id: int

class TopicListPag(Pagination):
    data: List[Topic]

    class Config:
        orm_mode = True
        