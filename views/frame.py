from tkinter import *
from tkinter.font import *
from tkmacosx import *

from .tile_panel import TilePanel 
from .digit_panel import DigitPanel
from .command_panel import CommandPanel

class Frame(Tk):

    # --- Constructor ---

    def __init__(self, model): 
        super().__init__()
        TilePanel(self, model).pack()
        DigitPanel(self, model).pack()
        CommandPanel(self, model).pack()

    # --- Methods ---

    def run(self):
        mainloop()
