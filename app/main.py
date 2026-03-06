import asyncio
from fastapi import FastAPI
from fastapi import APIRouter
from app.api.router.world_router import router as world_router
from app.api.router.action_router import router as action_router
from app.api.router.entity_router import router as entity_router

app = FastAPI()
router = APIRouter()
app.include_router(world_router)
app.include_router(action_router)
app.include_router(entity_router)
# app.include_router(npc_router)


@app.on_event("startup")
async def startup_event():
    #  asyncio.create_task(game_engine.start())
     pass


