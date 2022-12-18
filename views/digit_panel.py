from tkinter import *
from tkinter.font import *
from tkmacosx import *

from controllers import ControllerFactory

class DigitPanel(Frame):
    
    # --- Constructor ---

    def __init__(self, root, model):
        super().__init__(root)
        for i in range(1,10):
            ControllerFactory.make_digit_button(model, self, i).grid(row=0, column=i - 1)

