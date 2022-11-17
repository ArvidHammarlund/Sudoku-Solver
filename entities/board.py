#
# Description: Sudoku game board object.
# Author: Arvid Hammarlund
# Version: 0.0.1
#

import json
from entities.tiles import Tile, SudokuRow, SudokuColumn, SudokuSection

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
            tmp = []
            for tile in row.get_members():
                tmp.append(tile.get_digit())
            res.append(tmp)
        return res

    def highlight(self, digit):
        res = []
        for row in self.__rows:
            tmp = []
            for tile in row.get_members():
                ans = any([x.contains_digit(digit) for x in
                           tile.get_subscriptions()])
                tmp.append(ans)
            res.append(tmp)
        return res
    
    def change_digit(self, row, col, digit):
        self.__rows[row].change_digit(col, digit)

    # --- Helpers ---
    def __build(self) -> None:
        """Generate sudoko board of tiles"""
        self.__build_rows()
        self.__build_cols()
        self.__build_sections()

    def __build_sections(self):
        s1 = []
        s2 = []
        s3 = []
        tmp = [s1, s2, s3]
        for i in range(Board.SIZE):
            flag = 0
            for j in range(Board.SIZE):
                tile = self.__rows[i].get_members()[j]
                tmp[flag].append(tile)
                if (j + 1) % 3 == 0:
                    flag += 1
                    
            if (i + 1) % 3 == 0:
                for i in range(3):
                    section = SudokuSection(tmp[i])
                    self.__sections.append(section)
                    tmp[i] = []
                
    def __build_cols(self):
        for i in range(Board.SIZE):
            col = []
            for row in self.__rows:
                col.append(row.get_members()[i])
            self.__cols.append(SudokuColumn(col))

    def __build_rows(self):
        for _ in range(Board.SIZE):
            row = []
            for _ in range(Board.SIZE):
                row.append(Tile())
            self.__rows.append(SudokuRow(row))
 




