############ MAP #############


a1---a2
     |   |--a4   c4--c5--c6
 b5  a3--|       |
  |      |--b1   c3--d1--d2
  |      |       |   
 b4--b3--b2--c1--c2--e1--e2--e3

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

#Ways to navigate the maps. If North has value, [up] command will return info about the map above if locked or moved directly.
NORTH = ""
SOUTH = ""
WEST = ""
EAST = ""


#Player selects 1,2,3 or 4 from prompt menu. each value calls for player_movement("North"..etc)

### --> the method must be called with player_movement("North") or "South" or "East" or "West"

##program checks if north location is available and changes the player position if possible.

#Then calls the method to display player description welcome()
def player_movement(direction):
    if direction == "North":
        destination = zonemap[MyPlayer.location][NORTH]
        if zonemap[destination][LOCKED] is False:
            print("This area of the map is locked. Check for a key nearby.")
        else:
            MyPlayer.location = zonemap[MyPlayer.location][NORTH]
            welcome()
    elif direction == "South":
        destination = zonemap[MyPlayer.location][SOUTH]
        if zonemap[destination][LOCKED] is False:
            print("This area of the map is locked. Check for a key nearby.")
        else:
            MyPlayer.location = zonemap[MyPlayer.location][SOUTH]
            welcome()
    elif direction == "East":
        destination = zonemap[MyPlayer.location][EAST]
        if zonemap[destination][LOCKED] is False:
            print("This area of the map is locked. Check for a key nearby.")
        else:
            MyPlayer.location = zonemap[MyPlayer.location][EAST]
            welcome()
    elif direction == "West":
        destination = zonemap[MyPlayer.location][WEST]
        if zonemap[destination][LOCKED] is False:
            print("This area of the map is locked. Check for a key nearby.")
        else:
            MyPlayer.location = zonemap[MyPlayer.location][WEST]
            welcome()


def welcome():
    destination = zonemap[MyPlayer.position][DESCRIPTION]
    zonename = zonemap[MyPlayer.position][NAME]
    print("""
    
    ----------------[{zonename}]---------------
    {destination}
    
    """.format(zonename, destination))

zonemap = {
          "a1": {
          NAME: "Home",
          DESCRIPTION: "description",
          EXAMINED: True,
          LOOT: [],
          ENEMIES: [],
          LOCKED: False,
          NPC: [], 
          NORTH = ""
          SOUTH = ""
          WEST = ""
          EAST = "a2"}
}