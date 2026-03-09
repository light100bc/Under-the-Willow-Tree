# core/world/scheduler.py

from collections import deque
from app.domain.executor import Executor
# 只是队列
# 不判断逻辑

class Scheduler:
    def __init__(self, world):
        self.world = world
        self.queue = deque()
        self.executor = Executor(world)

    def schedule(self, action):
        """
        加入行为队列
        """
        self.queue.append(action)

    def process(self):
        """
        执行所有行为
        """
        actions=[]
        actions = list(self.queue)
        self.queue.clear()
        while actions:
            actions = self.executor.execute(actions)