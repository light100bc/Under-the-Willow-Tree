from fastapi import APIRouter

from app.api.schemas.schemas import EatRequest
from app.container import action_service

router = APIRouter(prefix="/action")
@router.post("/eat")
def eat(req : EatRequest):
    action_service.create_npc(req.entity,req.value)
    return {"status": "ok"}