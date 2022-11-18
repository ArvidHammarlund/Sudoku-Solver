from abc import ABC, abstractmethod
import random
from enum import Enum
from math import floor

class Solver(object):
    def auto_assign(self, board):
        digits = [n for n in range(1,10)]
        random.shuffle(digits)
        for digit in digits:
            for section in self.__sections:
                allowed_placements = []
                for tile in section.get_members():
                    if tile.valid_assignment:
                        allowed_placements.append(tile)
                return len(allowed_placements) == 1                       
                        

                    
    
