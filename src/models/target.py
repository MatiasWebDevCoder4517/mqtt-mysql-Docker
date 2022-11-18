from models import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, ForeignKey, Integer, String


class Target(Base):
    __tablename__ = 'targets'
    id = Column(Integer, primary_key=True)
    url = Column(String, default="localhost:5000/test")
    
    id_broker_target = Column(Integer, ForeignKey('brokers.id', onupdate='CASCADE', ondelete='CASCADE'), nullable=True)
    broker = relationship('Broker', foreign_keys=[id_broker_target])