from app.domain.actions.action import Action
import app.config.my_enum as my_enum

def import_function():
    #如果放开头就变成互相循环引用，会报错
    #这里做一个延迟引用
    from domain.system.emotion_system import MarriageSystem
    
#只对自己影响，不需要event_bus
class Eat(Action):
    def __init__(self, entity=list(),value=list()):
        super().__init__(entity)
        self.value = value #吃了多少


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

