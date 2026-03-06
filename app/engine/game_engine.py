import asyncio

# engine 控制时间
# service 控制行为
# 所以是engine调用service，而不是router ->直接-> service
class GameEngine:

    def __init__(self,world_service, tick_rate=0.2):
        self.world_service = world_service
        self.tick_rate = tick_rate
        self.running = False

    async def start(self):
        self.running = True
        while self.running:
            self.world_service.tick_world()
            await asyncio.sleep(self.tick_rate)

    def stop(self):
        self.running = False

    def step(self):
        self.world_service.tick_world()