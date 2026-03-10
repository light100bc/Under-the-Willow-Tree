import numpy as np

from app.domain.simulation.l2.components.attr import NameData
from app.domain.commands.create_npc_command import SpawnNPCCommand
from app.domain.errors import EntityCapacityExceeded


class SpawnSystem:
    def __init__(self, world):
        self.world = world

    def process(self, actions, cmd_buffer):
        eids = []
        names = []
        xs = []
        ys = []

        for action in actions:
            if isinstance(action.name, list):
                count = len(action.name)
                if self.world.entity_index.remaining_count() < count:
                    raise EntityCapacityExceeded(
                        self.world.entity_index.capacity,
                        self.world.entity_index.remaining_count(),
                    )

                new_eids = [self.world.entity_index.create() for _ in range(count)]
                eids.extend(new_eids)
                names.extend(action.name)
                xs.extend(action.x)
                ys.extend(action.y)
            else:
                if self.world.entity_index.remaining_count() < 1:
                    raise EntityCapacityExceeded(
                        self.world.entity_index.capacity,
                        self.world.entity_index.remaining_count(),
                    )

                eid = self.world.entity_index.create()
                eids.append(eid)
                names.append(action.name)
                xs.append(action.x)
                ys.append(action.y)

        if not eids:
            return []

        cmd_buffer.add(SpawnNPCCommand(eids, names, xs, ys))
        return []
