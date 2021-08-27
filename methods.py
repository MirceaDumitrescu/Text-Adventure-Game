import sys
import time
import os
import math
import json
import random
import character as c
import screens.menu as m
import map as map


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
            "An error with the random_examine function!"

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
        m.game_menu()


do = Action()
