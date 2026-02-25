from actions import Eat
from character import MAN


class GameController:
    def __init__(self, world):
        self.world = world
        self.npc_count = 0

    def create_npc(self,name):
        if not name or name in self.world.npcs:
            return
        name = f"NPC_{name}"
        self.npc_count += 1
        npc = MAN(name)
        self.world.add_npc(npc)

    def feed_npc(self, npc):
        if npc:
            action = Eat(npc)
            self.world.dispatch(action)