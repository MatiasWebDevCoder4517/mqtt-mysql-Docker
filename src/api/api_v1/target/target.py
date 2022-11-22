from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from db.session import get_db
from .service import target_service
from api.dependencies import get_admin_user
from schemas.target import TargetCreate, TargetUpdate, TargetListPag, Target
from schemas.user import UserCreate

router = APIRouter()
# ***** auth: current_user: UserCreate = Depends(get_admin_user) ; IN EVERY ENDPOINT *****

@router.get('/target/{id}', response_model=Target, tags=['target'])
def target_get(
    id: int,
    db: Session = Depends(get_db),
    current_user: UserCreate = Depends(get_admin_user)
):
    return target_service.get(db, id)


@router.post('/target', response_model=Target, status_code=201, tags=['target'])
def target_create(target: TargetCreate, db: Session = Depends(get_db), current_user: UserCreate = Depends(get_admin_user)
                  ):
    return target_service.create(db, obj_in=target)


@router.delete('/target/{id}', response_model=Target, tags=['target'])
def delete_target(
    id: int,
    db: Session = Depends(get_db),
    current_user: UserCreate = Depends(get_admin_user)
    
):
    return target_service.remove(db, id=id)


@router.put('/target', response_model=Target, tags=['target'])
def update_target(
    upd_target: TargetUpdate,
    db: Session = Depends(get_db),
    current_user: UserCreate = Depends(get_admin_user)
    
):
    return target_service.update(db, obj_in=upd_target)

@router.get('/targets', response_model=TargetListPag, tags=['target'])
def get_all_target(
    page: int,
    db: Session = Depends(get_db),
    current_user: UserCreate = Depends(get_admin_user)
    
):
    return target_service.get_paginate(db, page=page)
