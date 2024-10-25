"""Stack to fill a slot in an inventory"""
from typing import overload, Self, Protocol
from copy import copy
from attrs import define, field, Factory
from src.game_handler.items import Item


class _StackType(Protocol):
    item: Item | type[Item] | None
    quantity: int
    capacity: int


@define
class Stack:
    item: Item | type[Item] | None = field(
        default=None,
        converter=lambda item: type(item) if isinstance(item, Item) else item
    )
    quantity: int = field(default=0, validator=lambda _, __, value: value >= 0)
    capacity: int = field(default=64, repr=False, kw_only=True)

    @staticmethod
    def can_join(stack1: "Stack", stack2: "Stack") -> bool:
        """Check if two stacks can be joined"""
        return (((stack1.item is None and stack2.item is not None) or
                 stack1.item == stack2.item) and
                stack1.capacity == stack2.capacity)

    @overload
    def add(self, quantity: int):
        """Add a quantity of items to the stack"""

    @overload
    def add(self, item: Item):
        """Add an item to the stack"""

    def add(self, item: Self | Item | int):
        if self.is_full():
            raise ValueError("Stack is full")

        if isinstance(item, Item):
            if self.item is None:
                self.item = item
            elif self.item != item:
                raise ValueError("Item type mismatch")
            self.quantity += 1
        elif isinstance(item, Stack):
            self.join(item)
        else:
            self.quantity += item

    def remove(self, quantity: int):
        self.quantity -= quantity
        if self.quantity <= 0:
            self.reset()

    def reset(self):
        self.item = None
        self.quantity = 0

    def split(self, quantity: int = -1) -> "Stack":
        if quantity == -1:
            quantity = self.quantity // 2
        self.remove(quantity)
        new_stack = copy(self)
        new_stack.quantity = quantity
        return new_stack

    def join(self, stack: "Stack") -> None:
        """Join a stack with this stack"""
        if not Stack.can_join(self, stack):
            raise ValueError("Cannot join stacks")
        if self.quantity + stack.quantity > self.capacity:
            stack.quantity -= self.capacity - self.quantity
        if self.item is None:
            self.item = stack.item
        self.quantity += stack.quantity
        stack.reset()

    def is_empty(self) -> bool:
        return self.quantity == 0

    def is_full(self) -> bool:
        return self.quantity == self.capacity

    @overload
    def has(self, quantity: int) -> bool:
        return self.quantity >= quantity

    @overload
    def has(self, item: Item | type[Item]) -> bool:
        return self.item == item

    def has(self, item: Item | type[Item] | int) -> bool:
        if isinstance(item, int):
            return self.quantity >= item
        return self.item == item if isinstance(item, type) else self.item == item.__class__

    def contains(self, item: Item | type[Item] | _StackType, quantity: int = 1) -> bool:
        if isinstance(item, Stack):
            quantity = item.quantity
            item = item.item
        return self.has(item) and self.has(quantity)


if __name__ == "__main__":
    stack = Stack()
    print(stack)
