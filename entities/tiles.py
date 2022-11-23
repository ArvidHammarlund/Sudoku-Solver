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
                    #or self.__digit != 0)

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

    def get_members(self):
        return self.__members

