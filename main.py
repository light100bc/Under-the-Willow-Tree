import time

from controller.game_controller import GameController
import my_enum
from ai.AI_system import AISystem
from system.system import EmotionSystem, MarriageSystem
from ui.ui import GameUI
from core.world import World
from entity.character import MAN
import tkinter as tk

def generate_world(world):
    world.add_system(my_enum.SYSTEM.MarriageSystem,MarriageSystem(world))
    world.add_system(my_enum.SYSTEM.EmotionSystem,EmotionSystem(world))
    world.add_system(my_enum.SYSTEM.AISystem,AISystem())

def main():
    world = World()
    generate_world(world)
    controller = GameController(world)

    root = tk.Tk()
    ui = GameUI(root, controller, world)

    def game_loop():
        world.update()       # 更新世界
        ui.refresh()         # 刷新UI
        root.after(1000, game_loop)  # 1秒后再调用

    root.after(1000, game_loop)

    root.mainloop()

if __name__ == "__main__":
    main()