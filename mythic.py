import sys
import os
from random import randint

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
defaultroll = "1d100"

def intInput(prompt="Enter a number\n"):
    return int(input(prompt))

def roll(prompt="Enter result or press ENTER\n"):
    try:
        return intInput(defaultroll+" "+prompt)
    except ValueError:
        print("Rolling", defaultroll, "for you")
        return do_roll(defaultroll)

# Roll on a table and get the result
def getTableResult(table):
    # print(result)
    return table[roll()]

def do_quit(args):
    sys.exit()

def do_print(args):
    print(args)

def do_printCommands(args):
    msg = ""
    for cmd in cmds.keys():
        msg += "["
        msg += cmd
        msg += "]"
    print(msg)

def do_roll(args):
    roll = args
    if len(roll) == 0:
        roll = defaultroll
        
    dice = {
        "1d10": randint(1,10),
        "1d100": randint(1,100),
    }
    result = dice[roll]
    print(roll, "result:", result)
    return result

def do_actions(args):
    actions = getTableResult(actions1), getTableResult(actions2)
    print("Actions:", actions)

def do_descriptors(args):
    descriptors = getTableResult(descriptors1), getTableResult(descriptors2)  
    print("Descriptors:", descriptors)

def do_eventfocus(args):
    eventfocusresult = getTableResult(eventfocus)
    print("Event Focus:", eventfocusresult)

def do_specialelements(args):
    specialelementsresult = getTableResult(specialelements)
    print(specialelementsresult)

def do_characterspecialtraits(args):
    characterspecialtraitsresult = getTableResult(characterspecialtraits)
    print("Character Special Traits:", characterspecialtraitsresult)

def do_characteridentities(args):
    characteridentitiesresults = getTableResult(characteridentities)
    print("Character Identity:",  characteridentitiesresults)

def do_characterdescriptors(args):
    characterdescritporsresults = getTableResult(characterdescriptors)
    print("Character Description:", characterdescritporsresults)

def do_cthulhuoccupations(args):
    cthulhuoccupationsresults = getTableResult(cthulhuoccupations)
    print("Cthulhu Occupation:", cthulhuoccupationsresults)

def do_cthulhuelements(args):
    cthulhuelementsresults = getTableResult(cthulhuelements)
    print("Cthulhu Element:", cthulhuelementsresults)


# TODO: Add descriptions. "q": {"cmd": do_cmd, "description": "blablabla"}
cmds = {
        "q": do_quit,
        "quit": do_quit,
        "exit": do_quit,
        "print": do_print,
        "actions": do_actions,
        "a": do_actions,
        "description": do_descriptors,
        "d": do_descriptors,
        "eventfocus": do_eventfocus,
        "ef": do_eventfocus,
        "specialelement": do_specialelements,
        "se": do_specialelements,
        "characterspecialtraits": do_characterspecialtraits,
        "cst": do_specialelements,
        "characterdescription": do_characterdescriptors,
        "cd": do_characterdescriptors,
        "cthulhuoccupations": do_cthulhuoccupations,
        "co": do_cthulhuoccupations,
        "cthulhuelements": do_cthulhuelements,
        "ce": do_cthulhuelements,
        "roll": do_roll,
        "r": do_roll,
        "help": do_printCommands,
        "h": do_printCommands,
}

def prompt():
    inputstr = input("> ")
    cmd = inputstr.strip().split(" ", 1)[0]
    args = " ".join(inputstr.split()[1:])

    try:
        cmds[cmd](args)
    except KeyError:
        print(cmd, "does not exist")

    prompt()

prompt()
