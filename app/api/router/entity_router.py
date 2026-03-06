from fastapi import APIRouter

from app.api.schemas.schemas import CreateNpcRequest
from app.container import entity_service

router = APIRouter(prefix="/entity")
@router.post("/create_npc")
def create_npc(req: CreateNpcRequest):
    entity_service.create_npc(req.name,req.x,req.y)
    return {"status": "ok"}