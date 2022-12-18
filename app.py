from model import Model
from views import Frame

class SudokuGUI(object):
    def __init__(self):
        self.__model = Model()
        self.__frame = Frame(self.__model)
        self.__frame.run()

class SudokuCLI(object):
    def __init__(self):
        self.__board = Board()
        self.__view = ViewCLI()

    def run(self):
        self.__view.welcome_msg()
        while True:
            self.__view.current_board(self.__board.parse())
            n = ControllerCLI.query_digit()
            values = self.__board.parse()
            valid_assignments = self.__board.valid_assignments(n)
            self.__view.highlight_digit(values, valid_assignments)
            if ControllerCLI.do_solver():
                self.__board.solver()
                continue
            row, col = ControllerCLI.query_position()
            if valid_assignments[row][col]:
                self.__board.set_digit(row, col, n)

if __name__ == "__main__":
    SudokuGUI()
