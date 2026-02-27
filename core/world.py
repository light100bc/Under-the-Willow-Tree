from ai.AI_system import AISystem
from core.event_bus import EventBus
from entity.character import MAN
from system.system import EmotionSystem, MarriageSystem
import my_enum
import actions.human_actions as human_actions

class World:
    def __init__(self):
        # self.npcs = []
 
        self.next_entity_id = 1
        self.entities = set()

        # 组件池（核心）
        self.components = {}

        self.systems = {}
        self.action_queue = []

        #这个world内的message传输管道
        self.event_bus = EventBus()

    # ===== Entity =====
    def create_entity(self):
        eid = self.next_entity_id
        self.next_entity_id += 1
        self.entities.add(eid)
        return eid
    
    # ===== Component =====
    def add_component(self, entity, component):
        comp_type = type(component)

        if comp_type not in self.components:
            self.components[comp_type] = {}

        self.components[comp_type][entity] = component

    def get_component(self, comp_type):
        return self.components.get(comp_type, {})

    def get_entity_component(self, entity, comp_type):
        return self.components.get(comp_type, {}).get(entity)

    # ===== System =====
    def add_system(self, name,system):
        self.systems[name]=system

    # 会改变entity或者component的action放dispatch，查询类的不放
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
        ai_system=self.systems[my_enum.SYSTEM.AISystem]
        if ai_system:
            ai_system.update(self)

        current_actions = self.action_queue
        self.action_queue = []
        for action in current_actions:
            action.apply(self)