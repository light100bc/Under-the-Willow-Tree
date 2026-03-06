class TimeSystem:
    def __init__(self):
        self.tick_count = 0

    def advance(self):
        self.tick_count += 1