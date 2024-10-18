"""Inventory class"""
from src.game_handler.items import Item


class Inventory:
    """The player's inventory"""
    width: int
    height: int

    def __init__(self, *, width: int = 4, height: int = 4):
        self.width = width
        self.height = height
        self.inventory: list[Item | None] = [None for _ in range(width * height)]

    def __validate_column(self, column: int):
        """Validate the column index if it is within the inventory's width"""
        if column < 0 or column >= self.width:
            raise ValueError("Column out of range")

    def __validate_row(self, row: int):
        """Validate the row index if it is within the inventory's height"""
        if row < 0 or row >= self.height:
            raise ValueError("Row out of range")

    def __validate_index(self, row: int, column: int):
        """Validate the row and column index if it is within the inventory's width and height"""
        self.__validate_column(column)
        self.__validate_row(row)

    def append(self, item: Item):
        """Add an item to the inventory"""
        try:
            index = next(i for i, stored in enumerate(self.inventory) if stored is None)
            self.inventory[index] = item
        except StopIteration:
            raise ValueError("Inventory is full")

    def insert_item(self, item: Item, row: int, column: int):
        """Add an item to the inventory"""
        self.__validate_index(row, column)
        self.inventory[(row * self.width) + column] = item

    def get_item(self, row: int, column: int) -> Item | None:
        """Get an item from the inventory"""
        self.__validate_index(row, column)
        return self.inventory[(row * self.width) + column]

    def is_empty(self, row: int, column: int) -> bool:
        """Check if a slot is empty"""
        self.__validate_index(row, column)
        return self.inventory[(row * self.width) + column] is None

    def get_column(self, column: int) -> list[Item | None]:
        """Get a column from the inventory"""
        return [self.get_item(row, column) for row in range(self.height)]

    def get_row(self, row: int) -> list[Item | None]:
        """Get a row from the inventory"""
        return [self.get_item(row, column) for column in range(self.width)]

    def __str__(self):
        return "\n".join(" | ".join(
            str(self.get_item(row, col)).ljust(max(len(str(item)) for item in self.get_column(col))) for col in
            range(self.width)) for row in range(self.height))

    def __repr__(self):
        return str(self)
