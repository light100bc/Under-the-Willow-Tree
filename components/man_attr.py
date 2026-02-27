import my_enum


class Hunger:
    def __init__(self, value=0):
        self.value = value

class Mood:
    def __init__(self):
        self.mood={}
        for mood in my_enum.MOOD:
            self.mood[mood] = 0

class Name:
    def __init__(self, name):
        self.name = name


class Marriage:
    def __init__(self):
        self.spouse = None

