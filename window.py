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

        phonics_lines = tk.LabelFrame(self.window,text="Lines", pady=20)
        phonics_lines.pack(pady=20)

        label_inside_phonics_lines = tk.Label(phonics_lines, text="This is inside", font=("Arial", 12))
        label_inside_phonics_lines.pack(pady=10)


def main():
    window = tk.Tk()
    app = DragDropApp(window)
    window.mainloop()

if __name__ == "__main__":
    main()
