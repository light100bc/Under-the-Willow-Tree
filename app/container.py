# 实例化 ≠ 业务逻辑
# 实例化属于：
# 应用启动阶段（bootstrap）
# 这层只负责：创建对象 # 组装依赖 # 注入依赖

from app.config import my_enum
# from engine.decisions.AI_system import AISystem
# from engine.simulation.l2.system.system import EmotionSystem, MarriageSystem
from app.domain.system.eat_system import EatSystem
from app.domain.system.spawn_system import SpawnSystem
from app.domain.system.emotion_system import EmotionSystem
from app.domain.world import World
from app.engine.game_engine import GameEngine
from app.service.action_service import ActionService
from app.service.entity_service import EntityService
from app.service.query_service import QueryService
from app.service.world_service import WorldService

def generate_world(world):
    # world.add_system(my_enum.SYSTEM.MarriageSystem, MarriageSystem(world))
    # world.add_system(my_enum.SYSTEM.EmotionSystem, EmotionSystem(world))
    # world.add_system(my_enum.SYSTEM.AISystem, AISystem())
    world.add_system(EatSystem,EatSystem(world))
    world.add_system(SpawnSystem, SpawnSystem(world))
    world.add_system(EmotionSystem, EmotionSystem(world))

world = World()
generate_world(world)
world_service = WorldService(world)
action_service=ActionService(world)
entity_service=EntityService(world)
query_service=QueryService(world)
game_engine=GameEngine(world_service)
