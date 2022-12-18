from tkinter import *
from tkinter.font import *
from tkmacosx import *

from model import Model

class SolverButton(Button):

    # --- Attributes ---

    __WIDTH = 250
    __HEIGHT = 50
    __TEXT = "Solver"

    # --- Constructor ---

    def __init__(self, model, root):
        super().__init__(root, text="Solver", height=SolverButton.__HEIGHT, width=SolverButton.__WIDTH, command=model.solver)
