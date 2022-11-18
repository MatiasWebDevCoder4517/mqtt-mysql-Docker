from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.user import UserCreate
from api.dependencies import get_admin_user
from db.session import get_db
from schemas.broker import ListBroker, BrokerBase, BrokerDisplay
from .service import broker_service

router = APIRouter()

# ***** auth: current_user: UserCreate = Depends(get_admin_user) ; IN EVERY ENDPOINT *****


@router.get('/broker/{id}', response_model=BrokerDisplay)
def get_broker(
    id: int,
    db: Session = Depends(get_db),
    current_user: UserCreate = Depends(get_admin_user)

):
    return broker_service.get(db, id)


@router.post('/broker', response_model=BrokerDisplay, status_code=201)
def create_broker(
    broker: BrokerBase,
    db: Session = Depends(get_db),
    current_user: UserCreate = Depends(get_admin_user)

):
    try:
        return broker_service.create(db, obj_in=broker)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f'{e}')


@router.put('/broker', response_model=BrokerDisplay)
def update_broker(
    broker: BrokerDisplay,
    db: Session = Depends(get_db),
    current_user: UserCreate = Depends(get_admin_user)

):
    try:
        return broker_service.update(db, obj_in=broker)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f'{e}')


@router.delete('/broker/{id}')
def delete_broker(
    id: int,
    db: Session = Depends(get_db),
    current_user: UserCreate = Depends(get_admin_user)

):
    try:
        return broker_service.remove(db, id=id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f'{e}')

@router.get('/brokers', response_model=ListBroker)
def get_all_brokers(
    page: int,
    db: Session = Depends(get_db),
    current_user: UserCreate = Depends(get_admin_user)

):
    return broker_service.get_paginate(db, page=page)
