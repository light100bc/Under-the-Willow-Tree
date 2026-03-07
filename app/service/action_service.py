from app.domain.actions.human_behaviour_actions import Eat


class ActionService:
    def __init__(self, world):
        self.world = world

    def eat(self, npc_id,value):
        action = Eat(npc_id,value)
        self.world.scheduler.schedule(action)