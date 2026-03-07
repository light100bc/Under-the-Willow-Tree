import numpy as np

from app.domain.actions.human_entity_actions import SetMood
from app.domain.simulation.l2.components.attr import HungerData
from app.config import my_enum

class EatSystem:
    def __init__(self,world):
        self.world = world
    def process(self, actions):

        eids=[]
        values=[]
        for action in actions:
            if type(action.entity)==list:
                eids.extend(action.entity)
                values.extend(action.value)
            else:
                eids.append(action.entity)
                values.append(action.value)

        self.world.l2.components[HungerData].value[eids] += values

        new_actions=[]
        new_actions.append(SetMood(eids,[my_enum.MOOD.HAPPY]*len(eids),np.array([5 for i in range(len(eids))]),[my_enum.MOOD_METHOD.CALCULATE]*len(eids)))
        return new_actions