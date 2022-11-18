#
# Author: Arvid Hammarlund
#

from entities.board import Board
from adapters.view import ViewCLI
from interactors.solver import Solver

class Main(object):
    def __init__(self):
        self.__board = Board()
        self.__view = ViewCLI()
        self.__solver = Solver()

    def run(self):
        self.__view.welcome_msg()
        self.__view.current_board(self.__board.parse())
        while True:
            n = int(input("digit: or 0 for solver"))
            values = self.__board.parse()
            valid_assignments = self.__board.valid_assignments(n)
            print(valid_assignments)
            if n == 0:
                self.__solver.auto_assign(values)
                continue
            self.__view.highlight_digit(values, valid_assignments)
            row = int(input("row: ")) - 1
            col = int(input("col: ")) - 1
            if valid_assignments[row][col]:
                self.__board.set_digit(row, col, n)
            self.__view.current_board(self.__board.parse())


if __name__ == "__main__":
    Main().run()

