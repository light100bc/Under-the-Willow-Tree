from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.router.world_router import router as world_router
from app.api.router.action_router import router as action_router
from app.api.router.entity_router import router as entity_router
from app.container import build_container


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.container = build_container()
    try:
        yield
    finally:
        await app.state.container.game_engine.shutdown()


app = FastAPI(lifespan=lifespan)
app.include_router(world_router)
app.include_router(action_router)
app.include_router(entity_router)
