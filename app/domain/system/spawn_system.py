    
import numpy as np

from app.domain.simulation.l2.components.attr import NameData
from app.config import my_enum

class SpawnSystem:
    def __init__(self,world):
        self.world = world
    def process(self, actions):
        from  app.domain.simulation.l2.components.attr import HungerData, PositionData, EmotionData

        eids=[]
        name=[]
        x=[]
        y=[]
        for action in actions:
            if type(action.name)==list:
                eids.extend([self.world.entity_index.create() for i in range(len(action.name))])
                name.extend(action.name)
                x.extend(action.x)
                y.extend(action.y)
            else:
                name.append(action.name)
                x.append(action.x)
                y.append(action.y)
                eid = self.world.entity_index.create()
                eids.append(eid)


        self.world.l2.components[NameData].name[eids] = name
        self.world.l2.components[PositionData].x[eids] = x #???是否要分开赋值x,y
        self.world.l2.components[PositionData].y[eids] = y
        self.world.l2.components[HungerData].value[eids] = [30 for i in range(len(eids))]
        for emotion in my_enum.MOOD:
            self.world.l2.components[EmotionData].moods[emotion][eids] = np.array([0 for i in range(len(eids))])
