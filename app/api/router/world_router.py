from fastapi import APIRouter, Request, Depends

router = APIRouter(prefix="/world")


def get_container(request: Request):
    return request.app.state.container


def get_engine(container=Depends(get_container)):
    return container.game_engine


@router.post("/tick")
def tick(engine=Depends(get_engine)):
    engine.step()
    return {"status": "one tick"}


@router.post("/start")
async def start_world(engine=Depends(get_engine)):
    started = engine.start()
    status = "world started" if started else "world already running"
    return {"status": status}


@router.post("/stop")
def stop_world(engine=Depends(get_engine)):
    engine.stop()
    return {"status": "world stopped"}


@router.post("/print")
def print_world(container=Depends(get_container)):
    return container.query_service.query_world()
