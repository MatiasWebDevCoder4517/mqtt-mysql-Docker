from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from db.session import get_db
from .service import topic_service
from api.dependencies import get_admin_user
from schemas.user import UserCreate
from schemas.topic import TopicCreate, TopicUpdate, TopicListPag, Topic

router = APIRouter()
# ***** auth: current_user: UserCreate = Depends(get_admin_user) ; IN EVERY ENDPOINT *****


@router.get('/topics/{id}', response_model=Topic)
def topics_get(
    id: int,
    db: Session = Depends(get_db),
    current_user: UserCreate = Depends(get_admin_user)

):
    return topic_service.get(db, id)


@router.post('/topics', response_model=Topic, status_code=201)
def topics_create(topics: TopicCreate, db: Session = Depends(get_db), current_user: UserCreate = Depends(get_admin_user)
                  ):
    return topic_service.create(db, obj_in=topics)


@router.delete('/topics/{id}', response_model=Topic)
def delete_topics(
    id: int,
    db: Session = Depends(get_db),
    current_user: UserCreate = Depends(get_admin_user)

):
    return topic_service.remove(db, id=id)


@router.put('/topics', response_model=Topic)
def update_topics(
    upd_topics: TopicUpdate,
    db: Session = Depends(get_db),
    current_user: UserCreate = Depends(get_admin_user)

):
    return topic_service.update(db, obj_in=upd_topics)


@router.get('/topicss', response_model=TopicListPag)
def get_all_topics(
    page: int,
    db: Session = Depends(get_db),
    current_user: UserCreate = Depends(get_admin_user)

):
    return topic_service.get_paginate(db, page=page)
