
import my_enum
import actions
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

        a.spouse = b
        b.spouse = a

        world.event_bus.emit("marriage", {"a": a, "b": b})

class EmotionSystem:
    def __init__(self,world):
        self.world=world
        #订阅event_bus这个事件处理器，有marriage事件时，触发on_marriage
        world.event_bus.subscribe("marriage", self.on_marriage)
        
    def on_marriage(self, data):
        a = data["a"]
        b = data["b"]
        a.spouse=b
        b.spouse=a
        a.set_mood(my_enum.MOOD.HAPPY, 20, my_enum.MOOD_METHOD.CALCULATE) 
        b.set_mood(my_enum.MOOD.HAPPY, 20, my_enum.MOOD_METHOD.CALCULATE)
        
        #事件触发action
        #如果结婚，所有有家庭的人都吃饭（这里循环，人数少可以直接写仅这两个人吃饭）
        # for npc in self.world.npcs:
        #     if hasattr(npc, "spouse") and npc.spouse:
        #         action = actions.Eat(npc)  # 吃饭
        #         self.world.dispatch(action)
    # def on_eat(self, data):
    #     data.set_mood(my_enum.MOOD.HAPPY, 10, my_enum.MOOD_METHOD.CALCULATE)