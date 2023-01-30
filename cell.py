from tkinter import Button
import random as r
import settings as st
class Cell:

    all = []

    def __init__(self, x, y, is_mine = False):
        self.is_mine = is_mine
        self.cell_btn_object = None
        self.x = x
        self.y = y

        # добавить ячейку к списку Cell.all
        Cell.all.append(self)

    def create_btn_object(self, location):
        btn = Button(
            location,
            width = 12,
            height  = 4
        )

        btn.bind('<Button-1>', self.left_click_actions) # Left click
        btn.bind('<Button-3>', self.right_click_actions) # Right click
        
        self.cell_btn_object = btn

    def left_click_actions(self, event):
        if self.is_mine:
            self.show_mine()
        else:
            self.show_cell()

    def get_cell_by_axis(self, x, y):
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell

    @property
    def surrounded_cells(self):
        cells = []

        for x in range(self.x - 1, self.x + 2): 
            for y in range(self.y - 1, self.y + 2):
                new_cell = self.get_cell_by_axis(x, y) 

                if (new_cell is not None):
                    if (new_cell.x != self.x or new_cell.y != self.y):
                        cells.append(new_cell)

        return cells

    @property
    def surrounded_cells_mines_length(self):
        counter = 0
        for cell in self.surrounded_cells:
            if cell.is_mine:
                counter += 1
        return counter

    def show_cell(self):
        print(self.surrounded_cells_mines_length)

    def show_mine(self):
        self.cell_btn_object.configure(bg = 'magenta')

    def right_click_actions(self, event):
        print('I am righter!')

    @staticmethod
    def randomize_mines():
        picked_cells = r.sample(
            Cell.all, 
            st.MINES_COUNT
        )

        for cell in picked_cells:
            cell.is_mine = True

    def __repr__(self):
        return f"Cell({self.x}, {self.y})"




    