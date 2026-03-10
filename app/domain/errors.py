class EntityCapacityExceeded(Exception):
    def __init__(self, capacity, remaining):
        self.capacity = capacity
        self.remaining = remaining
        super().__init__(
            f"entity capacity exceeded: capacity={capacity}, remaining={remaining}"
        )
