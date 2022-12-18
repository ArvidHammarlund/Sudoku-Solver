from tkinter import *
from tkinter.font import *
from tkmacosx import *

from model import Model
from utils import templates

class TemplatesMenu(OptionMenu):

    # --- Attributes ---

    __WIDTH = 100
    __HEIGHT = 50
    __TEXT = "Templates"

    # --- Constructor ---

    def __init__(self, model, root, var):
        super().__init__(
                root, 
                var,
                *templates.keys(),
                command=lambda var=var: model.template(templates[var])) 
