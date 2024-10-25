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
        self.get_item(*self.find(item) if self.contains(item) else self.first_empty()).add(item)

    def insert_item(self, item: Stack | Item, row: int, column: int):
        """Add a stack or item to the inventory"""
        self.__validate_index(row, column)
        self.get_item(row, column).add(item)

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

    @overload
    def is_empty(self) -> bool:
        ...

    @overload
    def is_empty(self, row: int, column: int) -> bool:
        ...

    def is_empty(self, row: int | None = None, column: int | None = None) -> bool:
        """Check if a slot is empty"""
        if row is None and column is None:
            return all(stack.is_empty() for stack in self.__inventory)

        self.__validate_index(row, column)
        return self.get_item(row, column).is_empty()

    @overload
    def contains(self, item: Item, quantity: int = 1) -> bool:
        ...

    @overload
    def contains(self, item: Stack) -> bool:
        ...

    def contains(self, item: Stack | Item, quantity: int = 1) -> bool:
        """Check if the inventory contains an item"""
        if isinstance(item, Item):
            item = Stack(item, 1)
        return any(stack.contains(item, quantity) for stack in self.__inventory)

    def first_empty(self) -> tuple[int, int]:
        """Find the first empty slot in the inventory"""
        for i, stack in enumerate(self.__inventory):
            if stack.is_empty():
                return divmod(i, self.width)
        raise ValueError("Inventory is full")

    def find(self, item: Item | type[Item]) -> tuple[int, int]:
        """Find the first occurrence of an item in the inventory"""
        for i, stack in enumerate(self.__inventory):
            if stack.item == item if isinstance(item, type) else type(item):
                return divmod(i, self.width)
        raise ValueError("Item not found")

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
