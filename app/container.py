from dataclasses import dataclass

from app.domain.system.hunger_system import HungerSystem
from app.domain.system.spawn_system import SpawnSystem
from app.domain.system.emotion_system import EmotionSystem
from app.domain.world import World
from app.engine.game_engine import GameEngine
from app.service.action_service import ActionService
from app.service.entity_service import EntityService
from app.service.query_service import QueryService
from app.service.world_service import WorldService


@dataclass
class AppContainer:
    world: World
    world_service: WorldService
    action_service: ActionService
    entity_service: EntityService
    query_service: QueryService
    game_engine: GameEngine


def generate_world(world: World) -> None:
    world.add_system(HungerSystem, HungerSystem(world))
    world.add_system(SpawnSystem, SpawnSystem(world))
    world.add_system(EmotionSystem, EmotionSystem(world))


def build_container() -> AppContainer:
    world = World()
    generate_world(world)

    world_service = WorldService(world)
    action_service = ActionService(world)
    entity_service = EntityService(world)
    query_service = QueryService(world)
    game_engine = GameEngine(world_service)

    return AppContainer(
        world=world,
        world_service=world_service,
        action_service=action_service,
        entity_service=entity_service,
        query_service=query_service,
        game_engine=game_engine,
    )
