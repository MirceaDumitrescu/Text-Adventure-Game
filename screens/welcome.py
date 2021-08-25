import sys
from methods import type_text, loading, write, loads, starting_kits
from character import myPlayer
from text_input import text_input
from screens.menu import game_menu

player = {}


def welcome():
    welcome = """

#####################################################
       _____  __                __               
      / ___/ / /_   ____ _ ____/ /____  _      __
      \__ \ / __ \ / __ `// __  // __ \| | /| / /
     ___/ // / / // /_/ // /_/ // /_/ /| |/ |/ / 
    /____//_/ /_/ \__,_/ \__,_/ \____/ |__/|__/  

    __  ___                        ____   ____   ______
   /  |/  /____   ____   ____     / __ \ / __ \ / ____/
  / /|_/ // __ \ / __ \ / __ \   / /_/ // /_/ // / __  
 / /  / // /_/ // /_/ // / / /  / _, _// ____// /_/ /  
/_/  /_/ \____/ \____//_/ /_/  /_/ |_|/_/     \____/   
                                                       
######################################################
           Copyright Python Task Force 2021

                       [1] Play <
                       [2] Quit <
"""
    type_text(welcome)
    menu = {"1": setup_game, "2": sys.exit}
    text_input("> ", menu)
    game_menu()


def setup_game():
    type_text(
        """
        ▛▝▝▝▝▝▝▝▝▝▝▝▝▝▝▝▝▝▝▝▝▝▝▝▝▝▝▝▝▝▝▝▝▝▝▝ ▜
                  WHAT IS YOUR NAME?      
        ▙ ▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▟

                How should we call you?

    """
    )
    name = input("> ").capitalize()
    myPlayer.name = name
    type_text(
        """
        ▛▝▝▝▝▝▝▝▝▝▝▝▝▝▝▝▝▝▝▝▝▝▝▝▝▝▝▝▝▝▝▝▝▝▝▝ ▜
                  WHAT IS YOUR JOB?      
        ▙ ▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▟

   You can choose between Medic, Police and Tehnician.

    """
    )
    selected_kit = input("> ").upper()
    while selected_kit not in starting_kits.keys():
        type_text(
            """
        ▛▝▝▝▝▝▝▝▝▝▝▝▝▝▝▝▝▝▝▝▝▝▝▝▝▝▝▝▝▝▝▝▝▝▝▝ ▜
             TRY AGAIN! WHAT IS YOUR JOB?      
        ▙ ▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▟
   You can choose between Medic, Police and Tehnician.
 Make sure you type the correct job name as written above!
    """
        )
        selected_kit = input("> ").upper()
    myPlayer.starting_kit = selected_kit
    # once the player chooses the kit we will store it in data/character.json
    player[selected_kit] = {
        "potions": starting_kits[selected_kit]["POTIONS"],
        "bullet": starting_kits[selected_kit]["BULLETS"],
        "keys": starting_kits[selected_kit]["KEYS"],
        "clues": starting_kits[selected_kit]["CLUES"],
        "letter": starting_kits[selected_kit]["LETTERS"],
        "food": starting_kits[selected_kit]["FOOD"],
    }
    write("data/character.json", player)
    # to print their inventories
    starting_potions = starting_kits[selected_kit]["POTIONS"]
    starting_bullets = starting_kits[selected_kit]["BULLETS"]
    starting_keys = starting_kits[selected_kit]["KEYS"]

    type_text(
        f"""
        ◤━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━◥
                  YOU ARE NOW A {myPlayer.starting_kit}
        ◣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━◢

            You will start with {starting_potions} potions,
                {starting_bullets} bullets and {starting_keys} keys
                in your inventory!

"""
    )

    loading(delay=5, text=loads)
