import unittest
from src.game_handler.inventory import Inventory, Stack
from src.game_handler.items import Log, Stick


class TestInventory(unittest.TestCase):

    def test_append(self):
        inventory = Inventory(2, 2)
        inventory.append(Log())
        self.assertEqual(inventory.get_item(0, 0), Stack(Log(), 1))
        self.assertEqual(inventory.get_item(0, 0), Stack(Log, 1))

        inventory.append(Log())
        self.assertEqual(inventory.get_item(0, 0), Stack(Log(), 2))
        self.assertEqual(inventory.get_item(0, 0), Stack(Log, 2))
        inventory.append(Stick())
        self.assertEqual(inventory.get_item(0, 1), Stack(Stick(), 1))
        self.assertEqual(inventory.get_item(0, 1), Stack(Stick, 1))

    def test_insert_item(self):
        inventory = Inventory(2, 1)
        inventory.insert_item(Log(), 0, 1)
        self.assertEqual(inventory.get_item(0, 1), Stack(Log(), 1))
        inventory.insert_item(Log(), 0, 1)
        self.assertEqual(inventory.get_item(0, 1), Stack(Log(), 2))

        self.assertRaises(ValueError, inventory.insert_item, Stick(), 0, 1)
        inventory.insert_item(Stick(), 0, 0)
        self.assertEqual(inventory.get_item(0, 0), Stack(Stick(), 1))

    def test_get_item(self):
        inventory = Inventory(2, 1)
        self.assertEqual(inventory.get_item(0, 0), Stack())
        inventory.append(Log())
        self.assertEqual(inventory.get_item(0, 0), Stack(Log(), 1))
        self.assertEqual(inventory.get_item(0, 1), Stack())
        self.assertRaises(IndexError, inventory.get_item, 0, 2)
        self.assertRaises(IndexError, inventory.get_item, 3, 0)

    def test_remove_item(self):
        inventory = Inventory(2, 1)
        inventory.append(Log())
        stack = inventory.remove_item(0, 0)
        self.assertEqual(stack, Stack(Log(), 1))
        self.assertTrue(inventory.is_empty(0, 0))

    def test_split_item(self):
        inventory = Inventory(2, 1)
        inventory.append(Stack(Log(), 2))
        stack = inventory.split_item(0, 0)
        self.assertEqual(stack, Stack(Log(), 1))
        self.assertFalse(inventory.is_empty(0, 0))

        inventory.append(Log())
        stack = inventory.split_item(0, 0, 1)
        self.assertEqual(stack, Stack(Log(), 1))
        self.assertEqual(inventory.get_item(0, 0), Stack(Log(), 1))

        self.assertRaises(ValueError, inventory.split_item, 0, 0, 2)
        self.assertRaises(IndexError, inventory.split_item, 0, 2)

    def test_is_empty(self):
        inventory = Inventory(2, 2)
        self.assertTrue(inventory.is_empty())
        inventory.append(Log())
        self.assertFalse(inventory.is_empty())

    def test_is_empty_at(self):
        inventory = Inventory(2, 1)
        self.assertTrue(inventory.is_empty(0, 0))
        self.assertTrue(inventory.is_empty(0, 0))
        inventory.append(Log())
        self.assertFalse(inventory.is_empty(0, 0))
        self.assertTrue(inventory.is_empty(0, 1))

    def test_contains(self):
        inventory = Inventory(2, 1)
        self.assertFalse(inventory.contains(Log()))
        inventory.append(Log())
        self.assertTrue(inventory.contains(Log()))
        self.assertTrue(inventory.contains(Log(), 1))
        self.assertFalse(inventory.contains(Log(), 2))
        self.assertTrue(inventory.contains(Stack(Log(), 1)))
        self.assertFalse(inventory.contains(Stack(Log(), 2)))

    def test_first_empty(self):
        inventory = Inventory(2, 1)
        self.assertEqual(inventory.first_empty(), (0, 0))
        inventory.append(Log())
        self.assertEqual(inventory.first_empty(), (0, 1))
        inventory.insert_item(Stick(), 0, 1)
        self.assertRaises(ValueError, inventory.first_empty)

    def test_find(self):
        inventory = Inventory(2, 1)
        self.assertRaises(ValueError, inventory.find, Log())
        inventory.append(Log())
        self.assertEqual(inventory.find(Log()), (0, 0))
        inventory.insert_item(Stick(), 0, 1)
        self.assertEqual(inventory.find(Stick()), (0, 1))

    def test_get_row(self):
        inventory = Inventory(2, 2)
        self.assertEqual(inventory.get_row(0), [Stack(), Stack()])
        inventory.append(Log())
        self.assertEqual(inventory.get_row(0), [Stack(Log(), 1), Stack()])
        inventory.append(Stick())
        self.assertEqual(inventory.get_row(0), [Stack(Log(), 1), Stack(Stick(), 1)])

        self.assertEqual(inventory.get_row(1), [Stack(), Stack()])
        inventory.append(Log())
        self.assertEqual(inventory.get_row(1), [Stack(), Stack()])
        inventory.insert_item(Log(), 1, 1)
        self.assertEqual(inventory.get_row(1), [Stack(), Stack(Log(), 1)])

        self.assertRaises(IndexError, inventory.get_row, 2)

    def test_get_column(self):
        inventory = Inventory(2, 2)
        self.assertEqual(inventory.get_column(0), [Stack(), Stack()])
        inventory.append(Log())
        self.assertEqual(inventory.get_column(0), [Stack(Log(), 1), Stack()])
        inventory.append(Stick())
        self.assertEqual(inventory.get_column(0), [Stack(Log(), 1), Stack()])

        self.assertEqual(inventory.get_column(1), [Stack(Stick(), 1), Stack()])
        inventory.append(Log())
        self.assertEqual(inventory.get_column(1), [Stack(Stick(), 1), Stack()])
        inventory.insert_item(Log(), 1, 1)
        self.assertEqual(inventory.get_column(1), [Stack(Stick(), 1), Stack(Log(), 1)])

        self.assertRaises(IndexError, inventory.get_column, 2)

    def test_str(self):
        inventory = Inventory(2, 2)
        target = "Stack(item=None, quantity=0) | Stack(item=None, quantity=0)\nStack(item=None, quantity=0) | Stack(item=None, quantity=0)"

        self.assertEqual(str(inventory), target)

    def test_repr(self):
        inventory = Inventory(2, 2)
        self.assertEqual(str(inventory), repr(inventory))
