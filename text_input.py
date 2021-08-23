# Choices dict should be in the following format
#   prompt: The choice the user made
#   choices: A dictionary of functions in the following format:
#               menu = {"1":my_play_fn,
#                       "2":my_quit_fn }

def text_input(prompt: str, choices: dict):
  player_input = input(prompt)
  if player_input in choices.keys():
    res = choices[player_input]()
    return res
  else:
    print("""
      -------[Please choose a valid option]-------
    The valid options are displayed above this error
    """)
    player_input = input(prompt)
    if player_input in choices.keys():
        res = choices[player_input]()
        return res
    else:
      print("""
      
   _____                         ____                 _ 
  / ____|                       / __ \               | |
 | |  __  __ _ _ __ ___   ___  | |  | |_   _____ _ __| |
 | | |_ |/ _` | '_ ` _ \ / _ \ | |  | \ \ / / _ \ '__| |
 | |__| | (_| | | | | | |  __/ | |__| |\ V /  __/ |  |_|
  \_____|\__,_|_| |_| |_|\___|  \____/  \_/ \___|_|  (_)
 =======================================================
                    Please try again !
      """)




#
#   player_input = input(prompt)
#   res = choices[player_input]()
#   return res
