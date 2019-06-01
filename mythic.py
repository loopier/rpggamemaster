import sys
import os

def load(filename):
    with open(filename, "r") as file:
        return file.read().split('\n')

descriptors1 = load("data/descriptors1.txt")
descriptors2 = load("data/descriptors2.txt")
actions1 = load("data/actions1.txt")
actions2 = load("data/actions2.txt")
eventfocus = load("data/eventfocus.txt")
specialelements = load("data/specialelements.txt")
characterspecialtraits = load("data/characterspecialtraits.txt") 
characteridentities = load("data/characteridentities.txt")
characterdescriptors = load("data/characterdescriptors.txt")
cthulhuoccupations = load("data/cthulhuoccupations.txt")
cthulhuelements = load("data/cthulhuelements.txt")

def do_quit(args):
    sys.exit()

def do_print(args):
    print(args)

cmds = {
        "q": do_quit,
        "print": do_print,
}

def prompt():
    inputstr = input("> ")
    cmd = inputstr.split(" ", 1)[0]
    args = " ".join(inputstr.split()[1:])

    if cmd == "quit" or cmd == "q" or cmd == "exit":
        do_quit(args)

    try:
            cmds[cmd](args)
    except:
        print(cmd, "does not exist")

    prompt()

prompt()
