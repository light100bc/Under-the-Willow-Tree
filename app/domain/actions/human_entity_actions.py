from app.domain.actions.action import Action
import app.config.my_enum as my_enum

class SetMood(Action):
    def __init__(self, entity,mood,value,method=my_enum.MOOD_METHOD.SET):
        self.entity = entity
        self.mood = mood
        self.value=value
        self.method = method

    # def apply(self,world):
    #     if not self.mood or self.mood not in my_enum.MOOD: return
    #     moods = world.get_entity_component(self.entity, Mood).mood
    #     if self.method == my_enum.MOOD_METHOD.SET:
    #         moods[self.mood] = self.value
    #     else:
    #         moods[self.mood] += self.value
    #         if moods[self.mood] < 0:
    #             moods[self.mood] = 0
    #         if moods[self.mood] > 120:
    #             moods[self.mood] = 120