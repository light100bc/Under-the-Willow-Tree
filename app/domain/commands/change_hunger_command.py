import numpy as np

from app.domain.simulation.l2.components.attr import HungerData


class HungerChangeCommand:

    def __init__(self, eids, values):
        self.eids = np.array(eids)
        self.values = np.array(values)

    def apply(self, world):

        world.l2.components[HungerData].value[self.eids] += self.values