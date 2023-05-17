import keyboard
import time
import sys

x = 0

def mywait():
    keyboard.read_key()

def acabar():

    x + 1
    quit()

def my_function():
    
    while x < 1 :
        print("1")
        time.sleep(1)


keyboard.add_hotkey('h', my_function)

keyboard.add_hotkey('esc', acabar)

while True:
    mywait()