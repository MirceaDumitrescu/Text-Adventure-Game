import methods as m
import screens.menu as menu
import map as map
import character as c


def get_direction():

    m.cls()

    directions = f"""
            a1---a2
                 |    |--a5   c4--c5--c6
            b5   a3--a4       |
            |         |--b1   c3--d1--d2
            |         |       |
            b4--b3---b2--c1--c2--e1--e2--e3
_________________________________________________________
|                    NAVIGATION MENU                     |
           Current location: {map.zonemap[c.myPlayer.location]["NAME"]}
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
