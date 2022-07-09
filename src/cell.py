# just imports the details can be found in main.py comment top line
from tkinter import Button
import random
import tkinter
import settings

# ctypes import to use the message box when click on bomb
# sys is for sys.exit() when the message box appears
import ctypes
import sys

class Cell():
    # all variable is an array to put the x,y coordinate of all the minesweeper boxes or buttons
    all = []

    # the variable to store starting number for the label "Cells Left: bla bla bla"
    cell_count_left = settings.row1 * settings.column1

    # a variable to store created button
    # this variable is going to be called in create_btn_obj
    cell_count_obj = None

    # to make boolean for is it a bomb or not
    # to know whether the box has been clicked or not
    # when generating the boxes, save the x y coordinate to all array
    # and etc
    def __init__(self, row, column, is_mine = False):
        self.is_mine = is_mine
        self.cell_btn_obj = None
        self.is_clicked = False
        self.is_red = False
        self.is_right_clicked = False
        self.row = row
        self.column = column
        Cell.all.append(self)

    # make a function to make the boxes for the minesweeper
    # to give attributes to the boxes like
    # enable right click and left click
    # this function is called in the main.py to generate the boxes as well
    def create_btn_obj(self, location):
        btn = Button(
            location,
            # text = f"{self.row}, {self.column}",
            width = 6, height = 3,
        )
        btn.bind ('<Button-1>', self.left_click_actions)
        btn.bind ('<Button-3>', self.right_click_actions)
        self.cell_btn_obj = btn
    
    # the code for what happens when left click for the minesweeper boxes
    def left_click_actions(self, event):
        if self.is_mine:
            self.show_mine()
        else:
            if self.count_surrounded_cell_length == 0:
                for k in self.count_surrounded_cell:
                    k.show_cell()
            self.show_cell()
        if Cell.cell_count_left == settings.bombs:
            ctypes.windll.user32.MessageBoxW(
                0, 'You win', 'Congratulations!', 0
            )
            sys.exit()
        
    
    # this show_mine is to change the box become red color
    # if the box is a bomb when left-click at the box
    # and also to display message box and close the game
    def show_mine(self):
        self.cell_btn_obj.configure(bg = "red")
        ctypes.windll.user32.MessageBoxW(0, 'You clicked on a mine', 'Game Over', 0)
        sys.exit()

    # to get a specific x,y coordinate for box
    # it is needed to get the coordinate when clicking a box
    def get_cell_by_axis(self, x, y):
        for cell in Cell.all:
            if cell.row == x and cell.column == y:
                return cell
    
    # to return the coordinate nearby box, example
    # when click box 0,0 there is 3 nearby box, 0,1; 1,1; and 1,0;
    # so this function will return the coordinate, 0,1; 1,1; and 1,0; if 0,0 is clicked
    # if it is for example 1,1 will return 9 coordinate box 
    @property
    def count_surrounded_cell(self):
        surrounded_cells = []
        for k in range(-1, 2, 1):
            for u in range(-1, 2, 1):
                asd = self.get_cell_by_axis(self.row + k, self.column + u)
                if asd is not None: surrounded_cells.append(asd)
        return surrounded_cells

    # to count the surrounded bombs
    # for example if there is 2 bombs nearby, this function will return 2
    @property
    def count_surrounded_cell_length(self):
        counter = 0
        for k in self.count_surrounded_cell:
            if k.is_mine:
                counter = counter + 1
        return counter

    # this function to check whether a box has been clicked or not.
    # if not will give open the box and reveal the box
    def show_cell(self):
        if self.is_clicked == False and self.is_red == False and self.is_right_clicked == False:
            Cell.cell_count_left -= 1
            # print(self.count_surrounded_cell)
            # print(self.count_surrounded_cell_length)
            self.cell_btn_obj.configure(bg = "green")
            self.cell_btn_obj.configure(text = self.count_surrounded_cell_length)
            if Cell.cell_count_obj:
                Cell.cell_count_obj.configure(
                    text = f"Cells Left: {Cell.cell_count_left}"
                )
            self.is_clicked = True
            self.cell_btn_obj.unbind('<Button-1>')
            self.cell_btn_obj.unbind('<Button-3>')

    # the enable right click on the minesweeper boxes
    def right_click_actions(self, event):
        if self.is_red == False and self.is_clicked == False and self.is_right_clicked == False:
            self.is_red = True
            self.cell_btn_obj.configure(bg = "orange")
            self.is_right_clicked = True
        elif self.is_red == True and self.is_clicked == False and self.is_right_clicked == True:
            self.is_red = False
            self.is_right_clicked = False
            self.cell_btn_obj.configure(bg = "SystemButtonFace")

    # function to choose random boxes as the bombs
    @staticmethod
    def randomize_mines():
        picked_cell = random.sample(
            # settings.bombs is to set the number of bomb
            # when the number is 7 it means there will be 7 bombs
            Cell.all, settings.bombs 
        )
        for k in picked_cell:
            k.is_mine = True

    # not sure what is this
    def __repr__(self):
        return f"Cell({self.row}, {self.column})"

    # the function to make the label for "Cells Left: bla bla bla"
    # the parameter can be adjusted
    @staticmethod
    def create_cell_count_label(location):
        lbl = tkinter.Label(
            location,
            bg = "black",
            fg = "white",
            text = f"Cells Left: {settings.row1 * settings.column1}",
            font = ("", 18),
        )
        Cell.cell_count_obj = lbl