
from actions.human_entity_actions import Set_Mood
from components.man_attr import Marriage
import my_enum
import actions.human_actions as human_actions
# 判断can marry，复杂计算（比如happy增加值设计personality）
#只影响“单个个体内部状态”的行为，可以只用 Action 类。
# system用于规则，是action发生后触发的规则
# action用class因为涉及多个实体 / 合法性判断的行为
class MarriageSystem:
    def __init__(self,world):
        self.world=world

    def marry(self, a, b,world):
        if world==None:
            world=self.world
        marriage_pool = world.get_component(Marriage)
        marriage_pool[a].spouse = b
        marriage_pool[b].spouse = a

        world.event_bus.emit("marriage", {"a": a, "b": b})

class EmotionSystem:
    def __init__(self,world):
        self.world=world
        #订阅event_bus这个事件处理器，有marriage事件时，触发on_marriage
        world.event_bus.subscribe("marriage", self.on_marriage)
        
    def on_marriage(self, data):
        a = data["a"]
        b = data["b"]
        self.world.dispatch(Set_Mood(a,my_enum.MOOD.HAPPY,20,my_enum.MOOD_METHOD.CALCULATE))
        self.world.dispatch(Set_Mood(b,my_enum.MOOD.HAPPY,20,my_enum.MOOD_METHOD.CALCULATE))