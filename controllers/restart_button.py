from tkinter import *
from tkinter.font import *
from tkmacosx import *

from model import Model

class RestartButton(Button):

    # --- Attributes ---

    __WIDTH = 100
    __HEIGHT = 50
    __TEXT = "Restart"

    # --- Constructor ---

    def __init__(self, model, root):
        super().__init__(root, text="Restart", height=RestartButton.__HEIGHT, width=RestartButton.__WIDTH, command=model.restart)
