#
# Description: Sudoku board componants.
# Author: Arvid Hammarlund
# Version: 0.0.1
#

from abc import ABC, abstractmethod
from math import floor

class Tile(object):
    """Unit of area displaying either 0-9, where 0 signifies empty."""
    def __init__(self, digit: int = 0) -> None:
        self.__digit = digit
        self.__subscriptions: list[TileGroup] = []
    
    # --- METHODS ---

    def valid_assignment(self, digit: int):
        return not any([x.contains(digit) for x in self.__subscriptions])     

    def add_subscription(self, grouping):
        self.__subscriptions.append(grouping)

    # --- SETTERS & GETTERS ---

    def get_digit(self) -> int:
        return self.__digit

    def set_digit(self, digit: int) -> None:
        self.__digit = digit


class TileGroup(ABC, object):
    """Collection of references to Tile objects."""
    def __init__(self, members: list[Tile]) -> None:
        self.__members = members
        self.__subscribe_members()

    # --- METHODS ---
   
    def valid_assignments(self, digit):
        return [member.valid_assignment(digit) for member in self.__members]

    def parse(self):
        return [member.get_digit() for member in self.__members]

    def contains(self, digit: int) -> bool:
        """Checks whether grouping already contains n"""
        return digit in self.parse()

    # --- HELPERS ---
    
    def __subscribe_members(self):  
        for tile in self.__members:
            tile.add_subscription(self)

    # --- SETTERS & GETTERS ---

    def set_digit(self, idx: int, digit: int):
        self.__members[idx].set_digit(digit)

    def ref(self):
        return self

    def get_members(self):
        return self.__members


class Row(TileGroup, object):
    def __init__(self, size: int):
        super().__init__(Row.__build(size))
    
    @staticmethod
    def __build(size):
        res = []
        for _ in range(size):
            res.append(Tile())
        return res
         

class Column(TileGroup):
    def __init__(self, rows: list[Row], idx: int):
        super().__init__(Column.__build(rows, idx))
    
    @staticmethod
    def __build(rows: list[Row], idx: int):
        res = []
        for row in rows:
            res.append(row.get_members()[idx])
        return res


class Section(TileGroup):
    def __init__(self, rows: list[Row], idx: int):
        super().__init__(Section.__build(rows, idx))

    @staticmethod
    def __build(rows, idx):
        res = []
        for i in range(3):
            for j in range(3):
                row = floor(idx / 3)*3 + i
                col = (j % 3)+3*(idx % 3)
                res.append(rows[row].get_members()[col])
        return res

