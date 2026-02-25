import time

from game_controller import GameController
from ui import GameUI
from world import World
from character import MAN
import tkinter as tk

def main():
    world = World()
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