#
# Description: Sudoku game board object.
# Author: Arvid Hammarlund
# Version: 0.0.1
#

from entities.tiles import TileGroup, Tile
from math import floor
from random import shuffle

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

    def solver(self):
        digits = [n for n in range(1,10)]
        shuffle(digits)
        for digit in digits:
            for section in self.__sections:
                valid_assignments = []
                for tile in section.get_members():
                    if (tile.valid_assignment(digit)
                            and tile.get_digit() == 0):
                        valid_assignments.append(tile)
                if len(valid_assignments) == 1:
                    valid_assignments[0].set_digit(digit)

    def set_digit(self, row: int, col: int, digit: int):
        self.__rows[row].set_digit(col, digit)

    # --- Helpers ---
    def __build(self) -> None:
        """Generate sudoko board of tiles"""
        self.__build_rows()
        self.__build_cols()
        self.__build_sections()

    def __build_rows(self):
        self.__rows = [self.__build_row() for _ in range(Board.SIZE)]

    def __build_row(self):
        res = []
        for _ in range(Board.SIZE):
            res.append(Tile())
        res = TileGroup(res)
        return res
    
    def __build_cols(self):
        self.__cols = [self.__build_col(i) for i in range(Board.SIZE)]

    def __build_col(self, idx):
        res = []
        for row in self.__rows:
            res.append(row.get_members()[idx])
        res = TileGroup(res)
        return res

    def __build_sections(self):
        self.__sections = [self.__build_section(i) for i in
                           range(Board.SIZE)]

    def __build_section(self, idx):
        SIZE = 3 # A sudoku board has 3x3 sections
        rows = self.__rows
        res = []
        for i in range(SIZE): 
            for j in range(SIZE):
                row = floor(idx / SIZE)*SIZE + i
                col = (j % SIZE) + SIZE*(idx % SIZE)
                res.append(rows[row].get_members()[col])
        res = TileGroup(res)
        return res


