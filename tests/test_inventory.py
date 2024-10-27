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
