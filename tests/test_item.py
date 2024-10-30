import unittest

from src.game_handler.inventory import Inventory, Stack
from src.game_handler.items import Item, Log, Stick


class Test_Item(Item):
    ...


class TestItem(unittest.TestCase):
    def test_item_constructor(self):
        item = Log()
        self.assertEqual(item, Log())

    def test_item_repr(self):
        item = Log()
        self.assertEqual(repr(item), "Log()")
