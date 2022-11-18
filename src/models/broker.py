from models import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class Broker(Base):
    __tablename__ = 'brokers'
    id = Column(Integer, primary_key=True)
    hostname = Column(String(30), unique=True)
    port = Column(Integer, default=1883)
    username = Column(String, default='user_test')
    password = Column(String)
    transport = Column(String)
    
    ##targets = relationship("Target")
    ##topics = relationship("Topic")
