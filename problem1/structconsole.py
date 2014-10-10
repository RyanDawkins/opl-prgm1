# Ryan Dawkins
# October 9th, 2014
# Programming Assignment 1

from console import Console
from student import Student

class StructConsole(Console):

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
