from actions.action import Action
from components.man_attr import Hunger, Mood, Name
import my_enum

class Set_Mood(Action):
    def __init__(self, entity,mood,value,method=my_enum.MOOD_METHOD.SET):
        self.entity = entity
        self.mood = mood
        self.method = method
        self.value=value

    def apply(self,world):
        if not self.mood or self.mood not in my_enum.MOOD: return
        moods = world.get_entity_component(self.entity, Mood).mood
        if self.method == my_enum.MOOD_METHOD.SET:
            moods[self.mood] = self.value
        else:
            moods[self.mood] += self.value
            if moods[self.mood] < 0:
                moods[self.mood] = 0
            if moods[self.mood] > 120:
                moods[self.mood] = 120