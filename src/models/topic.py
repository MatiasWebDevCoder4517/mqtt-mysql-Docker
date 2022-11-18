from models import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, ForeignKey, Integer, String


class Topic(Base):
    __tablename__ = 'topics'
    id = Column(Integer, primary_key=True)
    topic = Column(String)
    qos = Column(Integer)
    
    id_broker_topic = Column(Integer, ForeignKey('brokers.id', onupdate='CASCADE', ondelete='CASCADE'), nullable=True)
    broker = relationship('Broker', foreign_keys=[id_broker_topic])