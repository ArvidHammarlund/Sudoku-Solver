from tkinter import *
from tkinter.font import *
from tkmacosx import *

from model import Model

class DigitButton(Button):

    # --- Attributes ---

    __WIDTH = 50
    __HEIGHT = 50

    # --- Constructor ---

    def __init__(self, model, root, digit):
        super().__init__(root, text=digit, width=DigitButton.__WIDTH, height=DigitButton.__HEIGHT, command= lambda i=digit: model.set_current_digit(i))

    

 
