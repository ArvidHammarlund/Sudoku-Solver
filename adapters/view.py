import json

from abc import ABC, abstractmethod
from tkinter import *
from tkmacosx import * 

class View(ABC):
    @abstractmethod
    def welcome_msg(self):
        pass

    @abstractmethod
    def win_msg(self):
        pass

    @abstractmethod
    def current_board(self, board):
        pass


class ViewGUI(object):
    def __init__(self, board):
        self.__root = Tk()
        self.__board = board
        self.__buttons = self.__build(board)
        self.__current_digit = 0
        mainloop()

    def welcome_msg(self):
        pass

    def win_msg(self):
        pass

    def __build(self, board):
        buttons = []
        for i, row in enumerate(board):
            for j, tile in enumerate(row):
                btn = Button(self.__root,
                             text=tile,
                             bg='grey',
                             width = 50,
                             height = 50)
                btn["command"] = lambda btn=btn: self.onClick(btn)
                buttons.append(btn)
                btn.grid(row=i, column=j)

        for i in range(1,10):
            btn = Button(self.__root,
                    text=i,
                    width=50,
                    height=50,
                    command= lambda i=i: self.command_click(i))
            btn.grid(row=11, column=i - 1) 
        return buttons

    def command_click(self, n):
        self.__current_digit = n
        self.update(self.__board.parse(), self.__board.valid_assignments(n))

    def update(self, values, valids):
        for row, digits, marks in zip(self.__buttons, values, valids):
            for btn, digit, mark in zip(row, digits, marks):
                btn['text'] = digit
                btn['bg'] = 'red'

    def onClick(self, btn):
        btn["text"] = self.__current_digit
        btn["bg"] = "red"

            

class ViewCLI(View):
    def welcome_msg(self):
        print("""
    Welcome to the sudoku game! CLI controller and view""")

    def win_msg(self):
        pass

    def current_board(self, board):
        res = f"""
     1   2   3   4   5   6   7   8   9
   +---+---+---+---+---+---+---+---+---+\n"""
        for i in range(len(board)):
            res += f" {i + 1} |"
            tmp = ""
            for j in range(len(board)):
                if board[i][j] == 0:
                    tmp += f"   |"
                else:
                    tmp += f" {str(board[i][j])} |"
            res += tmp
            res += "\n   +---+---+---+---+---+---+---+---+---+\n"
        print(res)

    def highlight_digit(self, board, highlight):
        res = f"""
     1   2   3   4   5   6   7   8   9
   +---+---+---+---+---+---+---+---+---+\n"""
        for i in range(len(board)):
            res += f" {i + 1} |"
            row = ""
            for digit, mark in zip(board[i], highlight[i]):
                tmp = " " if digit == 0 else str(digit)
                if not mark:
                    tmp = "<" + tmp + ">|"
                else:
                    tmp = " " + tmp + " |"
                row += tmp
            res += row
            res += "\n   +---+---+---+---+---+---+---+---+---+\n"
        print(res)







