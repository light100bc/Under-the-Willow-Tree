class AISystem:
    def update(self, world):
        for npc in world.npcs:
            actions = npc.ai.choose_action(npc, world)
            if actions:
                for action in actions:
                    world.dispatch(action)