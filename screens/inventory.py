from methods import cls, type_text, loading, loads
from character import get_inventory, get_job, myPlayer, read_json, create_json
import screens.menu as menu


def display_inventory():
    cls()
    job = get_job()
    inventory = f"""

===============================================================
|                                                              |
    Name: {myPlayer.name}      Health: {myPlayer.hp}      Location: {myPlayer.location}         
|                                                              |
===============================================================
|                                                              |
|                                                              |
|                      --- Inventory ---                       |
|                                                              |
|                                                              |
===============================================================
    [1] {get_inventory(job, "potions")} Potions                   [4] {get_inventory(job, "letter")} Letters
    [2] {get_inventory(job, "bullet")} Bullets                   [5] {get_inventory(job, "clues")} Clues
    [3] {get_inventory(job, "keys")} Keys                      [6] {get_inventory(job, "food")} Apples

"""
    type_text(inventory)
    loading(5, loads)
    menu.game_menu()
