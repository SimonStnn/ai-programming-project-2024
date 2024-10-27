import unittest

from src.game_handler.inventory import Inventory, Stack
from src.game_handler.items import Log, Stick


class TestStack(unittest.TestCase):
    def test_stack(self):
        stack = Stack()
        self.assertTrue(stack.is_empty())

        self.assertFalse(stack.contains(Log))
        self.assertFalse(stack.contains(Log()))
        self.assertFalse(stack.contains(Stack(Log)))
        self.assertFalse(stack.contains(Stack(Log())))

        self.assertEqual(stack, Stack())

    def test_quantity(self):
        stack = Stack()
        self.assertEqual(stack.quantity, 0)

        stack.add(Log())
        self.assertEqual(stack.quantity, 1)

        stack.add(Log())
        self.assertEqual(stack.quantity, 2)

        stack.reset()
        self.assertEqual(stack.quantity, 0)

    def test_item(self):
        stack = Stack()
        self.assertIsNone(stack.item)

        stack.add(Log())
        self.assertEqual(stack.item, Log)

        stack.add(Log())
        self.assertEqual(stack.item, Log)
        self.assertRaises(ValueError, stack.add, Stick())

        stack.reset()
        self.assertIsNone(stack.item)

    def test_reset(self):
        stack = Stack()
        stack.add(Log())
        stack.reset()
        self.assertEqual(stack, Stack())

    def test_is_empty(self):
        stack = Stack()
        self.assertTrue(stack.is_empty())

        stack.add(Log())
        self.assertFalse(stack.is_empty())
        self.assertEqual(stack.quantity, 1)

        stack.reset()
        self.assertTrue(stack.is_empty())
        self.assertEqual(stack.quantity, 0)

    def test_is_full(self):
        stack = Stack(Log(), 64, capacity=64)
        self.assertTrue(stack.is_full())

        stack = Stack(Log(), 63, capacity=64)
        self.assertFalse(stack.is_full())

    def test_add(self):
        stack = Stack()
        self.assertFalse(stack.contains(Log))

        stack.add(Log())
        self.assertFalse(stack.is_empty())

        self.assertTrue(stack.contains(Log))
        self.assertTrue(stack.contains(Log()))
        self.assertTrue(stack.contains(Stack(Log)))
        self.assertTrue(stack.contains(Stack(Log())))
        self.assertFalse(stack.contains(Stack(Log, 2)))

        self.assertEqual(stack, Stack(Log(), 1))

        stack.add(Log())
        self.assertNotEqual(stack, Stack(Log(), 1))
        self.assertEqual(stack, Stack(Log(), 2))

        self.assertRaises(ValueError, stack.add, Stick())

        stack = Stack(Log(), 63, capacity=64)
        self.assertRaises(ValueError, stack.add, 2)

    def test_remove(self):
        stack = Stack(Log(), 2)
        stack.remove(1)
        self.assertEqual(stack, Stack(Log(), 1))

        stack.remove(1)
        self.assertEqual(stack, Stack())
        self.assertTrue(stack.is_empty())

        self.assertRaises(ValueError, stack.remove, 1)

    def test_split(self):
        stack = Stack(Log(), 2)
        new_stack = stack.split()
        self.assertEqual(stack, Stack(Log(), 1))
        self.assertEqual(new_stack, Stack(Log(), 1))

        new_stack = stack.split(1)
        self.assertEqual(stack, Stack())
        self.assertEqual(new_stack, Stack(Log(), 1))

        self.assertRaises(ValueError, stack.split, 1)

    def test_join(self):
        stack = Stack(Log(), 1, capacity=64)
        new_stack = Stack(Log(), 1)
        stack.join(new_stack)
        self.assertEqual(stack, Stack(Log(), 2))
        self.assertEqual(new_stack, Stack())

        stack.join(Stack(Log(), 1))
        self.assertEqual(stack, Stack(Log(), 3))

        new_stack = Stack(Stick(), 1)
        self.assertRaises(ValueError, stack.join, new_stack)

        # Test capacity
        stack = Stack(Log(), 36, capacity=64)
        stack2 = Stack(Log(), 64, capacity=64)
        stack.join(stack2)
        self.assertEqual(stack, Stack(Log(), 64))
        self.assertEqual(stack2, Stack(Log(), 36))

    def test_has(self):
        stack = Stack(Log(), 5)
        self.assertTrue(stack.has(Log))
        self.assertTrue(stack.has(Log()))
        self.assertTrue(stack.has(5))
        self.assertFalse(stack.has(2))
        self.assertFalse(stack.has(Stick))
        self.assertFalse(stack.has(Stick()))
