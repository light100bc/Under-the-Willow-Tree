from fastapi import APIRouter, Request

from app.api.schemas.schemas import EatRequest

router = APIRouter(prefix="/action")


@router.post("/eat")
def eat(req: EatRequest, request: Request):
    request.app.state.container.action_service.eat(req.entity, req.value)
    return {"status": "ok"}
