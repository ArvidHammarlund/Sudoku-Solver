from tkinter import *
from tkinter.font import *
from tkmacosx import *

from model import Model
from observer import Observer

class TileButton(Button, Observer):

    # --- Attributes ---

    __WIDTH = 50
    __HEIGHT = 50

    # --- Constructor ---

    def __init__(self, model, root, row, col):
        super().__init__(root, text="", bg='grey', width = TileButton.__WIDTH, height = TileButton.__HEIGHT)
        self["command"] = lambda i=row, j=col: model.set_digit(i, j)
        model.add_observer(self)
        self.__row = row
        self.__col = col
        self.__model = model 
        helv36 = Font(family='Helvetica', size=36, weight='bold')
        self["font"] = helv36

    # --- Methods ---

    def update(self):
        digit = self.__model.parse()[self.__row][self.__col]
        mark = self.__model.valid_assignments()[self.__row][self.__col]
        self['text'] = digit if digit != 0 else ""
        self['bg'] = "grey" if mark else "red"

