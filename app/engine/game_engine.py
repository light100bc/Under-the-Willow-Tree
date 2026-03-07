import asyncio


class GameEngine:
    def __init__(self, world_service, tick_rate=0.2):
        self.world_service = world_service
        self.tick_rate = tick_rate
        self.running = False
        self._task = None

    async def _run_loop(self):
        try:
            while self.running:
                self.world_service.tick_world()
                await asyncio.sleep(self.tick_rate)
        finally:
            self.running = False
            self._task = None

    def start(self):
        if self.running and self._task and not self._task.done():
            return False

        self.running = True
        self._task = asyncio.create_task(self._run_loop())
        return True

    def stop(self):
        self.running = False

    async def shutdown(self):
        self.stop()
        if self._task:
            await self._task

    def step(self):
        self.world_service.tick_world()
