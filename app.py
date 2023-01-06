from model import Model
from views import Frame

class SudokuGUI(object):
    def __init__(self):
        self.__model = Model()
        self.__frame = Frame(self.__model)
        self.__frame.run()

if __name__ == "__main__":
    SudokuGUI()
