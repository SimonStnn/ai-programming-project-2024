"""Stack to fill a slot in an inventory"""
from typing import overload, Self
from attrs import define, field, Factory
from src.game_handler.items import Item


@define
class Stack:
    item: Item | None = field(default=None)
    quantity: int = field(default=0)
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

    def split(self, quantity: int) -> "Stack":
        new_stack = Stack(item=self.item, quantity=quantity)
        self.remove(quantity)
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


if __name__ == "__main__":
    stack = Stack()
    print(stack)
