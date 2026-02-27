from actions.human_actions import Eat
from actions.system_actions import CreateNPC
from entity.character import MAN


class GameController:
    def __init__(self, world):
        self.world = world
        self.npc_count = 0

    def create_npc(self,name):
        self.world.dispatch(CreateNPC(name))

    def feed_npc(self, entity):
        self.world.dispatch(Eat(entity))