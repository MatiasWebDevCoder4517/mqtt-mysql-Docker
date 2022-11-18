from fastapi import APIRouter
from .api_v1.user import user
from .api_v1.role import role
from .api_v1.auth import auth
from .api_v1.broker import broker
from .api_v1.target import target
from .api_v1.topic import topic

router = APIRouter()

router.include_router(auth.router)
router.include_router(role.router, tags=['role']) 
router.include_router(user.router)
router.include_router(broker.router, tags=["broker"])
router.include_router(target.router, tags=["target"])
router.include_router(topic.router, tags=['topic'])

