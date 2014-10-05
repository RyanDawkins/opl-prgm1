import os
import sys

# This class is abstracted for later implementation
class Storage(object):
    # We are forcing the implementation of these methods so that we can
    # call them later on in the console class using the execute method.
    def store(self, name, age, gpa, grade):
        raise NotImplementedError( "Should have implemented this" )
    def delete(self, name):
        raise NotImplementedError( "Should have implemented this" )
    def list(self):
        raise NotImplementedError( "Should have implemented this" )

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

class StructConsole(Console):#, Storage):

    # Initializes the program with structs
    def __init__(self):
        self.students = []

    # Method to deal with storage
    def store(self, name, age, gpa, grade):
        student = Student()
        student.name = name
        student.age = age
        student.gpa = gpa
        student.grade = grade
        self.students.append(student)

    # This method deletes a student by a string
    def delete(self, name):
        for i in range(len(self.students)):
            if(self.students[i].name == name):
                del self.students[i]
                return
        print "Student", name, "not found."

    # Lists all students
    def list(self):
        for s in self.students:
            print "Student: "+s.name
            print "  Age:   "+s.age
            print "  GPA:   "+s.gpa
            print "  Grade: "+s.grade

class ArrayConsole(Console):

    # Creating all of our arrays to store information
    def __init__(self):
        self.names = []
        self.ages = []
        self.gpas = []
        self.grades = []

    # Method to deal with storage
    def store(self, name, age, gpa, grade):
        self.names.append(name)
        self.ages.append(age)
        self.gpas.append(gpa)
        self.grades.append(grade)

    # Deletes an item by it's name
    def delete(self, name):
        key = -1
        for i in range(len(self.names)):
            if self.names[i] == name:
                del self.names[key]
                del self.ages[key]
                del self.gpas[key]
                del self.grades[key]
                return
        print "Student", name, "not found."

    # Prints out all of the students
    def list(self):
        for i in range(len(self.names)):
            print "Student: "+ self.names[i]
            print "  Age:   "+self.ages[i]
            print "  GPA:   "+self.gpas[i]
            print "  Grade: "+self.grades[i]

# Base student class for storing information
class Student:
    def __init__(self):
        self.name = None
        self.age = 0
        self.gpa = 0.0
        self.grade = None

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
