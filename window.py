import tkinter as tk

class DragDropApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("400x400")
        self.create_widgets()
        
    def create_widgets(self):
        self.label = tk.Label(self.root, text="Enter the number of lines:")
        self.label.pack(pady=10)
        
        self.entry = tk.Entry(self.root)
        self.entry.pack(pady=10)
        
        self.button = tk.Button(self.root, text="Create Lines", command=self.create_lines)
        self.button.pack(pady=10)
        
        self.lines_frame = tk.Frame(self.root)
        self.lines_frame.pack(pady=20)
        
    def create_lines(self):
        for widget in self.lines_frame.winfo_children():
            widget.destroy()
        
        try:
            num_lines = int(self.entry.get())
        except ValueError:
            num_lines = 0
        
        for i in range(num_lines):
            lbl = tk.Label(self.lines_frame, text=f"Line {i+1}", bg="lightblue", width=20)
            lbl.grid(row=i, column=0, padx=10, pady=5)
            lbl.bind("<B1-Motion>", self.on_drag)
        
    def on_drag(self, event):
        widget = event.widget
        widget.place(x=event.x_root, y=event.y_root)

def main():
    root = tk.Tk()
    app = DragDropApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
