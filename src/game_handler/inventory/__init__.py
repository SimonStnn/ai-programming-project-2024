from src.game_handler.items import Item


class Inventory:
    def __init__(self):
        self.inventory: list[Item] = []

    def add_item(self, item):
        self.inventory.append(item)

    def remove_item(self, item):
        self.inventory.remove(item)

    def get_inventory(self):
        return self.inventory

    def get_item(self, item):
        for i in self.inventory:
            if i == item:
                return i
        return None

    def __str__(self):
        return str(self.inventory)
