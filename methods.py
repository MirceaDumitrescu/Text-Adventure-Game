import sys
import time
import os
import math
import json
import random
import character as c
import screens.menu as m
import map as map
from screens import inventory 


def cls():
    os.system("cls" if os.name == "nt" else "clear")


##### Define Function to type words slowly
def type_text(txt):
    i = 0
    speed = 6
    # This to write {speed} chars at once since the limitation of float number is 10^-9 aka,
    # if the time.sleep is not fast/slow enought
    while i < len(txt):
        delta = len(txt) - i - speed
        if delta <= 0:
            speed = speed - abs(delta)  # Prevent out of range
        for b in range(0, speed):
            sys.stdout.write(txt[i + b])
            sys.stdout.flush()
        time.sleep(math.pow(10, -3))  # delay between when the chars are written
        i += speed


def loading(delay: int, text: str):
    # Length should be divisable to delay, if not,
    # you can add blank spaces to the begining and the end of the variable to make it divisable
    if len(text) % delay != 0:
        raise ValueError("Text length must be divisable to delay")

    i = 0
    t = 0
    while t <= delay:
        delta = int(len(text) / delay)
        n = i + delta
        sys.stdout.write(text[i:n])
        sys.stdout.flush()
        i = n
        t += 1
        if t != delay:
            time.sleep(1)


def read(file: str):
    return json.load(open(file))


def write(file: str, data: dict):
    with open(file, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


starting_kits = {
    "MEDIC": {
        "POTIONS": 3,
        "BULLETS": 1,
        "KEYS": 1,
        "CLUES": 0,
        "LETTERS": 0,
        "FOOD": 0,
    },
    "POLICE": {
        "POTIONS": 1,
        "BULLETS": 3,
        "KEYS": 1,
        "CLUES": 0,
        "LETTERS": 0,
        "FOOD": 0,
    },
    "TEHNICIAN": {
        "POTIONS": 1,
        "BULLETS": 1,
        "KEYS": 3,
        "CLUES": 0,
        "LETTERS": 0,
        "FOOD": 0,
    },
}


loads = "Loading [▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰] 100%"
loads_shorter = "[▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰] 100%"


# Available output actions:
# - Discover loot (Potion, Bullet, Key, Clue, Letter or Food) - also random
# - Discover NPC - dialogue starts
# - Initiate an encounter/attack - fight is being done via roll dice method


class Action:
    def __init__(self):
        pass

    def random_examine(self):
        r1 = random.randint(1, 3)
        #we need to add one more possibility for good npc
        if r1 == 1:
            do.loot_item()
            print("Loot Action rolled")
        elif r1 == 2:
            do.loot_item()  # to be changed
            print("NPC Action rolled")
        elif r1 == 3:
            do.loot_item()  # to be changed
            print("Enemy Action rolled")
        else:
            # "An error with the random_examine function!"
            print("Hello there passer, Stop")
            self.enemy_encounter()

    def loot_item(self):
        possible_loot = ["potions", "bullet", "keys", "clues", "letter", "food"]
        r2 = random.randint(1, 3)
        r3 = random.choice(possible_loot)
        c.set_inventory(c.get_job(), r3, r2)
        map.zonemap[c.myPlayer.location]["EXAMINED"] = True
        print(
            f"""
              
    ▕▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▿▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▏
     
                  LOOT FOUND !!!
    
        {r2}x {r3} was added in your inventory

    ▕▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▵▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▏
              
              """
        )
        time.sleep(1)
        loading(delay=2, text=loads_shorter)
        m.game_menu()

    def npc_encounter(self):
        print("Test")
        # We need NPC dialogue database with NPC informations
        m.game_menu()

    def enemy_encounter(self):
        print("Test2")
        # We need Enemy dialogue database with Enemy informations
        #then we need the player to lose health depending on dialogue
        c.myPlayer.hp -= 10
        print(f"-{c.myPlayer.hp}")
        #search for weapons in inventory
        self.use_items()
        m.game_menu()

    def use_items(self):
        #showing items that can be used
        show_inventory = inventory.display_inventory()
        user_input = input("Select an item to use: ")
        if "1" in user_input:
            print("potions is equiped")
            c.myPlayer.hp += 10
            print(f"Your Health is {c.myPlayer.hp}")
        elif "2" in user_input:
            #the weapon to attach enemy npcs
            print("bullet is equiped")
            self.attack()
        elif "3" in user_input:
            #To be used around the map
            print("key is equiped")
        elif "4" in user_input:
            #letters
            print("letter is equiped")
        elif "5" in user_input:
            #clues
            print("Clues are equiped")
        elif "6" in user_input:
            #health regain
            print("Apples are equiped")
            c.myPlayer.hp += 10
            print(f"Your Health is {c.myPlayer.hp}")
        
    def attack(self):
        #attacking mechanic
        #we need text to tell us we defeated the enemy npc 
        pass


        



do = Action()

