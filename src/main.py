from src.root import Window
from src.game_handler.player import Player
from src.game_handler.items import Log, Mossy_Log


if __name__ == "__main__":
    player = Player()

    log = Log()
    mossy_log = Mossy_Log()


    player.inventory.add_item(log)
    player.inventory.add_item(mossy_log)
    print(str(log))

    print(player.inventory)


game = Window()
game.run()
