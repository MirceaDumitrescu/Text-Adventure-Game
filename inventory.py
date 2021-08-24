import json

# Create an inventory dictionary with maximum 6 slots
with open("data/character.json", "r+") as f:
    player_inventory = json.load(f)

#method to get item in slot
def get_inventory(job, key):
    return player_inventory[job][key]

#method to add items to inventory
def set_inventory(job, key, value):
    player_inventory[job][key] = value

def get_job():
    res = list(player_inventory.keys())[0]
    return res