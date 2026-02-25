from AI_system import AISystem
from event_bus import EventBus
from character import MAN
from system import EmotionSystem, MarriageSystem
import my_enum
import actions

class World:
    def __init__(self):
        self.npcs = []
        self.action_queue=[]

        self.event_bus = EventBus()

        self.marriage_system = MarriageSystem(self)
        self.emotion_system = EmotionSystem(self)
        self.ai_system = AISystem()

    def add_npc(self, npc):
        self.npcs.append(npc)

    def dispatch(self, action):
        action.apply(self)
        # if isinstance(action, list):
        #     for a in action:
        #         a.apply(self)
        # else:
        #     action.apply(self)

    def dispatch_delay(self,action):
        if isinstance(action, list):
            self.action_queue.extend(action)
        else:
            self.action_queue.append(action)

    def update(self):
        # 简单示例：自动让前两个结婚
        self.ai_system.update(self)

        # current_actions = self.action_queue
        # self.action_queue = []
        # for action in current_actions:
        #     action.apply(self)