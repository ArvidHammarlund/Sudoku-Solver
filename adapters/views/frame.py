from tkinter import *
from tkinter.font import *
from tkmacosx import *


class Frame(TK):

    __FONT = Font(family='Helvetica', size=36, weight='bold')

    # --- Constructor ---

    def __init__(self):
        buttons = []
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
