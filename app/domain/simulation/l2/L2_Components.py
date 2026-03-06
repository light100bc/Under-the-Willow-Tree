# simulation/l2/components.py

import numpy as np

from app.domain.simulation.l2.components.attr import NameData
from app.domain.simulation.l2.components.attr import EmotionData, HungerData, PositionData

class L2Components:
    def __init__(self, capacity):

        self.capacity = capacity

        self.components={}
        self.components.update({NameData: NameData(capacity), HungerData:  HungerData(capacity), 
                                PositionData: PositionData(capacity), EmotionData: EmotionData(capacity)})
    
    # ===== Component =====
    # 大型游戏很多entity，用这个方法存component list，可以并发执行
    # 小型游戏可以加一个entity class，里面只有访问接口，存放自己的component和访问component
    # ??? 初始化哪里调用add_component ???
    # 如何在这里初始化class，参数为capacity
    def add_component(self, component):
        comp_type = type(component)

        if comp_type not in self.components:
             self.components.update({comp_type:comp_type(self.capacity)})

    def get_component(self, comp_type):
        return self.components.get(comp_type)

    # 存储的是5000长np.array，由entity_index管理
    # 所以不能获取entity，因为5000个都存在里面了
    # 下面的方法存的是（面向对象的DOD）：
    #components = {
    #     Position: {1: Position(...), 2: Position(...)},
    #     Hunger: {1: Hunger(...)}
    #     }
    # def get_entity_component(self, entity, comp_type):
    #     return self.components.get(comp_type, {}).get(entity)
