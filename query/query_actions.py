from actions.action import Action
from components.man_attr import Hunger, Mood, Name
import my_enum

#只有复杂query采用class，比如排行榜，战斗目标选择器，条件匹配器
def print_entity(entity,world):
    hunger = world.get_entity_component(entity, Hunger).value
    mood = world.get_entity_component(entity, Mood).mood
    name = world.get_entity_component(entity, Name).name

    return f"{name}(happy={mood})(stomagche={hunger})"
    