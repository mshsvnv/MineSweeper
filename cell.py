from tkinter import Button, Label, messagebox
import random as r
import settings as st
import ctypes, sys
class Cell:

    all = []
    cell_count_label_object = None
    cell_count = st.CELL_COUNT

    def __init__(self, x, y, is_mine = False):
        self.is_mine = is_mine
        self.is_opend = False
        self.is_mine_candidate = False
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

    @staticmethod
    def create_cell_count_label(location):
        lbl = Label(
            location,
            bg = "light blue",
            fg = "#333333",
            font = ("", 30),
            text = f"Cells Left: {Cell.cell_count}",
            width = 12,
            height = 4
        )

        Cell.cell_count_label_object = lbl

    def left_click_actions(self, event):

        if self.is_mine:
            self.show_mine()
        else:
            if self.surrounded_cells_mines_length == 0:
                for cell in self.surrounded_cells:
                    cell.show_cell()
            
            self.show_cell()

            if Cell.cell_count == st.MINES_COUNT:
                message = messagebox.showinfo(
                    title = "Congratulations",
                    message = "You're the winner!"
                )

                sys.exit()
                
        
        # нельзя нажать на кнопку повторно
        self.cell_btn_object.unbind('<Button-1>')
        self.cell_btn_object.unbind('<Button-3>')

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
        if not self.is_opend:
            Cell.cell_count -= 1
            self.cell_btn_object.configure(text = self.surrounded_cells_mines_length)

            # заменить кол-во оставшихся мин
            if Cell.cell_count_label_object:
                Cell.cell_count_label_object.configure(
                    text = f"Cells Left: {Cell.cell_count}"
                )
            
            self.cell_btn_object.configure(
                bg = "SystemButtonFace"
            )

        # открыта ли мина
        self.is_opend = True

    def show_mine(self):
        self.cell_btn_object.configure(bg = '#d53032')

        message = messagebox.showerror(
            title = "Game Over!",
            message = "You clicked on a mine!"
        )

        sys.exit()

    def right_click_actions(self, event):
        if not self.is_mine_candidate:
            self.cell_btn_object.configure(
                bg = '#fcdd76'
            )
            self.is_mine_candidate = True
        else:
            self.cell_btn_object.configure(
                bg = 'SystemButtonFace'
            )
            self.is_mine_candidate = False

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




    