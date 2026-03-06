


from app.domain.query.query_actions import print_entity


class QueryService:
    def __init__(self, world):
        self.world = world

    def query_world(self):
        return print_entity(self.world)