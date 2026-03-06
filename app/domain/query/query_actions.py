from app.domain.actions.action import Action

import app.config.my_enum as my_enum

#只有复杂query采用class，比如排行榜，战斗目标选择器，条件匹配器
def print_entity(world):
    eids=world.entity_index.active_ids
    res=""
    for eid in eids:
        res+="eid:"+str(eid)
        res+=print_single_entity(eid,world)
    return res

def print_single_entity(entity,world):
    res=""
    for component_name, component_values in  world.l2.components.items():
        for attr, value in vars(component_values).items():
            if attr=='moods':
                for mood in my_enum.MOOD:
                    res+=f"{str(component_name).split(".")[-1]}:{attr}:{mood}={value[mood][entity]}\n)"
            else:
                res+=f"{str(component_name).split(".")[-1]}:{attr}={value[entity]}\n)"
    return res
    