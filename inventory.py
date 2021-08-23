# Create an inventory dictionary with maximum 6 slots
player_inventory = {
                "slot1": "0", #for potions only
                "slot2": "0", #for bullets only
                "slot3": "0", #for keys only
                "slot4": "0", #for letters only
                "slot5": "0", #for clues only
                "slot6": "0" } #for food only
                
#method to get item in slot
def get_inventory(key):
    return player_inventory[key]

#method to add items to inventory
def add_inventory(key, value):
    player_inventory[key] = value