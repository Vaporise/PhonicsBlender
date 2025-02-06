import tkinter as tk

class DragDropApp:
    def __init__(self, window): 
        self.window = window
        self.initialize_window() #runs the initialize_window method at runtime

    def initialize_window(self): #creates a window with a title, size and runs create_widgets
        self.window.title("Phonics Blender")
        self.window.geometry("900x900")
        self.create_widgets()
    
    def create_widgets(self): #creates widgets for the window of a label and a frame with a label within
        label = tk.Label(self.window, text="Hello, Tkinter!", font=("Arial", 16))
        label.pack(pady=20)

        phonics_lines = tk.LabelFrame(self.window,text="Lines", pady=20)
        phonics_lines.pack(pady=20)

        label_inside_phonics_lines = tk.Label(phonics_lines, text="This is inside", font=("Arial", 12))
        label_inside_phonics_lines.pack(pady=10)


def main():
    window = tk.Tk() # Creates the window
    app = DragDropApp(window) #for future use. It's an instance of the app.
    window.mainloop() #runs the window and loops it to update with user interaction.

if __name__ == "__main__":
    main()
