# Python OOPS - 4 Pillars (Beginner Friendly)

# -------- 1. ENCAPSULATION --------
# Wrapping data and methods inside a class

class Student:
    def __init__(self, name, age):
        self.name = name        # public variable
        self.__marks = 90       # private variable

    def show_details(self):
        print("Name:", self.name)
        print("Marks:", self.__marks)

s1 = Student("Lekhya", 21)
s1.show_details()

# -------- 2. INHERITANCE --------
# One class acquires properties of another class

class Person:
    def display_person(self):
        print("I am a person")

class Teacher(Person):   # Teacher inherits Person
    def display_teacher(self):
        print("I am a teacher")

t1 = Teacher()
t1.display_person()      # Parent class method
t1.display_teacher()

# -------- 3. POLYMORPHISM --------
# Same method name, different behavior

class Bird:
    def sound(self):
        print("Bird makes sound")

class Dog:
    def sound(self):
        print("Dog barks")

b = Bird()
d = Dog()

b.sound()
d.sound()

# -------- 4. ABSTRACTION --------
# Hiding implementation details

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car starts with key")

c = Car()
c.start()
