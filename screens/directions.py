from methods import cls, type_text
from map import player_movement
def get_direction():
    cls()
    directions = """
_________________________________________________________
|                                                        |
|             Where do you want to go now?               |
|     [s] South  | [n] North | [w] West | [e] East       |
|________________________________________________________|
    """
    type_text(directions)
    answer = input("> ")
    while not answer.lower() in ["s","n","w","e"]:
        print("------Please select from the available directions above------")
        answer = input("> ")
    if answer == "s":
        player_movement("South")

    elif answer == "n":
        player_movement("North")

    elif answer == "w":
        player_movement("West")

    elif answer == "e":
        player_movement("East")
