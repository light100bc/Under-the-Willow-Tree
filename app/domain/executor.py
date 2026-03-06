from app.domain.actions.spawn_action import CreateNPC
from app.domain.actions.human_behaviour_actions import Eat
from app.domain.actions.human_entity_actions import SetMood
from app.domain.system.eat_system import EatSystem
from app.domain.system.emotion_system import EmotionSystem
from app.domain.system.spawn_system import SpawnSystem


class Executor:
    def __init__(self, world):
        self.world = world

        self.systems = {
            SetMood: EmotionSystem(world),
            Eat:EatSystem(world),
            # "move": MovementSystem(world),
            CreateNPC: SpawnSystem(world),
        }

    def execute(self, actions):

        #actions = [
#     EatAction(1),
#     EatAction(5),
#     MoveAction(3),
#     EatAction(8),
# ]
# =>合并成
# grouped = {
#     "eat": [EatAction(1), EatAction(5), EatAction(8)],
#     "move": [MoveAction(3)]
# }
        # 按类型分组
        # action和执行分开，才可批处理（多个actions合并）
        while actions:

            grouped = {}

            for action in actions:
                grouped.setdefault(type(action), []).append(action)

            new_actions=[] #action可能触发其它action，用循环在同一个tick做掉

            # 分发给 system
            for action_type, acts in grouped.items():
                system = self.systems.get(action_type)
                if system:
                    res=system.process(acts)
                    if res:
                        new_actions.extend(res)

            actions= new_actions