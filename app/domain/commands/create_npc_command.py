import numpy as np

class SpawnNPCCommand:

    def __init__(self, eids, names, xs, ys):
        self.eids = np.array(eids)
        self.names = np.array(names)
        self.xs = np.array(xs)
        self.ys = np.array(ys)

    def apply(self, world):

        from app.domain.simulation.l2.components.attr import (
            NameData,
            PositionData,
            HungerData,
            EmotionData
        )
        from app.config import my_enum

        n = len(self.eids)

        world.l2.components[NameData].name[self.eids] = self.names

        world.l2.components[PositionData].x[self.eids] = self.xs
        world.l2.components[PositionData].y[self.eids] = self.ys

        world.l2.components[HungerData].value[self.eids] = np.full(n, 30)

        for emotion in my_enum.MOOD:
            world.l2.components[EmotionData].moods[emotion][self.eids] = np.zeros(n)