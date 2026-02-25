from actions import Eat, Marry


class SimpleAI:
    def choose_action(self, npc, world):
        actions=[]
        if not hasattr(npc, "spouse") or npc.spouse is None:
            for other in world.npcs:
                if other != npc and (not hasattr(other, "spouse") or other.spouse is None):
                    actions.append(Marry(npc, other,world.marriage_system))  # Marry(npc, other,world.marriage_system)

        if npc.hunger < 60:
            actions.append(Eat(npc))

        return actions