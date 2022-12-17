from entities.board import Board

from random import shuffle


class Model(object):
    
    # --- Constructor ---

    def __init__(self) -> None:
        self.__board = Board()

    # --- Method ---

    def solver(self):
        for digit in shuffle(range(1,10)):
            self.__board.assign_valids(digit)

    def parse(self):
        return self.__board.parse()

    def valid_assignments(self, digit):
        return self.__board.valid_assignment(digit)

    # --- Helper ---




