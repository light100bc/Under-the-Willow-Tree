from ai.ai import SimpleAI
import my_enum

class MAN():

    def __init__(self,name,sex=None,father=None,mother=None):
        self.name = name
        self.sex = sex
        self.father = father
        self.mother = mother
        self.hunger=40
        self.mood={}
        self.ai = SimpleAI()
        for mood in my_enum.MOOD:
            self.mood[mood] = 0

    def __repr__(self):
        return f"{self.name}(happy={self.mood})(stomagche={self.hunger})"
    

    def set_mood(self,mood,value,method=my_enum.MOOD_METHOD.SET):
        if not mood or mood not in my_enum.MOOD: return
        if method == my_enum.MOOD_METHOD.SET:
            self.mood[mood] = value
        else:
            self.mood[mood] += value
            if self.mood[mood] < 0:
                self.mood[mood] = 0
            if self.mood[mood] > 120:
                self.mood[mood] = 120
    
    # 统一调用接口
    # def perform(self, action, event_bus):
    #     action.apply(event_bus)