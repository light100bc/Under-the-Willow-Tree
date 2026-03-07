from fastapi import APIRouter, Request

from app.api.schemas.schemas import CreateNpcRequest

router = APIRouter(prefix="/entity")


@router.post("/create_npc")
def create_npc(req: CreateNpcRequest, request: Request):
    request.app.state.container.entity_service.create_npc(req.name, req.x, req.y)
    return {"status": "ok"}
