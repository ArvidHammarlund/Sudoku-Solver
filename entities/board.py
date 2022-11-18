#
# Description: Sudoku game board object.
# Author: Arvid Hammarlund
# Version: 0.0.1
#

from entities.tiles import Row, Column, Section

class Board(object):
    """Complete set of sudoku game components"""
    SIZE = 9
    def __init__(self):
        self.__rows = []
        self.__cols = []
        self.__sections = []
        self.__build()

    # --- Methods ---

    def parse(self):
        res = []
        for row in self.__rows:
            res.append(row.parse())
        return res

    def valid_assignments(self, digit):
        res = []
        for row in self.__rows:
            res.append(row.valid_assignments(digit))
        return res

    def set_digit(self, row: int, col: int, digit: int):
        self.__rows[row].set_digit(col, digit)

    # --- Helpers ---
    def __build(self) -> None:
        """Generate sudoko board of tiles"""
        self.__build_rows()
        self.__build_cols()
        self.__build_sections()

    def __build_rows(self):
        self.__rows = [Row(Board.SIZE).ref() for _ in range(Board.SIZE)]
    
    def __build_cols(self):
        rows = self.__rows
        self.__cols = [Column(rows, i) for i in range(len(rows))]

    def __build_sections(self):
        rows = self.__rows
        self.__sections = [Section(rows, i) for i in range(len(rows))]

                



 

