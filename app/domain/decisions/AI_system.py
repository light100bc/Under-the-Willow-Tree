from ai.ai import SimpleAI

class AISystem:
    def update(self, world):
        for entity in world.entities:
            ai=SimpleAI()
            actions = ai.choose_action(entity, world)
            if actions:
                for action in actions:
                    world.dispatch(action)