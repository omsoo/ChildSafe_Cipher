import tkinter as tk

class GraphicalPasswordInterface:
    def __init__(self, master):
        self.master = master
        self.master.title("Graphical Password Creation")
        # Header
        self.header_label = tk.Label(master, text="Create Your Graphical Password", font=("Helvetica", 16))
        self.header_label.pack(pady=10)

        # Grid Layout for Graphical Elements
        self.graphical_elements = ["🌟", "🎈", "🍕", "🚀", "🌈", "🐱", "🎨", "🐻"]  # Example graphical elements
        self.selected_elements = []

        self.grid_frame = tk.Frame(master)
        self.grid_frame.pack()

        for i, element in enumerate(self.graphical_elements):
            button = tk.Button(self.grid_frame, text=element, font=("Helvetica", 20), width=4, height=2,
                               command=lambda e=element: self.toggle_selection(e))
            button.grid(row=i // 4, column=i % 4, padx=5, pady=5)

        # Confirmation Button
        self.confirm_button = tk.Button(master, text="Confirm Selection", font=("Helvetica", 12),
                                        command=self.confirm_selection)
        self.confirm_button.pack(pady=10)

    def toggle_selection(self, element):
        if element in self.selected_elements:
            self.selected_elements.remove(element)
        else:
            self.selected_elements.append(element)

    def confirm_selection(self):
        if len(self.selected_elements) > 0:
            print("Selected Graphical Password:", " ".join(self.selected_elements))
            # Implement logic to proceed to the next step (registration phase)
        else:
            print("Please select at least one graphical element.")

def main():
    root = tk.Tk()
    app = GraphicalPasswordInterface(root)
    root.mainloop()

if __name__ == "__main__":
    main()
        
