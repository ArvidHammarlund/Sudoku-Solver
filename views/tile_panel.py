from tkinter import *
from tkinter.font import *
from tkmacosx import *

from controllers import ControllerFactory

class TilePanel(Frame):
    
    # --- Attributes ---

    __SIZE = 9

    # --- Constructor ---

    def __init__(self, root, model):
        super().__init__(root)
        for i in range(TilePanel.__SIZE):
            for j in range(TilePanel.__SIZE):
                ControllerFactory.make_tile_button(model, self, i,j).grid(row=i, column=j)

