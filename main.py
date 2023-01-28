import tkinter as tk
import settings as st
import utils as ut

root = tk.Tk()            # window

# window settings
root.configure(bg = "light green")  # some features of the window
root.geometry(f'{st.WIDTH}x{st.HEIGHT}')  # size of the window
root.title("Sweeper Game")     # name of the window
root.resizable(False, False)  # disability of resizable

# frame settings
top_frame = tk.Frame(
    root, 
    bg = "light yellow",
    width = st.WIDTH,
    height = ut.height_prct(25)
)
top_frame.place(x = 0, y = 0)  # frame location

left_frame = tk.Frame(
    root,
    bg = "light blue",
    width = ut.width_prct(25),
    height = ut.height_prct(75)
)
left_frame.place(x = 0, y = ut.height_prct(25))

center_frame = tk.Frame(
    root,
    bg = "light pink",
    width = ut.width_prct(75),
    height = ut.height_prct(75)
)
center_frame.place(
    x = ut.width_prct(25),
    y = ut.height_prct(25)
)

# run the window
root.mainloop()
