# Ryan Dawkins
# October 9th, 2014
# Programming Assignment 1

from storage import Storage
from console import Console
from structconsole import StructConsole
from arrayconsole import ArrayConsole

if __name__ == "__main__":
    Console.clear()
    Console.greet()

    # We give storage the None object because we want
    # to abstract what kind of class it is later
    storage = None
    arraysOrStructs = raw_input("Would you rather use structs or arrays? (enter s or a)\n> ")
    if arraysOrStructs == "a":
        storage = ArrayConsole()
    elif arraysOrStructs == "s":
        storage = StructConsole()
    else:
        print "Incorrect input you must enter s or a"
        sys.exit()

    while True:
        command = raw_input("user:<storage>$ ")
        storage.execute(command)
