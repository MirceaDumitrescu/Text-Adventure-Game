import sys
import time
import os

class Player():
    def __init__(self, name, hp, starting_kit, stamina, intelect, charisma, location="a1"):
        self.name = name
        self.hp = hp
        self.starting_kit = starting_kit
        self.stamina = 100
        self.intelect = 100
        self.charisma = 10
#now you can call methods like: myPlayer.location
myPlayer = Player()


def setup_game():
    pass

##### Defined Function to type words slowly
def type_sys_text(i):
    for char in i:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.003)
    # player_input = input("> ")
    # os.system("clear")

##### Defined Function to call inventory
### this will have more complex features in the future
def get_inventory():
    inventory = f"""

===============================================================
|                                                              |
|    Level: self.level      Health: self.health      Location: self.location     |
|                                                              |
===============================================================
|                                                              |
|                                                              |
|                      --- Inventory ---                       |
|                                                              |
|                                                              |
===============================================================
    [1] Phone                   [4] Apple
    [2] Gun (3 bullets)         [5] Cigaretes
    [3] Bottle of Vodka         [6] Letter

"""
    for char in inventory:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.001)
    # player_input = input("> ")
    # os.system("clear")