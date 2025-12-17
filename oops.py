# Class and Object

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)

# Creating object
s1 = Student("Lekhya", 21)
s1.display()
