import asyncio


class GameEngine:
    def __init__(self, world_service, tick_rate=0.2):
        self.world_service = world_service
        self.tick_rate = tick_rate
        self.running = False
        self._task = None

    async def _run_loop(self):
        loop = asyncio.get_running_loop()
        next_tick = loop.time()
        try:
            while self.running:

                now = loop.time()

                while now >= next_tick:
                    self.world_service.tick_world()
                    next_tick += self.tick_rate

                await asyncio.sleep(0)
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
