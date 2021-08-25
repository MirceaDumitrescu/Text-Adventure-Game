import sys
import time
import os
import math
import json


def cls():
    os.system('cls' if os.name=='nt' else 'clear')

##### Define Function to type words slowly
def type_text(txt):
    i = 0
    speed = 6
    #This to write {speed} chars at once since the limitation of float number is 10^-9 aka, 
    #if the time.sleep is not fast/slow enought
    while i < len(txt):
        delta = len(txt) - i - speed
        if delta <= 0:
            speed = speed - abs(delta) #Prevent out of range
        for b in range(0, speed):
            sys.stdout.write(txt[i + b])
            sys.stdout.flush()
        time.sleep(math.pow(10, -3)) #delay between when the chars are written
        i += speed

def loading(delay: int, text: str):
    #Length should be divisable to delay, if not, 
    # you can add blank spaces to the begining and the end of the variable to make it divisable
    if len(text) % delay != 0:
        raise ValueError('Text length must be divisable to delay')

    i = 0
    t = 0
    while t <= delay:
        delta = int(len(text) / delay)
        n = i + delta
        sys.stdout.write(text[i:n])
        sys.stdout.flush()
        i = n
        t += 1
        if t != delay: time.sleep(1)

def read(file: str):
    return json.load(open(file))
def write(file: str, data: dict):
    with open(file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

starting_kits = {
            "MEDIC": {
                "POTIONS": 3,
                "BULLETS": 1,
                "KEYS": 1,
                "CLUES": 0,
                "LETTERS": 0,
                "FOOD": 0 },
            "POLICE": {
                "POTIONS": 1,
                "BULLETS": 3,
                "KEYS": 1,
                "CLUES": 0,
                "LETTERS": 0,
                "FOOD": 0 },
            "TEHNICIAN": {
                "POTIONS": 1,
                "BULLETS": 1,
                "KEYS": 3,
                "CLUES": 0,
                "LETTERS": 0,
                "FOOD": 0 }
                }


loads = "Loading [▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰] 100%"

