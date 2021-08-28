import sys
import character as c
from text_input import text_input
from screens.menu import game_menu
import methods as m

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
    m.type_text(welcome)
    menu = {"1": setup_game, "2": sys.exit}
    text_input("> ", menu)
    game_menu()


def setup_game():
    m.type_text(
        """
        ▛▝▝▝▝▝▝▝▝▝▝▝▝▝▝▝▝▝▝▝▝▝▝▝▝▝▝▝▝▝▝▝▝▝▝▝ ▜
                  WHAT IS YOUR NAME?      
        ▙ ▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▟

                How should we call you?

    """
    )
    name = input("> ").capitalize()
    c.myPlayer.name = name
    m.type_text(
        """
        ▛▝▝▝▝▝▝▝▝▝▝▝▝▝▝▝▝▝▝▝▝▝▝▝▝▝▝▝▝▝▝▝▝▝▝▝ ▜
                  WHAT IS YOUR JOB?      
        ▙ ▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▟

   You can choose between Medic, Police and Technician.

    """
    )
    selected_kit = input("> ").upper()
    while selected_kit not in m.starting_kits.keys():
        m.type_text(
            """
        ▛▝▝▝▝▝▝▝▝▝▝▝▝▝▝▝▝▝▝▝▝▝▝▝▝▝▝▝▝▝▝▝▝▝▝▝ ▜
             TRY AGAIN! WHAT IS YOUR JOB?      
        ▙ ▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▖▟
   You can choose between Medic, Police and Technician.
 Make sure you type the correct job name as written above!
    """
        )
        selected_kit = input("> ").upper()
    c.myPlayer.starting_kit = selected_kit
    # once the player chooses the kit we will store it in data/character.json
    player[selected_kit] = {
        "potions": m.starting_kits[selected_kit]["POTIONS"],
        "bullet": m.starting_kits[selected_kit]["BULLETS"],
        "keys": m.starting_kits[selected_kit]["KEYS"],
        "clues": m.starting_kits[selected_kit]["CLUES"],
        "letter": m.starting_kits[selected_kit]["LETTERS"],
        "food": m.starting_kits[selected_kit]["FOOD"],
    }
    m.write("data/character.json", player)
    # to print their inventories
    starting_potions = m.starting_kits[selected_kit]["POTIONS"]
    starting_bullets = m.starting_kits[selected_kit]["BULLETS"]
    starting_keys = m.starting_kits[selected_kit]["KEYS"]

    m.type_text(
        f"""
        ◤━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━◥
                  YOU ARE NOW A {c.myPlayer.starting_kit}
        ◣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━◢

            You will start with {starting_potions} potions,
                {starting_bullets} bullets and {starting_keys} keys
                in your inventory!

"""
    )

    m.loading(delay=5, text=m.loads)
