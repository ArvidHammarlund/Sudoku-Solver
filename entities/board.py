
from entities.tiles import Tile, TileGroup


class Board(object):

    # --- Static attributes ---

    SIZE = 9

    # --- Constructor --- 

    def __init__(self):
        self.__rows = []
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
            tiles = [tile for tile in section.get_members() if tile.valid_assignment() and tile.get_digit == 0]
            if len(tiles) == 1:
                tiles[0].set_digit(digit)

    # --- Helpers ---

    def __build(self) -> None:
        self.__build_rows()
        self.__build_cols()
        self.__build_sections(Board.SIZE / 3)

    def __build_rows(self) -> None:
        self.__rows = [self.__build_row() for _ in range(Board.SIZE)]

    def __build_row(self) -> list[Tile]:
        return TileGroup([Tile() for _ in range(Board.SIZE)])

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
        return [row.get_members()[col*size:col+size] for row in self.__rows[row*size:row+size]] 

    # --- Setters & Getters ---

    def set_digit(self, row: int, col: int, digit: int) -> None:
        self.__rows[row].set_digit(col, digit)


