import sys
import time
import os
from os import path
import json
import math
from text_input import text_input
from inventory import get_inventory
from map import  player_movement
from character import Player

myPlayer = Player()

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def read(file: str):
    return json.load(open(file))
def write(file: str, data: dict):
    with open(file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

##### Define Function to type words slowly
def type_sys_text(txt):
    i = 0
    speed = 5
    #This to write {speed} chars at once since the limitation of float number is 10^-9 aka, 
    #if the time.sleep is not fast/slow enought
    while i < len(txt):
        delta = len(txt) - i - speed
        if delta <= 0:
            speed = speed - abs(delta) #Prevent out of range
        for b in range(0, speed):
            sys.stdout.write(txt[i + b])
            sys.stdout.flush()
        
        time.sleep(math.pow(10, -3)) #delay between when the chars are written
        i += speed

def loading(delay: int, text: str):
    #horizontal length should be divisable to delay, if not, 
    # you can add blank spaces to the begining and the end of the variable to make it divisable
    i = 0
    t = 0
    while t <= delay:
        delta = int(len(text) / delay)
        n = i + delta
        sys.stdout.write(text[i:n])
        sys.stdout.flush()
        i = n
        t += 1
        if t != delay: time.sleep(1)

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

player = {}

#TODO: Need rework for the 'loading' variable
loads = ">>==============================================<<"

if not path.exists('data'):
    os.mkdir('data')

if not os.path.exists('data/character.json'):
    write('data/character.json', {})
else:
    player = read('data/character.json')


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
    type_sys_text(welcome)
    menu = {"1": setup_game,
        "2": sys.exit
       }
    text_input("> ", menu)
    game_menu()

def setup_game():
    name = input("""
        _________________________________________    
        |          WHAT IS YOUR NAME?           |
        ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
                How should we call you?
    
    > """).capitalize()
    myPlayer.name = name
    selected_kit =  input("""
        _________________________________________    
        |           WHAT IS YOUR JOB?           |
        ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
   You can choose between Medic, Police and Tehnician.
    
    > """).upper()
    while selected_kit not in starting_kits.keys():
        selected_kit =  input("""
        _________________________________________    
        |     TRY AGAIN! WHAT IS YOUR JOB?      |
        ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
   You can choose between Medic, Police and Tehnician.
 Make sure you type the correct job name as written above!
    
    > """).upper()

    #once the player chooses the kit we will store it in data/character.json
    player[selected_kit] = {
        "potions": starting_kits[selected_kit]["POTIONS"],
        "bullet": starting_kits[selected_kit]["BULLETS"],
        "keys": starting_kits[selected_kit]["KEYS"]
    }
    write('data/character.json', player)
    #to print their inventories
    starting_potions = starting_kits[selected_kit]["POTIONS"]
    starting_bullets = starting_kits[selected_kit]["BULLETS"]
    starting_keys = starting_kits[selected_kit]["KEYS"]

    print(f"""
    _________________________________________    
    |      YOU ARE NOW A {selected_kit}          |
    ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
        You will start with {starting_potions} potions,
            {starting_bullets} bullets and {starting_keys} keys
            in your inventory!

        The game will start in 5 seconds.....
    """)
    
    loading(delay=5, text=loads)


##### Defined Function to call inventory
### this will have more complex features in the future
def display_inventory():
    cls()
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
    type_sys_text(inventory)
    loading(5, loads)
    game_menu()



def help_game():
    cls()
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
    loading(5, loads)
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
    menu = {
        "m": get_direction,
        "h": help_game,
        "i": display_inventory
        }
    text_input("> ", menu)


def get_direction():
    cls()
    directions = """
_________________________________________________________
|                                                        |
|             Where do you want to go now?               |
|     [s] South  | [n] North | [w] West | [e] East       |
|________________________________________________________|
    """
    type_sys_text(directions)
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