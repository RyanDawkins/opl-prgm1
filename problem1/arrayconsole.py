from console import Console

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
