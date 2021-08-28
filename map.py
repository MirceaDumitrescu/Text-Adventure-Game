import character as c
import screens.menu as menu

############ MAP #############


# a1---a2
#      |   |--a5   c4--c5--c6
#  b5  a3--a4       |
#   |      |--b1   c3--d1--d2
#   |      |       |
#  b4--b3--b2--c1--c2--e1--e2--e3


def player_movement(direction):
    if direction == "North":
        destination = zonemap[c.myPlayer.location]["NORTH"]
        if not zonemap[c.myPlayer.location]["NORTH"]:
<<<<<<< Updated upstream
            print("---------There is no available location in the North---------")
            wrong_direction()
        elif zonemap[destination]["LOCKED"] is False:
            print("---------[!] This area of the map is locked. [!]---------")
=======
            methods.type_text(
                "---------There is no available location in the North---------"
            )
>>>>>>> Stashed changes
            wrong_direction()
        elif zonemap[destination]["LOCKED"] == True:
            methods.type_text(
                "---------[!] This area of the map is locked. [!]---------"
            )
            unlock(destination)
        else:
            c.myPlayer.location = zonemap[c.myPlayer.location]["NORTH"]
            welcome()
    elif direction == "South":
        destination = zonemap[c.myPlayer.location]["SOUTH"]
        if not zonemap[c.myPlayer.location]["SOUTH"]:
<<<<<<< Updated upstream
            print("---------There is no available location in the South---------")
            wrong_direction()
        elif zonemap[destination]["LOCKED"] is False:
            print("---------[!] This area of the map is locked. [!]---------")
=======
            methods.type_text(
                "---------There is no available location in the South---------"
            )
>>>>>>> Stashed changes
            wrong_direction()
        elif zonemap[destination]["LOCKED"] == True:
            methods.type_text(
                "---------[!] South area of the map is locked. [!]---------"
            )
            unlock(destination)
        else:
            c.myPlayer.location = zonemap[c.myPlayer.location]["SOUTH"]
            welcome()
    elif direction == "East":
        destination = zonemap[c.myPlayer.location]["EAST"]
        if not zonemap[c.myPlayer.location]["EAST"]:
<<<<<<< Updated upstream
            print("---------There is no available location in the East---------")
            wrong_direction()
        elif zonemap[destination]["LOCKED"] is False:
            print("---------[!] This area of the map is locked. [!]---------")
=======
            methods.type_text(
                "---------There is no available location in the East---------"
            )
            wrong_direction()
        elif zonemap[destination]["LOCKED"] == True:
            methods.type_text(
                "---------[!] This area of the map is locked. [!]---------"
            )
>>>>>>> Stashed changes
            unlock(destination)
        else:
            c.myPlayer.location = zonemap[c.myPlayer.location]["EAST"]
            welcome()
    elif direction == "West":
        destination = zonemap[c.myPlayer.location]["WEST"]
        if not zonemap[c.myPlayer.location]["WEST"]:
<<<<<<< Updated upstream
            print("---------There is no available location in the West---------")
            wrong_direction()
        elif zonemap[destination]["LOCKED"] is False:
            print("---------[!] This area of the map is locked. [!]---------")
=======
            methods.type_text(
                "---------There is no available location in the West---------"
            )
>>>>>>> Stashed changes
            wrong_direction()
        elif zonemap[destination]["LOCKED"] == True:
            methods.type_text(
                "---------[!] This area of the map is locked. [!]---------"
            )
            unlock(destination)
        else:
            c.myPlayer.location = zonemap[c.myPlayer.location]["WEST"]
            welcome()


def wrong_direction():
    print(
        """
_________________________________________________________
|                       MAP MENU                         |
|                                                        |
|             Where do you want to go now?               |
|     [s] South  | [n] North | [w] West | [e] East       |
|       [b] Go back to Main Menu  | [i] Examine          |
|________________________________________________________|
    """
    )
    answer = input("> ")
    while not answer.lower() in ["s", "n", "w", "e", "b", "i"]:
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

    elif answer == "b":
        menu.game_menu()

    elif answer == "i":
        menu.examine()


