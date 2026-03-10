class CommandBuffer:

    def __init__(self):
        self.commands = []

    def add(self, cmd):
        self.commands.append(cmd)

    def apply(self, world):

        for cmd in self.commands:
            cmd.apply(world)

        self.commands.clear()