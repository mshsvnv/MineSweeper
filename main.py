import tkinter as tk

root = tk.Tk()            # window

# window settings
root.configure(bg = "light green")  # some features of the window
root.geometry('500x500')  # size of the window
root.title("My Game")     # name of the window
root.resizable(False, False)  # disability of resizable

root.mainloop()