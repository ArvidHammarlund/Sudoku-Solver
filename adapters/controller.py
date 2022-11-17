#
# Decription: User input interface
# Author: Arvid Hammarlund
# Version: 0.0.1
#

from abc import ABC, abstractmethod

class Controller(ABC):
    @abstractmethod 
    def query_action(self) -> str:
        pass

    @abstractmethod
    def query_digit(self) -> int:
        pass

    @abstractmethod
    def query_tile(self) -> str:
        pass

class ControllerCLI(Controller):
    def query_action(self):
        inp = input("""
    Please enter which action to proceede with:
        
        * (S)olver let the computer assign a valid tile.

        * (H)ighlight illuminates the invalid spots for a given digit
                to help you with the principle of exclusion

        * (A)ssign a tile a new digit.

""")
        return inp
    
    def query_digit(self):
        inp = input("Enter digit 1-9 >> ")
        return int(inp)

    def query_tile(self):
        return input("Please a tiles corresponding row and col >>")



