#fetch("/player/move", {
#   method: "POST",
#   body: JSON.stringify({
#     entity_id: 1,
#     target_x: 10,
#     target_y: 5
#   })
# })
import asyncio

from fastapi import APIRouter
from app.container import game_engine,query_service

router = APIRouter(prefix="/world")

@router.post("/tick")
def tick():
    game_engine.step()
    return {"status": "one tick"}


@router.post("/start")
async def start_world():
    asyncio.create_task(game_engine.start())
    return {"status": "world started"}

@router.post("/stop")
def stop_world():
    game_engine.stop()
    return {"status": "world stopped"}

@router.post("/print")
def print_world():
    res=query_service.query_world() 
    return res
# @router.post("/player/move")
# def move_player(req: MoveRequest):

#     # 生成 Action
#     action = MoveAction(
#         entity_id=req.entity_id,
#         target_position=(req.target_x, req.target_y)
#     )

#     # 加入调度队列
#     world.scheduler.schedule(action)

#     return {"status": "ok"}