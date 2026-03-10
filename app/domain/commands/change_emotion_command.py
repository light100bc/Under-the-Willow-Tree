import numpy as np

from app.domain.simulation.l2.components.attr import EmotionData


class EmotionChangeCommand:
    def __init__(self, eids, moods, values):
        self.eids = np.array(eids)
        self.moods = np.array(moods)
        self.values = np.array(values)

    def apply(self, world):
        emotion_data = world.l2.components[EmotionData]
        for eid, mood, value in zip(self.eids, self.moods, self.values):
            emotion_data.moods[mood][eid] = value
