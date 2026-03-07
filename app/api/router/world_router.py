from fastapi import APIRouter, Request

router = APIRouter(prefix="/world")


def get_container(request: Request):
    return request.app.state.container


@router.post("/tick")
def tick(request: Request):
    get_container(request).game_engine.step()
    return {"status": "one tick"}


@router.post("/start")
async def start_world(request: Request):
    started = get_container(request).game_engine.start()
    status = "world started" if started else "world already running"
    return {"status": status}


@router.post("/stop")
def stop_world(request: Request):
    get_container(request).game_engine.stop()
    return {"status": "world stopped"}


@router.post("/print")
def print_world(request: Request):
    return get_container(request).query_service.query_world()
