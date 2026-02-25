import tkinter as tk


class GameUI:
    def __init__(self, root, controller, world):
        self.controller = controller
        self.world = world

        self.root = root
        self.root.title("NPC Simulator")

        self.listbox = tk.Listbox(root,width=5000)
        self.listbox.pack()

        self.input = tk.Entry(root)
        self.input.pack()

        self.create_button = tk.Button(
            root, text="Create NPC",  
            command=lambda: self.create_npc(self.input.get())
        )
        self.create_button.pack()

        self.feed_button = tk.Button(
            root, text="Feed Selected NPC", command=self.feed_selected
        )
        self.feed_button.pack()

        self.refresh()

    def create_npc(self,input):
        self.controller.create_npc(input)
        self.refresh()

    def feed_selected(self):
        selection = self.listbox.curselection()
        if selection:
            index = selection[0]
            npc = self.world.npcs[index]
            self.controller.feed_npc(npc)
            self.refresh()

    def refresh(self):
        self.listbox.delete(0, tk.END)
        for npc in self.world.npcs:
            self.listbox.insert(tk.END, str(npc))