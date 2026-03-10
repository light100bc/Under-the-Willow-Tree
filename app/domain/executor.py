from app.domain.actions.spawn_action import CreateNPC
from app.domain.actions.human_behaviour_actions import Eat
from app.domain.actions.human_entity_actions import SetMood
from app.domain.system.eat_system import EatSystem
from app.domain.system.emotion_system import EmotionSystem
from app.domain.system.spawn_system import SpawnSystem


class Executor:
    def __init__(self, world):
        self.world = world
        self.system_types = {
            SetMood: EmotionSystem,
            Eat: EatSystem,
            CreateNPC: SpawnSystem,
        }

    def execute(self, actions):
        while actions:

            grouped = {}

            for action in actions:
                grouped.setdefault(type(action), []).append(action)

            futures = []
            for action_type, acts in grouped.items():
                system_type = self.system_types.get(action_type)
                system = self.world.get_system(system_type) if system_type else None
            if system:
                futures.append(self.pool.submit(system.process, acts))

            new_actions = []
            for f in futures:
                res = f.result()
                if res:
                    new_actions.extend(res)

            return new_actions
