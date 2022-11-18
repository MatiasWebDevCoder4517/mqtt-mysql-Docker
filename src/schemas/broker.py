from typing import List, Optional
from pydantic import BaseModel
from .response import Pagination
from models import Target, Topic


class BrokerBase(BaseModel):
    hostname: str
    port: int
    username: str
    password: str
    transport: str
    
   
class BrokerCreate(BrokerBase):
    password: str
    
class BrokerUpdate(BrokerCreate):
    id: int
    password: Optional[str]

class BrokerDisplay(BrokerBase):
    id: int
    
    ##targets: List[Target] = []
    ##topics: List[Topic] = []

    class Config:
        orm_mode = True
        

class ListBroker(Pagination):
    data: List[BrokerDisplay]

    class Config:
        orm_mode = True
        
        
#############       
        