def unlock(destination):
    job = c.get_job()
    print(
        '''
   ad8888888888ba
  dP'         `"8b,
  8  ,aaa,       "Y888a     ,aaaa,     ,aaa,  ,aa,
  8  8' `8           "8baaaad""""baaaad""""baad""8b
  8  8   8              """"      """"      ""    8b
  8  8, ,8         ,aaaaaaaaaaaaaaaaaaaaaaaaddddd88P
  8  `"""'       ,d8""
  Yb,         ,ad8"  
   "Y8888888888P"

  [!] Do you want to use a key and unlock the door?

                    > [yes]
                    > [no]
    '''
    )
    answer = input("> ").lower()
    while not answer in ["yes", "no"]:
        print("------Please select from the available options above------")
        answer = input("> ").lower()
    if answer == "yes":
        # check for key in inventory
        slot3 = int(c.get_inventory(job, "keys"))
        if slot3 > 0:
            new_slot = slot3 - 1
            c.set_inventory(job, "keys", new_slot)
            zonemap[destination]["LOCKED"] = False
            c.myPlayer.location = destination
            welcome()
        else:
            print("-------[!] You do not have a key to unlock this area! [!]-------")
            wrong_direction()
    elif answer == "no":
        wrong_direction()


def welcome():
    zonemap_name = zonemap[c.myPlayer.location]["NAME"]
    description = zonemap[c.myPlayer.location]["DESCRIPTION"]
    if zonemap[c.myPlayer.location]["EXAMINED"] == True:
        examination = "No, everything seems where it should be!"
    else:
        examination = "You haven't checked this place yet. You should try!"
    print(
        f"""
    
    ----------------[{zonemap_name}]---------------
    {description}
    
    Is there anything to examin here?
    > {examination}
    
    """
    )
    menu.game_menu()


