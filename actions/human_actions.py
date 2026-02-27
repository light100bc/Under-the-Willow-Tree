from actions.action import Action
from actions.human_entity_actions import Set_Mood
from components.man_attr import Hunger
from core.event_bus import EventBus
import my_enum

def import_function():
    #如果放开头就变成互相循环引用，会报错
    #这里做一个延迟引用
    from system.system import MarriageSystem


    def apply(self,world):
        pass
    
#只对自己影响，不需要event_bus
class Eat(Action):
    def apply(self,world):
        hunger = world.get_entity_component(self.entity, Hunger)
        world.dispatch(Set_Mood(self.entity,my_enum.MOOD.HAPPY,5,my_enum.MOOD_METHOD.CALCULATE))
        hunger.value += 5

# 即使marriage是一个system，还是有action部分。
# action部分是行动（只影响actor自己不影响世界或其它npc，比如睡觉），system部分是规则和更新状态
class Marry(Action):
    def __init__(self,actor,target,system):
        self.marriage_system = system
        self.actor=actor
        self.target=target
    def apply(self,world):
        # 自己世界的marriage_system可以触发另一个世界的event_bus
        self.marriage_system.marry(self.actor,self.target,world)