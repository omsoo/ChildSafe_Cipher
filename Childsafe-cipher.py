import tkinter as tk

class GraphicalPasswordInterface:
    def __init__(self, master):
        self.master = master
        self.master.title("Graphical Password Creation")

        # Header
        self.header_label = tk.Label(master, text="Create Your Graphical Password", font=("Helvetica", 16))
        self.header_label.pack(pady=10)