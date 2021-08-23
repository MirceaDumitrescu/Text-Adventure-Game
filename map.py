from character import Player




############ MAP #############


# a1---a2
#      |   |--a5   c4--c5--c6
#  b5  a3--a4       |
#   |      |--b1   c3--d1--d2
#   |      |       |   
#  b4--b3--b2--c1--c2--e1--e2--e3

### return upon entry
NAME = ""
DESCRIPTION = ""

### gets checked when [Examine] action triggered
EXAMINED = False

#if map has loot the Examine action collets
LOOT = []

#if map has ENEMIES the Examine action triggers enemies
ENEMIES = []

#checks before entry. Can be unlocked with key from inventory
LOCKED = False

#if NPC == True it gets triggered after Examine>Loot>Attack/etc
NPC = []

myPlayer = Player()



#Player selects 1,2,3 or 4 from prompt menu. each value calls for player_movement("North"..etc)

### --> the method must be called with player_movement("North") or "South" or "East" or "West"

##program checks if north location is available and changes the player position if possible.

#Then calls the method to display player description welcome()
def player_movement(direction):
    myPlayer = Player()
    if direction == "North":
        destination = zonemap[myPlayer.location]["NORTH"]
        if not zonemap[myPlayer.location]["NORTH"]:
            print("There is no location in the North")
        elif zonemap[destination]["LOCKED"] is False:
            print("This area of the map is locked. Check for a key nearby.")
        else:
            myPlayer.location = zonemap[myPlayer.location]["NORTH"]
            welcome()
    elif direction == "South":
        destination = zonemap[myPlayer.location]["SOUTH"]
        if not zonemap[myPlayer.location]["SOUTH"]:
            print("There is no location in the South")
        elif zonemap[destination]["LOCKED"] is False:
            print("This area of the map is locked. Check for a key nearby.")
        else:
            myPlayer.location = zonemap[myPlayer.location]["SOUTH"]
            welcome()
    elif direction == "East":
        destination = zonemap[myPlayer.location]["EAST"]
        if not zonemap[myPlayer.location]["EAST"]:
            print("There is no location in the East")
        elif zonemap[destination]["LOCKED"] is False:
            print("This area of the map is locked. Check for a key nearby.")
        else:
            myPlayer.location = zonemap[myPlayer.location]["EAST"]
            welcome()
    elif direction == "West":
        destination = zonemap[myPlayer.location]["WEST"]
        if not zonemap[myPlayer.location]["WEST"]:
            print("There is no location in the West")
        elif zonemap[destination]["LOCKED"] is False:
            print("This area of the map is locked. Check for a key nearby.")
        else:
            myPlayer.location = zonemap[myPlayer.location]["WEST"]
            welcome()


def welcome():
    destination = zonemap[myPlayer.position]["DESCRIPTION"]
    zonename = zonemap[myPlayer.position]["NAME"]
    print("""
    
    ----------------[{zonename}]---------------
    {destination}
    
    """.format(zonename, destination))

