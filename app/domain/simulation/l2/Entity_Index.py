from app.domain.errors import EntityCapacityExceeded


class EntityIndex:
    def __init__(self, capacity):
        self.capacity = capacity
        self.free_ids = list(range(capacity))
        self.active_ids = set()
        self.l3_ids = set()

    def remaining_count(self):
        return len(self.free_ids)

    def create(self):
        if not self.free_ids:
            raise EntityCapacityExceeded(self.capacity, 0)
        eid = self.free_ids.pop()
        self.active_ids.add(eid)
        return eid

    def remove(self, eid):
        if eid not in self.l3_ids:
            self.active_ids.remove(eid)
            self.free_ids.append(eid)
            return 1
        return 0

    def create_l3_id(self, eid=None):
        if eid:
            self.l3_ids.add(eid)
            return eid
        eid = self.create()
        self.l3_ids.add(eid)
        return eid

    def remove_l3_id(self, eid):
        self.l3_ids.remove(eid)
