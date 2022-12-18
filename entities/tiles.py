

class Tile(object):

    # --- Constructor --- 

    def __init__(self, digit: int = 0) -> None:
        self.__digit = digit
        self.__subscriptions: list[TileGroup] = []
    
    # --- METHODS ---

    def valid_assignment(self, digit: int) -> bool:
        return not any([x.contains(digit) for x in self.__subscriptions])

    def add_subscription(self, grouping) -> None:
        self.__subscriptions.append(grouping)

    # --- SETTERS & GETTERS ---

    def get_digit(self) -> int:
        return self.__digit

    def set_digit(self, digit: int) -> None:
        if (not self.valid_assignment(digit)):
            raise ValueError("Exisiting digit does not allow placement!")
        self.__digit = digit


class TileGroup(object):
    
    # --- Constructor ---

    def __init__(self, members: list[Tile]) -> None:
        self.__members = members
        self.__subscribe_members()

    # --- METHODS ---
   
    def valid_assignments(self, digit) -> list[bool]:
        return [member.valid_assignment(digit) for member in self.__members]

    def parse(self) -> list[int]:
        return [member.get_digit() for member in self.__members]

    def contains(self, digit: int) -> bool:
        return digit in self.parse() if digit !=0 else False

    # --- HELPERS ---
    
    def __subscribe_members(self) -> None:  
        for tile in self.__members:
            tile.add_subscription(self)

    # --- SETTERS & GETTERS ---

    def set_digit(self, idx: int, digit: int) -> None:
        self.__members[idx].set_digit(digit)

    def get_members(self):
        return self.__members


class TileSection(TileGroup):

    # --- Methods ---

    def assign_valids(self, digit: int) -> None:
        valid_tiles = [tile for tile in super().get_members() if tile.valid_assignment(digit) and tile.get_digit() == 0]
        if len(valid_tiles) == 1:
            valid_tiles[0].set_digit(digit)

