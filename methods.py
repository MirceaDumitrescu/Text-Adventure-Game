import sys
import time
import os
from text_input import text_input
from inventory import get_inventory
from inventory import add_inventory
from map import  player_movement
from character import Player

myPlayer = Player()

starting_kits = {
                "MEDIC": {
                "POTIONS": 3,
                "BULLETS": 1,
                "KEYS": 1 },
                "POLICE": {
                "POTIONS": 1,
                "BULLETS": 3,
                "KEYS": 1 },
                "TEHNICIAN": {
                "POTIONS": 1,
                "BULLETS": 1,
                "KEYS": 3 }
                }


def setup_game():
    name = input("""
        _________________________________________    
        |          WHAT IS YOUR NAME?           |
        ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
                How should we call you?
    
    > """).capitalize()
    #print(f"Your name is {name}")
    myPlayer.name = name

    selected_kit =  input("""
        _________________________________________    
        |           WHAT IS YOUR JOB?           |
        ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
   You can choose between Medic, Police and Tehnician.
    
    > """).upper()
    #print(f"Your job is {selected_kit}")
    while selected_kit not in starting_kits.keys():
        selected_kit =  input("""
        _________________________________________    
        |     TRY AGAIN! WHAT IS YOUR JOB?      |
        ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
   You can choose between Medic, Police and Tehnician.
 Make sure you type the correct job name as written above!
    
    > """).upper()
    else:
        #once the player chooses the kit we will store it in selected_kit
        myPlayer.starting_kit = selected_kit

        #to print their inventories
        starting_potions = starting_kits[myPlayer.starting_kit]["POTIONS"]
        starting_bullets = starting_kits[myPlayer.starting_kit]["BULLETS"]
        starting_keys = starting_kits[myPlayer.starting_kit]["KEYS"]

        print(f"""
        _________________________________________    
        |      YOU ARE NOW A {selected_kit}          |
        ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
            You will start with {starting_potions} potions,
                {starting_bullets} bullets and {starting_keys} keys
                in your inventory!
        """)
        time.sleep(5)



##### Defined Function to type words slowly
def type_sys_text(i):
    for char in i:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.003)
    # player_input = input("> ")
    # os.system("clear")

##### Defined Function to call inventory
### this will have more complex features in the future
def display_inventory():
    inventory = f"""

===============================================================
|                                                              |
|    Name: {myPlayer.name}      Health: {myPlayer.hp}      Location: {myPlayer.location}         |
|                                                              |
===============================================================
|                                                              |
|                                                              |
|                      --- Inventory ---                       |
|                                                              |
|                                                              |
===============================================================
    [1] {get_inventory("slot1")} Potions                   [4] {get_inventory("slot4")} Letters
    [2] {get_inventory("slot2")} Bullets                   [5] {get_inventory("slot5")} Clues
    [3] {get_inventory("slot3")} Keys                      [6] {get_inventory("slot6")} Apples

"""
    for char in inventory:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.001)
    # player_input = input("> ")
    # os.system("clear")
    time.sleep(5)
    game_menu()

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

##### Calling out the function from methods.py to type the welcome message when program run

    type_sys_text(welcome)
    menu = {"1": setup_game,
        "2": sys.exit
       }
    text_input("> ", menu)
    game_menu()

def help_game():
    help_info = """

 ____  ____  ________  _____     _______   
|_   ||   _||_   __  ||_   _|   |_   __ \  
  | |__| |    | |_ \_|  | |       | |__) | 
  |  __  |    |  _| _   | |   _   |  ___/  
 _| |  | |_  _| |__/ | _| |__/ | _| |_     
|____||____||________||________||_____|    
                                           
                              
Discover the mistery behind the murder of Ardit, 
the scientist. Ardit was the brother of the Medic, 
lover of the Police officer and best friend of the Tehnician. 
Embark into this mistery from all three perspectives 
and see if you can find out who murdered Ardit.

        _________________________________________    
        |          AVAILABLE COMMANDS           |
        ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
  During any interaction the game will ask for your input 
  in the from of a number which coresponds to one of the  
             options provided by the game.
  Make sure to type a valid answer to continue the game.

        _________________________________________    
        |        ABOUT MAP & LOCATIONS          |
        ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
     Some rooms or locations are locked by default. 
     You can use keys from your inventory to unlock 
      them or solve the puzzle from that location.

        _________________________________________    
        |         HOW TO BEAT THE GAME?         |
        ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
   Once you reach the last room and solve the puzzle 
        (without getting killed in the process) 
              you will finish the game.
############################################################
The game will continue in 5 seconds... Please read carefully

  """
    type_sys_text(help_info)
    time.sleep(5)
    game_menu()


def game_menu():
    game_options = """
_________________________________________________________
|                                                        |
|             What do you want to do next?               |
|   [m] Change Location | [h] Help Menu | [i] Inventory  |
|________________________________________________________|
    """
    type_sys_text(game_options)
    menu = {"m": get_direction,
        "h": help_game,
        "i": display_inventory,}
    text_input("> ", menu)


def get_direction():
    directions = """
_________________________________________________________
|                                                        |
|             Where do you want to go now?               |
|     [s] South  | [n] North | [w] West | [e] East       |
|________________________________________________________|
    """
    type_sys_text(directions)
    menu = {"s": player_movement("South"),
        "n": player_movement("North"),
        "w": player_movement("West"),
        "e": player_movement("East")}
    text_input("> ", menu)