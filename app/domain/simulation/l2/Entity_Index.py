class EntityIndex:
    def __init__(self, capacity):
        self.free_ids = list(range(capacity))
        self.active_ids = set()
        self.l3_ids=set() #被选为L3的id

    def create(self):
        eid = self.free_ids.pop()
        self.active_ids.add(eid)
        return eid

    def remove(self, eid):
        #要remove l2 entity，先要remove它的l3 entity
        if eid not in self.l3_ids:
            self.active_ids.remove(eid)
            self.free_ids.append(eid)
            return 1
        else:
            return 0

    def create_l3_id(self,eid=None):
        if eid:
            self.l3_ids.add(eid)
            return eid
        else:   
            eid=self.create()
            self.l3_ids.add(eid)
            return eid
    
    def remove_l3_id(self,eid):
        self.l3_ids.remove(eid)