zonemap = {
    "a1": {
        "NAME": "Murder Scene",
        "DESCRIPTION": """
    This is your start location. Usually nothing changes here. 
    Your apartment is as dirty as its ever been.""",
        "EXAMINED": True,
        "LOOT": [],
        "ENEMIES": [],
        "LOCKED": False,
        "NPC": [],
        "NORTH": "",
        "SOUTH": "",
        "WEST": "",
        "EAST": "a2",
    },
    "a2": {
        "NAME": "Outside of your apartment",
        "DESCRIPTION": """
    The narrow hallways of the apartment block are poor lit, 
    thus making hard to find anything or see where to go. 
    Try a couple of doors and see what happens.""",
        "EXAMINED": False,
        "LOOT": [],
        "ENEMIES": [],
        "LOCKED": False,
        "NPC": [],
        "NORTH": "",
        "SOUTH": "a3",
        "WEST": "a1",
        "EAST": "",
    },
    "a3": {
        "NAME": "Neighbour Apartment",
        "DESCRIPTION": """
    You knock on the door and the neighbour answers. 
    He seems to be startled by your knock and opens 
    the door carefully, almost as he was scared.""",
        "EXAMINED": True,
        "LOOT": [],
        "ENEMIES": [],
        "LOCKED": True,
        "NPC": [],
        "NORTH": "a2",
        "SOUTH": "",
        "WEST": "",
        "EAST": "a4",
    },
    "a4": {
        "NAME": "a4",
        "DESCRIPTION": "description",
        "EXAMINED": False,
        "LOOT": [],
        "ENEMIES": [],
        "LOCKED": False,
        "NPC": [],
        "NORTH": "a5",
        "SOUTH": "b2",
        "WEST": "a3",
        "EAST": "b1",
    },
    "a5": {
        "NAME": "a5",
        "DESCRIPTION": "description",
        "EXAMINED": False,
        "LOOT": [],
        "ENEMIES": [],
        "LOCKED": False,
        "NPC": [],
        "NORTH": "",
        "SOUTH": "a4",
        "WEST": "",
        "EAST": "",
    },
    "b1": {
        "NAME": "b1",
        "DESCRIPTION": "description",
        "EXAMINED": False,
        "LOOT": [],
        "ENEMIES": [],
        "LOCKED": False,
        "NPC": [],
        "NORTH": "",
        "SOUTH": "",
        "WEST": "a4",
        "EAST": "",
    },
    "b2": {
        "NAME": "b2",
        "DESCRIPTION": "description",
        "EXAMINED": False,
        "LOOT": [],
        "ENEMIES": [],
        "LOCKED": False,
        "NPC": [],
        "NORTH": "a4",
        "SOUTH": "",
        "WEST": "b3",
        "EAST": "c1",
    },
    "b3": {
        "NAME": "b3",
        "DESCRIPTION": "description",
        "EXAMINED": False,
        "LOOT": [],
        "ENEMIES": [],
        "LOCKED": False,
        "NPC": [],
        "NORTH": "",
        "SOUTH": "",
        "WEST": "b4",
        "EAST": "b2",
    },
    "b4": {
        "NAME": "b4",
        "DESCRIPTION": "description",
        "EXAMINED": False,
        "LOOT": [],
        "ENEMIES": [],
        "LOCKED": False,
        "NPC": [],
        "NORTH": "b5",
        "SOUTH": "",
        "WEST": "",
        "EAST": "b3",
    },
    "c1": {
        "NAME": "c1",
        "DESCRIPTION": "description",
        "EXAMINED": False,
        "LOOT": [],
        "ENEMIES": [],
        "LOCKED": False,
        "NPC": [],
        "NORTH": "",
        "SOUTH": "",
        "WEST": "b2",
        "EAST": "c2",
    },
    "c2": {
        "NAME": "c2",
        "DESCRIPTION": "description",
        "EXAMINED": False,
        "LOOT": [],
        "ENEMIES": [],
        "LOCKED": False,
        "NPC": [],
        "NORTH": "c3",
        "SOUTH": "",
        "WEST": "c1",
        "EAST": "e1",
    },
    "c3": {
        "NAME": "c3",
        "DESCRIPTION": "description",
        "EXAMINED": False,
        "LOOT": [],
        "ENEMIES": [],
        "LOCKED": False,
        "NPC": [],
        "NORTH": "c4",
        "SOUTH": "c2",
        "WEST": "",
        "EAST": "d1",
    },
    "c4": {
        "NAME": "c4",
        "DESCRIPTION": "description",
        "EXAMINED": False,
        "LOOT": [],
        "ENEMIES": [],
        "LOCKED": False,
        "NPC": [],
        "NORTH": "",
        "SOUTH": "c3",
        "WEST": "",
        "EAST": "c5",
    },
    "c5": {
        "NAME": "c5",
        "DESCRIPTION": "description",
        "EXAMINED": False,
        "LOOT": [],
        "ENEMIES": [],
        "LOCKED": False,
        "NPC": [],
        "NORTH": "",
        "SOUTH": "",
        "WEST": "c4",
        "EAST": "c6",
    },
    "c6": {
        "NAME": "c6",
        "DESCRIPTION": "description",
        "EXAMINED": False,
        "LOOT": [],
        "ENEMIES": [],
        "LOCKED": False,
        "NPC": [],
        "NORTH": "",
        "SOUTH": "",
        "WEST": "c5",
        "EAST": "",
    },
    "e1": {
        "NAME": "e1",
        "DESCRIPTION": "description",
        "EXAMINED": False,
        "LOOT": [],
        "ENEMIES": [],
        "LOCKED": False,
        "NPC": [],
        "NORTH": "",
        "SOUTH": "",
        "WEST": "c2",
        "EAST": "e2",
    },
    "e2": {
        "NAME": "e2",
        "DESCRIPTION": "description",
        "EXAMINED": False,
        "LOOT": [],
        "ENEMIES": [],
        "LOCKED": False,
        "NPC": [],
        "NORTH": "",
        "SOUTH": "",
        "WEST": "e1",
        "EAST": "e3",
    },
    "e3": {
        "NAME": "e3",
        "DESCRIPTION": "description",
        "EXAMINED": False,
        "LOOT": [],
        "ENEMIES": [],
        "LOCKED": False,
        "NPC": [],
        "NORTH": "",
        "SOUTH": "",
        "WEST": "e2",
        "EAST": "",
    },
    "d1": {
        "NAME": "d1",
        "DESCRIPTION": "description",
        "EXAMINED": False,
        "LOOT": [],
        "ENEMIES": [],
        "LOCKED": False,
        "NPC": [],
        "NORTH": "",
        "SOUTH": "",
        "WEST": "c3",
        "EAST": "d2",
    },
    "d2": {
        "NAME": "d2",
        "DESCRIPTION": "description",
        "EXAMINED": False,
        "LOOT": [],
        "ENEMIES": [],
        "LOCKED": False,
        "NPC": [],
        "NORTH": "",
        "SOUTH": "",
        "WEST": "d1",
        "EAST": "",
    },
}
