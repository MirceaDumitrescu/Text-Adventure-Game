import methods as m
import character as c
import screens.menu as menu


def display_inventory():
    m.cls()
    job = c.get_job()
    inventory = f"""

===============================================================
|                                                              |
    Name: {c.myPlayer.name}      Health: {c.myPlayer.hp}      Location: {c.myPlayer.location}         
|                                                              |
===============================================================
|                                                              |
|                                                              |
|                      --- Inventory ---                       |
|                                                              |
|                                                              |
===============================================================
    [1] {c.get_inventory(job, "potions")} Potions                   [4] {c.get_inventory(job, "letter")} Letters
    [2] {c.get_inventory(job, "bullet")} Bullets                   [5] {c.get_inventory(job, "clues")} Clues
    [3] {c.get_inventory(job, "keys")} Keys                      [6] {c.get_inventory(job, "food")} Apples

"""
    m.type_text(inventory)
    m.loading(5, m.loads)
    menu.game_menu()
