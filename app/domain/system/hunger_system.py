import numpy as np

from app.domain.actions.human_entity_actions import SetMood
from app.domain.simulation.l2.components.attr import HungerData
from app.config import my_enum
from app.domain.commands.change_hunger_command import HungerChangeCommand

class HungerSystem:
    def __init__(self,world):
        self.world = world
    def process(self, actions,cmd_buffer):

        eids=[]
        values=[]
        for action in actions:
            if type(action.entity)==list:
                eids.extend(action.entity)
                values.extend(action.value)
            else:
                eids.append(action.entity)
                values.append(action.value)

        #只进行值改变，不参加逻辑
        eids = np.array(eids)
        values = np.array(values)
        
        # 聚合重复eid
        acc = np.bincount(eids, weights=values)
        unique_eids = np.nonzero(acc)[0]
        unique_values = acc[unique_eids]

        eid_count=np.bincount(eids)[unique_eids]

        cmd_buffer.add(
            HungerChangeCommand(unique_eids, unique_values)
        )

        new_actions=[]
        new_actions.append(SetMood(unique_eids,[my_enum.MOOD.HAPPY]*len(unique_eids),np.array(5*eid_count),[my_enum.MOOD_METHOD.CALCULATE]*len(unique_eids)))
        return new_actions