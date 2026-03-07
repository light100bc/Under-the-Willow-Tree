import logging


logger = logging.getLogger(__name__)


class WorldService:
    def __init__(self, world):
        self.world = world

    def tick_world(self):
        self.world.update()
        logger.debug("world ticked")
