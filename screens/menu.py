from methods import type_text
from text_input import text_input
import screens.directions as m
import screens.help as h
import screens.inventory as i
def game_menu():
    game_options = f"""
__________________________________________________________
|                                                        |
|             What do you want to do next?               |
|   [m] Change Location | [h] Help Menu | [i] Inventory  |
|________________________________________________________|
    """
    type_text(game_options)
    menu = {
        "m": m.get_direction,
        "h": h.help_game,
        "i": i.display_inventory
        }
    text_input("> ", menu)