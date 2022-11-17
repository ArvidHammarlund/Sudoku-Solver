#
# Author: Arvid Hammarlund
#

from entities.board import Board
from adapters.view import ViewCLI

class Main(object):
    def __init__(self):
        self.__board = Board()
        self.__view = ViewCLI()

    def run(self):
        self.__view.welcome_msg()
        while True:
            self.__view.current_board(self.__board.parse())
            self.__view.highlight_digit(self.__board.parse(),
                                        self.__board.highlight(7))
            row = int(input("row: ")) - 1
            col = int(input("col: ")) - 1
            digit = int(input("digit: ")) 
            self.__board.change_digit(row, col, digit)

if __name__ == "__main__":
    Main().run()

