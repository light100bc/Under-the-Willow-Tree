from app.domain.simulation.l2.Entity_Index import EntityIndex
from app.domain.simulation.l2.L2_Components import L2Components
from app.engine.event_bus import EventBus
from app.engine.scheduler import Scheduler
from app.engine.time_system import TimeSystem


class World:
    def __init__(self):
        self.l2 = L2Components(capacity=5000)
        self.entity_index = EntityIndex(5000)

        self.systems = {}
        self.time = TimeSystem()
        self.scheduler = Scheduler(self)
        self.running = False
        self.action_queue = []
        self.event_bus = EventBus()

    def add_system(self, name, system):
        self.systems[name] = system

    def get_system(self, name):
        return self.systems.get(name)

    def update(self):
        self.time.advance()

        actions = []
        for action in actions:
            self.scheduler.schedule(action)

        self.scheduler.process()
