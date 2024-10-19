"""Inventory class"""
from typing import overload
from src.game_handler.items import Item
from src.game_handler.inventory.stack import Stack
from copy import copy


class Inventory:
    """The player's inventory"""
    __inventory: list[Stack]
    width: int
    height: int

    @property
    def size(self) -> int:
        """The size of the inventory"""
        return self.width * self.height

    def __init__(self, width: int = 4, height: int = 4):
        self.width = width
        self.height = height
        self.__inventory = [Stack() for _ in range(width * height)]
        assert len(self.__inventory) == self.size

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

    def append(self, item: Stack | Item):
        """Add a stack or item to the inventory"""
        try:
            index = next(
                i for i, stored in enumerate(self.__inventory) if
                isinstance(stored.item, item.__class__) or
                stored.is_empty())
            self.__inventory[index].add(item)
        except StopIteration:
            raise ValueError("Inventory is full")

    def insert_item(self, item: Stack | Item, row: int, column: int):
        """Add a stack or item to the inventory"""
        self.__validate_index(row, column)
        self.__inventory[(row * self.width) + column].add(item)

    def get_item(self, row: int, column: int) -> Stack:
        """Get an item from the inventory"""
        self.__validate_index(row, column)
        return self.__inventory[(row * self.width) + column]

    def remove_item(self, row: int, column: int) -> Stack:
        """Remove an item from the inventory and return a copy of the stack"""
        self.__validate_index(row, column)
        stack = copy(self.get_item(row, column))
        self.get_item(row, column).reset()
        return stack

    def split_item(self, row: int, column: int, quantity: int = -1) -> Stack:
        """Split an item from the inventory"""
        self.__validate_index(row, column)
        return self.get_item(row, column).split(quantity)

    def is_empty(self, row: int, column: int) -> bool:
        """Check if a slot is empty"""
        self.__validate_index(row, column)
        return self.__inventory[(row * self.width) + column].is_empty()

    def get_column(self, column: int) -> list[Stack]:
        """Get a column from the inventory"""
        return [self.get_item(row, column) for row in range(self.height)]

    def get_row(self, row: int) -> list[Stack]:
        """Get a row from the inventory"""
        return [self.get_item(row, column) for column in range(self.width)]

    def __str__(self):
        return "\n".join(" | ".join(
            str(self.get_item(row, col)).ljust(max(len(str(item)) for item in self.get_column(col))) for col in
            range(self.width)) for row in range(self.height))

    def __repr__(self):
        return str(self)
