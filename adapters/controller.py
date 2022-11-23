#
# Decription: User input interface
# Author: Arvid Hammarlund
# Version: 0.0.1
#

from abc import ABC, abstractmethod

class Controller(ABC):
    @abstractmethod 
    def do_solver(self) -> str:
        pass

    @abstractmethod
    def query_digit(self) -> int:
        pass

    @abstractmethod
    def query_position(self) -> tuple():
        pass

class ControllerCLI(Controller):
    @staticmethod
    def query_digit():
        while True:
            try: 
                inp = int(input("Enter digit 1-9 >> "))
            except Exception:
                print("invalid!")
            else:
                if inp > 0 and inp < 10:
                    return inp
            
    
    @staticmethod
    def query_position():
        print("Row number")
        row = ControllerCLI.query_digit()
        print("Column number")
        col = ControllerCLI.query_digit()
        return row - 1, col - 1

    @staticmethod
    def do_solver():
        inp = input("Sovler?")
        return bool(inp)


