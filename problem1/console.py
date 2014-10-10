# Ryan Dawkins
# October 9th, 2014
# Programming Assignment 1

import os
import sys
from storage import Storage

# This is our base class that has the console related functions such as
# receiving input, greeting, and executing commands.
class Console(Storage):

    # Greeting message
    @staticmethod
    def greet():
        print "============================================"
        print "Welcome to the most advanced student manager"
        print "============================================"
        print
        print "Type help to see what commands you can run."
        print

    # Clears the console
    @staticmethod
    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')

    # These methods are how we get information from the user
    # we also strip the data in case anyone types a space.
    def get_name(self):
        return raw_input("Enter a name:\t").strip()
    def get_age(self):
        return raw_input("Enter an age:\t").strip()
    def get_gpa(self):
        return raw_input("Enter a gpa:\t").strip()
    def get_grade(self):
        return raw_input("Enter a grade:\t").strip()

    # This function receives a string and
    def execute(self, command):

        # Stripping the command of spaces since we don't care
        # about the left or right spacing.
        command.strip()

        # I think this is self documenting, but it interprets the commands given
        if command == "clear":
            self.clear()
        elif command == "exit":
            sys.exit()
        elif command == "add":
            name = self.get_name()
            age = self.get_age()
            gpa = self.get_gpa()
            grade = self.get_grade()
            self.store(name, age, gpa, grade)
        elif command == "del":
            self.delete(raw_input("Enter the name of who you would to delete:\t"))
        elif command == "list":
            print "=========="
            print " Students "
            print "=========="
            self.list()
        elif command == "help":
            print "Commands:"
            print "\tclear\tClears the console"
            print "\texit \tExits the console"
            print "\tadd  \tAdds a student to the program in memory"
            print "\tdel  \tPrompts you to enter a name to delete"
            print "\tlist \tLists all students stored"
        else:
            print "We don't know that command, type help to see a list of commands"
