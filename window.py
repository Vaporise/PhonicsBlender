import tkinter as tk

class DragDropApp:
    def __init__(self, window):
        self.window = window
        self.initialize_window()

    def initialize_window(self):
        self.window.title("Phonics Blender")
        self.window.geometry("900x900")
        self.create_widgets()
    
    def create_widgets(self):
        label = tk.Label(self.window, text="Hello, Tkinter!", font=("Arial", 16))
        label.pack(pady=20)

def main():
    window = tk.Tk()
    app = DragDropApp(window)
    window.mainloop()

if __name__ == "__main__":
    main()
