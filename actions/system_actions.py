class CreateNPC:
    def __init__(self, name):
        self.name = name

    def apply(self, world):
        from components.man_attr import Name, Hunger, Marriage,Mood

        entity = world.create_entity()

        world.add_component(entity, Name(self.name))
        world.add_component(entity, Hunger())
        world.add_component(entity, Marriage())
        world.add_component(entity, Mood())