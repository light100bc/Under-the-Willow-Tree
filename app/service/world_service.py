class WorldService:

    def __init__(self, world):
        self.world = world

    def tick_world(self):
        # 可以加锁
        self.world.update()

        # 可以加日志
        print("world ticked")

        # 可以加持久化
        # self.save_snapshot()