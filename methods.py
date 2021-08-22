import sys
import time
import os

##### Defined Function to type words slowly
def type_sys_text(i):
    for char in i:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.003)
    player_input = input("> ")
    os.system("clear")