#
# Description: Sudoku board componants.
# Author: Arvid Hammarlund
# Version: 0.0.1
#

from abc import ABC, abstractmethod

class Tile(object):
    """Unit of area displaying either 0-9, where 0 signifies empty."""
    def __init__(self, digit: int = 0) -> None:
        self.__digit = digit
        self.__subscriptions = []

    # --- SETTERS & GETTERS ---
    def get_digit(self) -> int:
        return self.__digit

    def change_digit(self, digit: int) -> None:
        if not self.__allows_new_digit(digit):
            raise Exception("Invalid input")
        self.__digit = digit

    def __allows_new_digit(self, digit: int):
        do_allow = False
        if digit > 0 and digit < 10:
            for grouping in self.__subscriptions:
                if grouping.contains_digit(digit):
                    break
            else:
                do_allow = True
        return do_allow
                 
    def add_subscription(self, grouping):
        self.__subscriptions.append(grouping)

    def get_subscriptions(self):
        return self.__subscriptions


class TileGrouping(ABC, object):
    """Collection of references to Tile objects."""
    def __init__(self, members: list[Tile]) -> None:
        self.__members = members

    # --- METHODS ---
    def subscribe_tiles(self):  
        for tile in self.__members:
            tile.add_subscription(self)

    def contains_digit(self, n: int) -> bool:
        """Checks whether grouping already contains n"""
        do_contain = False
        for tile in self.__members:
            if tile.get_digit() == n:
                do_contain = True
                break
        return do_contain

    # --- SETTERS & GETTERS ---
    def get_members(self) -> list[Tile]:
        return self.__members


class SudokuRow(TileGrouping):
    """Set of 9 tiles, horizontally adjacent."""
    def __init__(self, members: list[Tile]) -> None:
        super().__init__(members)
        self.subscribe_tiles()
    
    # ---- Methods ----
    def change_digit(self, col: int, digit: int):
        self.get_members()[col].change_digit(digit) 


class SudokuColumn(TileGrouping):
    """Set of 9 tiles, vertically adjecent."""
    def __init__(self, members: list[Tile]) -> None:
        super().__init__(members)
        self.subscribe_tiles()


class SudokuSection(TileGrouping):
    """3x3 matrix of tiles. Sections are mutually exclusive."""
    def __init__(self, members: list[Tile]) -> None:
        super().__init__(members)
        self.subscribe_tiles()


       



