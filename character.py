import json
import os
from os import path
import methods as m


def create_json():
    if not path.exists("data"):
        os.mkdir("data")
    if not os.path.exists("data/character.json"):
        m.write("data/character.json", {})


class Player:
    def __init__(self):
        self.name = ""
        self.hp = 50
        self.starting_kit = ""
        self.stamina = 100
        self.intelect = 100
        self.charisma = 10
        self.location = "a1"


myPlayer = Player()
player_inventory = {}


def read_json():
    global player_inventory
    if os.path.exists("data/character.json"):
        with open("data/character.json", "r+") as f:
            player_inventory = json.load(f)
    else:
        print("Character.json does not exist")


def set_job(key):  # method to set the job of the player
    myPlayer.starting_kit = key


def get_job():  # method to get the job of the player
    global player_inventory
    with open("data/character.json", "r+") as f:
        player_inventory = json.load(f)
        res = list(player_inventory.keys())[0]
    return res


def get_inventory(job, key):  # method to get item in slot
    global player_inventory
    m.read("data/character.json")
    return player_inventory[job][key]


def set_inventory(job, key, value):  # method to add items to inventory
    global player_inventory
    player_inventory[job][key] = value
    m.write("data/character.json", player_inventory)
