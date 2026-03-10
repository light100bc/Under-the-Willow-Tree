from collections import deque

from app.domain.executor import Executor


class Scheduler:
    def __init__(self, world, cmd_buffer):
        self.world = world
        self.queue = deque()
        self.executor = Executor(world)
        self.cmd_buffer = cmd_buffer

    def schedule(self, action):
        self.queue.append(action)

    def schedule_batch(self, actions):
        self.queue.extend(actions)

    def process(self):
        actions = list(self.queue)
        self.queue.clear()
        while actions:
            actions = self.executor.execute(actions, self.cmd_buffer)
            self.cmd_buffer.apply(self.world)
