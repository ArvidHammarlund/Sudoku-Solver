
from .tiles import Tile, TileGroup, TileSection


class Board(object):

    # --- Static attributes ---

    SIZE = 9

    # --- Constructor --- 

    def __init__(self, template=[]):
        self.__rows = template
        self.__cols = []
        self.__sections = []
        self.__build()

    # --- Methods ---

    def parse(self) -> list[list[int]]: 
        return [row.parse() for row in self.__rows]

    def valid_assignments(self, digit) -> list[list[bool]]:
        return [row.valid_assignments(digit) for row in self.__rows]
    
    def assign_valids(self, digit):
        for section in self.__sections:
            section.assign_valids(digit)

    # --- Helpers ---

    def __build(self) -> None:
        self.__build_rows()
        self.__build_cols()
        self.__build_sections(Board.SIZE / 3)

    def __build_rows(self) -> None:
        self.__rows = [self.__build_row(i) for i in range(Board.SIZE)]

    def __build_row(self, idx) -> list[Tile]:
        return TileGroup([Tile(self.__rows[idx][j] if self.__rows else 0) for j in range(Board.SIZE)])

    def __build_cols(self) -> None:
        self.__cols = [self.__build_col(i) for i in range(Board.SIZE)]

    def __build_col(self, idx) -> list[Tile]:
        return TileGroup([row.get_members()[idx] for row in self.__rows])

    def __build_sections(self, size: int) -> None:
        """
        @param size: absolute height & width of constellation.
        """
        self.__sections = [self.__build_section(int(size), int(i / size), int(i % size)) for i in range(Board.SIZE)]

    def __build_section(self, size: int, row: int, col: int):
        """
        @param size: absolute height & width of constellation.
        @param row: the n consequent constellation in y axis.
        @param col: the n consequent constellation in x axis.
        """
        start_row = row * size
        end_row = start_row + size
        start_col = col * size
        end_col = start_col + size
        return TileSection([tile for row in self.__rows[start_row:end_row] 
                               for tile in row.get_members()[start_col:end_col]])

    # --- Setters & Getters ---

    def set_digit(self, row: int, col: int, digit: int) -> None:
        try:
            self.__rows[row].set_digit(col, digit)
        except ValueError as e:
            print(e)

