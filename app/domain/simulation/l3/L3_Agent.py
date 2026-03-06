class L3Agent:
    def __init__(self, entity_id, world):
        self.entity_id = entity_id
        self.world = world

    def get_position(self):
        return self.world.l2.position[self.entity_id]