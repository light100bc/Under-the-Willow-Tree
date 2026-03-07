from app.domain.actions.action import Action
import app.config.my_enum as my_enum


def import_function():
    # If this import is moved to module scope it introduces a circular dependency.
    from domain.system.emotion_system import MarriageSystem
    return MarriageSystem


class Eat(Action):
    def __init__(self, entity=None, value=None):
        super().__init__(entity)
        self.value = [] if value is None else value


class Marry(Action):
    def __init__(self, actor, target, system):
        self.marriage_system = system
        self.actor = actor
        self.target = target

    def apply(self, world):
        self.marriage_system.marry(self.actor, self.target, world)
