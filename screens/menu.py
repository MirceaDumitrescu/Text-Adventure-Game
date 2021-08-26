from methods import type_text, random_examine
from text_input import text_input
import screens.directions as d
import screens.help as h
import screens.inventory as i
from map import zonemap
from character import myPlayer


def examine():
    examined = zonemap[myPlayer.location]["EXAMINED"]
    if examined == True:
        print("There is nothing to examine here. This is your home")
        game_menu()
    else:
        print("There is something to examine")
        random_examine()


def game_menu():
    game_options = f"""
__________________________________________________________
|                       GAME MENU                        |
|                                                        |
|             What do you want to do next?               |
|   [m] Change Location | [h] Help Menu | [i] Inventory  |
|       [b] Go back to Main Menu  | [e] Examine          |
|________________________________________________________|
    """
    type_text(game_options)
    menu = {
        "m": d.get_direction,
        "h": h.help_game,
        "i": i.display_inventory,
        "b": game_menu,
        "e": examine,
    }
    text_input("> ", menu)