zonemap = {
            "a1": {
          "NAME": "Home",
          "DESCRIPTION": "description",
          "EXAMINED": True,
          "LOOT": [],
          "ENEMIES": [],
          "LOCKED": False,
          "NPC": [], 
          "NORTH": "",
          "SOUTH": "",
          "WEST": "",
          "EAST": "a2"},
            "a2": {
          "NAME": "a2",
          "DESCRIPTION": "description",
          "EXAMINED": True,
          "LOOT": [],
          "ENEMIES": [],
          "LOCKED": False,
          "NPC": [], 
          "NORTH": "",
          "SOUTH": "a3",
          "WEST": "a1",
          "EAST": ""},
            "a3": {
          "NAME": "a3",
          "DESCRIPTION": "description",
          "EXAMINED": True,
          "LOOT": [],
          "ENEMIES": [],
          "LOCKED": False,
          "NPC": [], 
          "NORTH": "a2",
          "SOUTH": "",
          "WEST": "",
          "EAST": "a4"},
            "a4": {
          "NAME": "a4",
          "DESCRIPTION": "description",
          "EXAMINED": True,
          "LOOT": [],
          "ENEMIES": [],
          "LOCKED": False,
          "NPC": [], 
          "NORTH": "a5",
          "SOUTH": "b2",
          "WEST": "a3",
          "EAST": "b1"},
            "a5": {
          "NAME": "a5",
          "DESCRIPTION": "description",
          "EXAMINED": True,
          "LOOT": [],
          "ENEMIES": [],
          "LOCKED": False,
          "NPC": [], 
          "NORTH": "",
          "SOUTH": "a4",
          "WEST": "",
          "EAST": ""},
            "b1": {
          "NAME": "b1",
          "DESCRIPTION": "description",
          "EXAMINED": True,
          "LOOT": [],
          "ENEMIES": [],
          "LOCKED": False,
          "NPC": [], 
          "NORTH": "",
          "SOUTH": "",
          "WEST": "a4",
          "EAST": ""},
            "b2": {
          "NAME": "b2",
          "DESCRIPTION": "description",
          "EXAMINED": True,
          "LOOT": [],
          "ENEMIES": [],
          "LOCKED": False,
          "NPC": [], 
          "NORTH": "a4",
          "SOUTH": "",
          "WEST": "b3",
          "EAST": "c1"},
            "b3": {
          "NAME": "b3",
          "DESCRIPTION": "description",
          "EXAMINED": True,
          "LOOT": [],
          "ENEMIES": [],
          "LOCKED": False,
          "NPC": [], 
          "NORTH": "",
          "SOUTH": "",
          "WEST": "b4",
          "EAST": "b2"},
            "b4": {
          "NAME": "b4",
          "DESCRIPTION": "description",
          "EXAMINED": True,
          "LOOT": [],
          "ENEMIES": [],
          "LOCKED": False,
          "NPC": [], 
          "NORTH": "b5",
          "SOUTH": "",
          "WEST": "",
          "EAST": "b3"},
            "c1": {
          "NAME": "c1",
          "DESCRIPTION": "description",
          "EXAMINED": True,
          "LOOT": [],
          "ENEMIES": [],
          "LOCKED": False,
          "NPC": [], 
          "NORTH": "",
          "SOUTH": "",
          "WEST": "b2",
          "EAST": "c2"},
            "c2": {
          "NAME": "c2",
          "DESCRIPTION": "description",
          "EXAMINED": True,
          "LOOT": [],
          "ENEMIES": [],
          "LOCKED": False,
          "NPC": [], 
          "NORTH": "c3",
          "SOUTH": "",
          "WEST": "c1",
          "EAST": "e1"},
            "c3": {
          "NAME": "c3",
          "DESCRIPTION": "description",
          "EXAMINED": True,
          "LOOT": [],
          "ENEMIES": [],
          "LOCKED": False,
          "NPC": [], 
          "NORTH": "c4",
          "SOUTH": "c2",
          "WEST": "",
          "EAST": "d1"},
            "c4": {
          "NAME": "c4",
          "DESCRIPTION": "description",
          "EXAMINED": True,
          "LOOT": [],
          "ENEMIES": [],
          "LOCKED": False,
          "NPC": [], 
          "NORTH": "",
          "SOUTH": "c3",
          "WEST": "",
          "EAST": "c5"},
            "c5": {
          "NAME": "c5",
          "DESCRIPTION": "description",
          "EXAMINED": True,
          "LOOT": [],
          "ENEMIES": [],
          "LOCKED": False,
          "NPC": [], 
          "NORTH": "",
          "SOUTH": "",
          "WEST": "c4",
          "EAST": "c6"},
            "c6": {
          "NAME": "c6",
          "DESCRIPTION": "description",
          "EXAMINED": True,
          "LOOT": [],
          "ENEMIES": [],
          "LOCKED": False,
          "NPC": [], 
          "NORTH": "",
          "SOUTH": "",
          "WEST": "c5",
          "EAST": ""},
            "e1": {
          "NAME": "e1",
          "DESCRIPTION": "description",
          "EXAMINED": True,
          "LOOT": [],
          "ENEMIES": [],
          "LOCKED": False,
          "NPC": [], 
          "NORTH": "",
          "SOUTH": "",
          "WEST": "c2",
          "EAST": "e2"},
            "e2": {
          "NAME": "e2",
          "DESCRIPTION": "description",
          "EXAMINED": True,
          "LOOT": [],
          "ENEMIES": [],
          "LOCKED": False,
          "NPC": [], 
          "NORTH": "",
          "SOUTH": "",
          "WEST": "e1",
          "EAST": "e3"},
            "e3": {
          "NAME": "e3",
          "DESCRIPTION": "description",
          "EXAMINED": True,
          "LOOT": [],
          "ENEMIES": [],
          "LOCKED": False,
          "NPC": [], 
          "NORTH": "",
          "SOUTH": "",
          "WEST": "e2",
          "EAST": ""},
            "d1": {
          "NAME": "d1",
          "DESCRIPTION": "description",
          "EXAMINED": True,
          "LOOT": [],
          "ENEMIES": [],
          "LOCKED": False,
          "NPC": [], 
          "NORTH": "",
          "SOUTH": "",
          "WEST": "c3",
          "EAST": "d2"},
            "d2": {
          "NAME": "d2",
          "DESCRIPTION": "description",
          "EXAMINED": True,
          "LOOT": [],
          "ENEMIES": [],
          "LOCKED": False,
          "NPC": [], 
          "NORTH": "",
          "SOUTH": "",
          "WEST": "d1",
          "EAST": ""},
}
