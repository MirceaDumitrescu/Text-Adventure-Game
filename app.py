import sys
import time
import os

##### Importing method from methods.py (all methods must be stored there or other files, not here)
from methods import type_sys_text
from methods import get_inventory
from methods import setup_game
from help import help
from text_input import text_input
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
                        [2] Help <
                        [3] Quit <
"""

##### Calling out the function from methods.py to type the welcome message when program run
type_sys_text(welcome)
# 
menu = {"1": setup_game,
        "2": get_inventory,
        "3": sys.exit
       }
text_input("> ", menu)
# get_inventory()
