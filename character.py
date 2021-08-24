import json
import os
from os import path


def read(file: str):
    return json.load(open(file))
def write(file: str, data: dict):
    with open(file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def create_json():
    if not path.exists('data'):
        os.mkdir('data')
    if not os.path.exists('data/character.json'):
        write('data/character.json', {})
    else:
        os.remove('data/character.json') #Added step to delete and recreate file every time game is ran
        write('data/character.json', {})
        player = read('data/character.json')


class Player():
    def __init__(self):
        self.name = ""
        self.hp = 50
        self.starting_kit = ""
        self.stamina = 100
        self.intelect = 100
        self.charisma = 10
        self.location = "a1"
myPlayer = Player()


with open("data/character.json", "r+") as f:
    player_inventory = json.load(f)

def set_job(key):
    myPlayer.starting_kit = key

def get_job():
    res = list(player_inventory.keys())[0]
    return res

    #method to get item in slot
def get_inventory(job, key):
    return player_inventory[job][key]

#method to add items to inventory
def set_inventory(job, key, value):
    player_inventory[job][key] = value






# note this is not finished and will be recoded because of the identation problem that came from another IDE, and also semplified with Methods instead of classes
# you can continue work, ignore this section.




# import random
# class Character:
#     intellect = 100
#     charisma = 10

#     def __init__(self,name, health = 100, stamina = 50):
#         self.name = name
#         self.health = health
#         self.stamina = stamina


# print("Welcome To Adventure Game\n")
# character_1 = Character(input("Your Character's name: "))

# print(f"  stamina:{character_1.stamina}\\50\n  health:{character_1.health}\\100\n")

# Room_items = {"key1": 10,"key2":0}
# infomations = ["There is tooth brush", "There is a key"]

# # class Actions():
    
#   def __init__(self,info, health = 100, stamina = 50):
#     self.health = health
#     self.stamina = stamina
#     self.info = info
        
#   def examine(self,respond,items):
#     inventory=[]
#     self.respond = respond
#     self.items = items
        
#     if respond == "Yes":
#       for i in self.items.keys():
#         inventory.append(i)
#         return inventory
        
#     elif type(respond) != str:
#         return print("please answer with Yes or No")
        
#     elif respond == "No":
#         return None
        
#     # def attack(self,):


#   # print("You character's action are Examine, Attack, Interact, Type any action while you explore the dungeon")

#   #  Action = input("your action: ")

#   # if Action == "examine":
#   #     action_1 = Actions(infomations)
#   #     print(action_1.info[1])
#   #     action_1.examine(input("Take the item: "),Room_items)
#       # print(action_1.inventory)

# # Other Methods
