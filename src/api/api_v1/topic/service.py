from sqlalchemy.orm import Session
from typing import Union, Dict, Any
from fastapi.encoders import jsonable_encoder
from models import Topic
from db.crud import CRUDBase
from schemas.topic import TopicUpdate, TopicCreate


class CRUDTopic(CRUDBase[Topic, TopicCreate, TopicUpdate]):
    def create(self, db: Session, *, obj_in: TopicCreate) -> Topic:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self, db: Session,
        *, obj_in: Union[TopicUpdate, Dict[str, Any]]
    ) -> Topic:
        db_obj = db.query(self.model).get(obj_in.id)
        obj_data = jsonable_encoder(db_obj)
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        for field in obj_data:
            if field in update_data:
                setattr(db_obj, field, update_data[field])
            
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

topic_service = CRUDTopic(model=Topic)