#30/October/2020--------
#Python---Classes and Objeects----
#Polymorphism------------

#Bilt in Polymorphic function-----
print(len("Ariful Islam"))
print(len([10,20,30]))

#User Difined Polymorphic function-----
def add(x, y , z =0):
    return x + y + z

print(add(10,20))
print(add(10,20,30))

#24/October/2020--------
#Python---Classes and Objeects----
#Magic method------------

class bike:
    def __init__(self,name,color):
        self.name = name
        self.color = color

    def __le__(self, other):
        return self.name <= other.name and self.color <= other.color

    def __ge__(self, other):
        return self.name >= other.name and self.color >= other.color

    def __ne__(self, other):
        return self.name != other.name and self.color != other.color

    def __eq__(self, other):
        return self.name == other.name and self.color == other.color

    def __str__(self):
        return (f"Name : {self.name}, Color : {self.color}")

    def display(self):
        print(f"Name : {self.name}, Color : {self.color}")

bike1 = bike("Yamaha R15","Blue")
bike2 = bike("Yamaha FZ","Red")
print(bike)
print(bike1)
print(bike2)
print(bike1 == bike2)
print(bike1 != bike2)
print(bike1 >= bike2)

#Creating your own Module-----------

from math import *
print(pow(2,3))
print(pi)

from module import triangle_area,rectangle_area

triangle_area(10,20)
rectangle_area(10,20)

