from app.domain.actions.spawn_action import CreateNPC


class EntityService:
    def __init__(self, world):
        self.world = world

    def create_npc(self, name, x, y):
        action = CreateNPC(name, x, y)
        self.world.scheduler.schedule(action)