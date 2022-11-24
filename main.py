#
# Author: Arvid Hammarlund
#

from entities.board import Board
from adapters.view import ViewCLI, ViewGUI
from adapters.controller import ControllerCLI

from tkinter import *
from tkinter.font import *
from tkmacosx import *

class SudokuCLI(object):
    def __init__(self):
        self.__board = Board()
        self.__view = ViewCLI()

    def run(self):
        self.__view.welcome_msg()
        while True:
            self.__view.current_board(self.__board.parse())
            n = ControllerCLI.query_digit()
            values = self.__board.parse()
            valid_assignments = self.__board.valid_assignments(n)
            self.__view.highlight_digit(values, valid_assignments)
            if ControllerCLI.do_solver():
                self.__board.solver()
                continue
            row, col = ControllerCLI.query_position()
            if valid_assignments[row][col]:
                self.__board.set_digit(row, col, n)

class SudokuGUI(object):
    def __init__(self):
        self.__root = Tk()
        self.__board = Board()
        self.__buttons = self.__build(self.__board.parse())
        self.__current_digit = 0
        mainloop()

    def command_click(self, n):
        self.__current_digit = n
        self.update(self.__board.parse(), self.__board.valid_assignments(n))

    def update(self, values, valids):
        for row, digits, marks in zip(self.__buttons, values, valids):
            for btn, digit, mark in zip(row, digits, marks):
                btn['text'] = digit if digit != 0 else ""
                btn['bg'] = "grey" if mark else "red"

    def onClick(self, row, col):
        if self.__board.valid_assignments(self.__current_digit)[row][col]:
            self.__board.set_digit(row, col, self.__current_digit)
        self.update(self.__board.parse(),
                    self.__board.valid_assignments(self.__current_digit))
            
    def __build(self, board):
        buttons = []
        font = Font(family='Helvetica', size=36, weight='bold')
        for i, row in enumerate(board):
            tmp = []
            for j, tile in enumerate(row):
                btn = Button(self.__root,
                             text="",
                             bg='grey',
                             font=font,
                             width = 50,
                             height = 50)
                btn["command"] = lambda i=i, j=j: self.onClick(i, j)
                tmp.append(btn)
                btn.grid(row=i, column=j)
            buttons.append(tmp)

        for i in range(1,10):
            btn = Button(self.__root,
                    text=i,
                    width=50,
                    height=50,
                    command= lambda i=i: self.command_click(i))
            btn.grid(row=10, column=i - 1) 
        Button(self.__root,
               text="Solver",
               height=50,
               width=50*9,
               command=self.solver_click).grid(row=11,
                                                 column=0,
                                                 columnspan=9)
        return buttons

    def solver_click(self):
        self.__board.solver()
        self.update(self.__board.parse(),
                    self.__board.valid_assignments(self.__current_digit))

if __name__ == "__main__":
    SudokuGUI()
