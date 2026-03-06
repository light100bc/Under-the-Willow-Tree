import numpy as np

import app.config.my_enum as my_enum


class HungerData:
    def __init__(self, capacity):
        self.value = np.zeros(capacity)
        self.max = np.ones(capacity)
        self.decay = np.full(capacity, 0.01)
        self.threshold = np.full(capacity, 0.8)

class PositionData:
    def __init__(self, capacity):
        self.x = np.zeros(capacity)
        self.y = np.zeros(capacity)

class EmotionData:
    def __init__(self, capacity):
        self.moods={}
        for mood in my_enum.MOOD:
            self.moods[mood] = np.zeros(capacity)

class NameData:
    def __init__(self, capacity):
        self.name = np.empty(5000, dtype="U20")