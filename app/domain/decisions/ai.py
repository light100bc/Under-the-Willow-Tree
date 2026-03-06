from actions.human_behaviour_actions import Eat, Marry
# from components.man_attr import Hunger, Marriage
import config.my_enum as my_enum


class SimpleAI:
    def choose_action(self, entity, world):
        actions=[]
        # if world.get_component(Marriage)[entity].spouse is None:
        #     for other in world.entities:
        #         if other != entity and world.get_component(Marriage)[other].spouse is None:
        #             actions.append(Marry(entity, other,world.systems.get(my_enum.SYSTEM.MarriageSystem)))  # Marry(npc, other,world.marriage_system)

        # if world.get_entity_component(entity, Hunger).value < 60:
        #     actions.append(Eat(entity))

        return actions