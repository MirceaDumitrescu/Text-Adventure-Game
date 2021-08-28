from text_input import text_input
import screens.directions as d
import screens.help as h
import screens.inventory as i
import map as map
import character as c
import methods as m
import time


def examine():
    if map.zonemap[c.myPlayer.location]["EXAMINED"] == True:
        print("----------> There is nothing to examine here! <----------")
        time.sleep(1)
        game_menu()
    else:
        m.do.random_examine()


def game_menu():
    game_options = f"""
__________________________________________________________
|                       GAME MENU                        |
|                                                        |
|             What do you want to do next?               |
|   [m] Change Location | [h] Help Menu | [i] Inventory  |
|                      [e] Examine                       |
|________________________________________________________|
    """
    m.type_text(game_options)
    menu = {
        "m": d.get_direction,
        "h": h.help_game,
        "i": i.display_inventory,
        "b": game_menu,
        "e": examine,
    }
    text_input("> ", menu)
