from tkinter import *
from tkinter.font import *
from tkmacosx import *

from controllers import ControllerFactory

class CommandPanel(Frame):
    
    # --- Constructor ---

    def __init__(self, root, model):
        super().__init__(root)
        ControllerFactory.make_solver_button(model, self).pack(side=LEFT)
        ControllerFactory.make_restart_button(model, self).pack(side=LEFT)
        ControllerFactory.make_templates_menu(model, self, StringVar(self)).pack(side=LEFT)
