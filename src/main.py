# line 2 to use tkinter for the ui 
# and line 3-5 just to connect to other python file
# cell.py is for the functions and class
# settings.py is for height width variable
# func is for the functions as well but only for width height percentage function
from tkinter import *
import settings
import func
import cell

# make the root or the base for the window
root = Tk()
root.configure(bg="black") #bg = background

#set width x height for window size
root.geometry(f"{settings.width}x{settings.height}")
root.title("Minesweeper Game")

# to disable fullscreen or to disable resize window
root.resizable(False, False) 

# top frame is for the frame at the top
top_frame = Frame(
    root,
    bg = 'blue',
    width = settings.width,
    height = func.height_percentage(settings.percent1),
)

# left is for the frame at the left. the location is below the top_frame
left_frame = Frame(
    root,
    bg = 'white',
    width = func.width_percentage(settings.percent1),
    height = settings.height - func.height_percentage(settings.percent1),
)

# the center_frame is on the center.
# below the top_frame, and on the right side of left_frame
center_frame = Frame(
    root,
    bg = 'green',
    width = settings.width - func.width_percentage(settings.percent1),
    height = settings.height - func.height_percentage(settings.percent1),
)

# the starting location for the frames
left_frame.place(x = 0, y = func.height_percentage(settings.percent1))
top_frame.place(x = 0, y = 0)
center_frame.place(x = func.width_percentage(settings.percent1), y = func.height_percentage(settings.percent1))

# to make the buttons for the minesweeper game
for i in range(settings.row1):
    for t in range(settings.column1):
        c1 = cell.Cell(row = i, column = t)
        c1.create_btn_obj(center_frame)
        c1.cell_btn_obj.grid(row = i, column = t)

# to make the label for "Count Left: bla bla bla"
cell.Cell.create_cell_count_label(left_frame)
cell.Cell.cell_count_obj.place(x = 0, y = 0)

# create a title for the minesweeper word
game_title = Label(
    top_frame,
    bg = 'black',
    fg = 'white',
    text = 'Minesweeper Game',
    font = ('', 48)
)

# place the game_title to the UI
game_title.place(x = func.width_percentage(15), y = func.height_percentage(3))

# to make how many bombs label so player can know how many the bombs for the game
bomb_many = Label(
    left_frame,
    bg = 'black',
    fg = 'white',
    text = f'{settings.bombs} Bombs',
    font = ('', 18)
)

# to place how many bombs to the UI on the left side
bomb_many.place(x = 0, y = 100)

# to choose random box / button to be the bombs
cell.Cell.randomize_mines()
#print(cell.Cell.all)

# do not delete this
root.mainloop()