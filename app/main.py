import logging
import os
from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.api.router.world_router import router as world_router
from app.api.router.action_router import router as action_router
from app.api.router.entity_router import router as entity_router
from app.container import build_container
from app.domain.errors import EntityCapacityExceeded


def setup_logging():
    level_name = os.getenv("LOG_LEVEL", "INFO").upper()
    level = getattr(logging, level_name, logging.INFO)
    logging.basicConfig(
        level=level,
        format="%(asctime)s %(levelname)s %(name)s - %(message)s",
    )


@asynccontextmanager
async def lifespan(app: FastAPI):
    setup_logging()
    app.state.container = build_container()
    try:
        yield
    finally:
        await app.state.container.game_engine.shutdown()


app = FastAPI(lifespan=lifespan)
app.include_router(world_router)
app.include_router(action_router)
app.include_router(entity_router)


@app.exception_handler(EntityCapacityExceeded)
async def handle_entity_capacity(request: Request, exc: EntityCapacityExceeded):
    return JSONResponse(
        status_code=409,
        content={
            "error": "entity_capacity_exceeded",
            "detail": str(exc),
        },
    )
