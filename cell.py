from tkinter import Button

class Cell:

    def __init__(self, is_mine = False):
        self.is_mine = is_mine
        self.cell_btn_object = None

    def create_btn_object(self, location):
        btn = Button(
            location,
            text = "hey sweet"
        )

        btn.bind('<Button-1>', self.left_click_actions) # Left click
        btn.bind('<Button-3>', self.right_click_actions) # Right click
        
        self.cell_btn_object = btn

    def left_click_actions(self, event):
        print('I am lefter!')

    def right_click_actions(self, event):
        print('I am righter!')



    