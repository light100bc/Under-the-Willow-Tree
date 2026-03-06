
class CreateNPC:
    def __init__(self, name=list(),x=list(),y=list()):
        self.name = name
        self.x=x
        self.y=y

    #不可以在这里实现apply，这样就是oop模式了
    #Action = 纯数据
    # System = 规则
    # World = 规则执行者
    # def apply(self, world):
    #     from l2.components.attr import HungerData, PositionData, EmotionData

    #     eid = world.entity_index.create()
    #     world.l2.components[HungerData][eid].value=10
    #     world.l2.components[HungerData][eid].max=50
    #     world.l2.components[PositionData][eid].x=0
    #     world.l2.components[PositionData][eid].y=0
    #     world.l2.components[EmotionData][eid].moods[my_enum.MOOD.HAPPY] = 0

    #     new_id = self.world.l2.create_entity()

    #     self.world.l2.position.x[new_id] = action.x
    #     self.world.l2.position.y[new_id] = action.y

    #     self.world.l2.hunger.value[new_id] = 0.5