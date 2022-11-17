import json

from abc import ABC, abstractmethod

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
                if mark:
                    tmp = "<" + tmp + ">|"
                else:
                    tmp = " " + tmp + " |"
                row += tmp
            res += row
            res += "\n   +---+---+---+---+---+---+---+---+---+\n"
        print(res)






