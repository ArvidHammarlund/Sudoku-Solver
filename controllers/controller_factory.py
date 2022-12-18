from .tile_button import TileButton
from .digit_button import DigitButton
from .solver_button import SolverButton
from .restart_button import RestartButton
from .templates_menu import TemplatesMenu

class ControllerFactory(object):

    # --- Methods ---

    @staticmethod
    def make_digit_button(model, root, digit):
        return DigitButton(model, root, digit)

    @staticmethod
    def make_solver_button(model, root):
        return SolverButton(model, root)

    @staticmethod
    def make_restart_button(model, root):
        return RestartButton(model, root)

    @staticmethod
    def make_templates_menu(model, root, var):
        return TemplatesMenu(model, root, var)

    @staticmethod
    def make_tile_button(model, root, row, col):
        return TileButton(model, root, row, col)


