import unittest

from src.game_handler.inventory import Inventory, Stack
from src.game_handler.items import Item, Log, Stick


class Test_Item(Item):
    """This is a test item"""


class TestItem(unittest.TestCase):
    def test_item_constructor(self):
        item = Log()
        self.assertEqual(item, Log())

    def test_item_repr(self):
        item = Log()
        self.assertEqual(repr(item), "Log()")

    def test_eq(self):
        item = Log()
        self.assertEqual(item, Log())
        self.assertEqual(item, Log)
        self.assertNotEqual(item, Stick())
        self.assertNotEqual(item, Stick)

    def test_item_name(self):
        item = Log()
        self.assertEqual(item.name, "Log")
        self.assertEqual(item.name, Log.__name__.replace("_", " "))
        self.assertEqual(Log.name, "Log")
        self.assertEqual(Log.name, Log.__name__.replace("_", " "))

        item = Test_Item()
        self.assertEqual(item.name, "Test Item")
        self.assertEqual(item.name, Test_Item.__name__.replace("_", " "))
        self.assertEqual(Test_Item.name, "Test Item")
        self.assertEqual(Test_Item.name, Test_Item.__name__.replace("_", " "))

    def test_item_description(self):
        item = Log()
        self.assertEqual(item.description, Log.__doc__)

        item = Test_Item()
        self.assertEqual(item.description, "This is a test item")
        self.assertEqual(item.description, Test_Item.__doc__)