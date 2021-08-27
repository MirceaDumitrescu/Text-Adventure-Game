import methods as m
import screens.menu as menu
import map as map


def get_direction():

    m.cls()

    directions = """
_________________________________________________________
|                     NAVIATION MENU                     |
|                                                        |
|             Where do you want to go now?               |
|     [s] South  | [n] North | [w] West | [e] East       |
|       [b] Go back to Main Menu  | [i] Examine          |
|________________________________________________________|
    """
    m.type_text(directions)

    answer = input("> ")
    while not answer.lower() in ["s", "n", "w", "e", "b", "i"]:
        print("------Please select from the available directions above------")
        answer = input("> ")
    if answer == "s":
        map.player_movement("South")

    elif answer == "n":
        map.player_movement("North")

    elif answer == "w":
        map.player_movement("West")

    elif answer == "e":
        map.player_movement("East")

    elif answer == "b":
        menu.game_menu()

    elif answer == "i":
        menu.examine()
