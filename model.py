from entities import Board

from random import shuffle


class Model(object):
    
    # --- Constructor ---

    def __init__(self) -> None:
        self.__board = Board()
        self.__observers = []
        self.__current_digit = 0

    # --- Method ---

    def solver(self):
        digits = [i for i in range(1,10)]
        shuffle(digits)
        for digit in digits:
            self.__board.assign_valids(digit)
        self.__signal()

    def parse(self):
        return self.__board.parse()

    def template(self, template):
        self.__board = Board(template)
        self.__current_digit = 0
        self.__signal()

    def valid_assignments(self):
        return self.__board.valid_assignments(self.__current_digit)

    def __signal(self):
        for observer in self.__observers:
            observer.update()

    def restart(self):
        self.__board = Board()
        self.__signal()

    # --- Helper ---

    # --- Setters & Getters ---

    def add_observer(self, observer):
        self.__observers.append(observer)

    def set_digit(self, row: int, col: int) -> None:
        self.__board.set_digit(row, col, self.__current_digit)
        self.__signal()
    
    def set_current_digit(self, digit):
        self.__current_digit = digit
        self.__signal()




