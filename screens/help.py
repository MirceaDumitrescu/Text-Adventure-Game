from methods import cls, type_text, loading, loads
import screens.menu as menu

def help_game():
    cls()
    help_info = """

 ____  ____  ________  _____     _______   
|_   ||   _||_   __  ||_   _|   |_   __ \  
  | |__| |    | |_ \_|  | |       | |__) | 
  |  __  |    |  _| _   | |   _   |  ___/  
 _| |  | |_  _| |__/ | _| |__/ | _| |_     
|____||____||________||________||_____|    
                                           
                              
Discover the mistery behind the murder of Ardit, 
the scientist. Ardit was the brother of the Medic, 
lover of the Police officer and best friend of the Tehnician. 
Embark into this mistery from all three perspectives 
and see if you can find out who murdered Ardit.

        _________________________________________    
        |          AVAILABLE COMMANDS           |
        ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
  During any interaction the game will ask for your input 
  in the from of a number which coresponds to one of the  
             options provided by the game.
  Make sure to type a valid answer to continue the game.

        _________________________________________    
        |        ABOUT MAP & LOCATIONS          |
        ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
     Some rooms or locations are locked by default. 
     You can use keys from your inventory to unlock 
      them or solve the puzzle from that location.

        _________________________________________    
        |         HOW TO BEAT THE GAME?         |
        ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
   Once you reach the last room and solve the puzzle 
        (without getting killed in the process) 
              you will finish the game.
"""
    type_text(help_info)
    loading(5, loads)
    menu.game_menu()