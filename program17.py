#17/October/2020--------
#Python---Classes and Objeects----

class MyClass:
    x = 5

print(MyClass)

#Create Object--------
class MyClass:
    x = 5

p1 = MyClass()
print(p1.x)

#Create Object--------
class MyClass():
    x = 5 + 5

p1 = MyClass()
print(p1.x)

#The __init__()Function-----
class person():
    def __init__(self,name,age):
        self.name = name
        self.age = age

p1 = person("Arif", 25)
print(p1.name)
print(p1.age)

#The __init__()Function-----
class car:
    def __init__(self,name,prise):
        self.name = name
        self.prise = prise
c1 = car("Bmw","$1000")
print(c1.name)
print(c1.prise)

#Object Methoods-----
class car:
    def __init__(self,name,prise):
        self.name = name
        self.prise = prise
    def myfunction(self):
        print("Car name is "+self.name)

    def myfunction2(self):
        print("Car prise is "+self.prise)

c1 = car("Bmw","$5000")
c1.myfunction()
c1.myfunction2()

#The self  Patrameter-------------
class car:
    def __init__(myselfobject,name,prise):
        myselfobject.name = name
        myselfobject.prise = prise
    def myfunction(self):
        print("Car name is "+self.name)

    def myfunction2(self):
        print("Car prise is "+self.prise)

c1 = car("Bmw","$5000")
c1.myfunction()
c1.myfunction2()

#Modify Object Properties-----
class car:
    def __init__(self,name,prise):
        self.name = name
        self.prise = prise
    def myfunction(self):
        print("Car name is "+self.name)

c1 = car("Bmw","$50000")
c1.name = "Honda"
print(c1.name)
c1.prise = 1000000
print(c1.prise)

#Delete Object Properties-----
#del ---
#pass---
class car:
    pass


#Introduction to OOP - class and object-----
print("Introduction to OOP - class and object------")
class Student:
    roll = ""
    gpa = ""

Tamim = Student()
print(isinstance(Tamim,Student))
Tamim.roll = 101
Tamim.gpa = 4.50
print(f"Roll : {Tamim.roll}, Gpa: {Tamim.gpa}")

#Introduction to OOP - class and object--------
print("Introduction to OOP - class and object------")
class car:
    name = ""
    color = ""

Bmw = car()
Bmw.name = "Bmw"
Bmw.color = "Red"
print(f"Name: {Bmw.name}, Color: {Bmw.color}")

Ford = car()
Ford.name = "Ford"
Ford.color = "Black"
print(f"Name: {Ford.name}, Color: {Ford.color}")

#Introducing Methods----------
print("Introducing Methods------")
class car:
    name = ""
    color = ""

    def display(self):
        print(f"Name: {self.name}, Color: {self.color}")

Bmw = car()
Bmw.name = "Bmw"
Bmw.color = "Red"
Bmw.display()

Ford = car()
Ford.name = "Ford"
Ford.color = "Black"
Ford.display()

#Introducing Methods------
print("Introducing Methods------")
class car:
    name = ""
    color = ""
    def set_value(self,name,color):
        self.name = name
        self.color = color

    def display(self):
        print(f"Name: {self.name}, Color: {self.color}")
Bmw = car()
Bmw.set_value("Bmw","Red")
Bmw.display()

Ford = car()
Ford.set_value("Ford","Black")
Ford.display()

#Introducing Methods------
print("Introducing Methods------")
class Student:
    name = ""
    roll = ""
    gpa = ""

    def set_value(self,name,roll,gpa):
        self.name = name
        self.roll = roll
        self.gpa = gpa

    def display(self):
        print(f"Name: {self.name}, Roll : {self.roll}, Gpa: {self.gpa}")

Arif = Student()
Arif.set_value("Arif",101,4.50)
Arif.display()

Tamim = Student()
Tamim.set_value("Tamim",102,4.30)
Tamim.display()

Nazim = Student()
Nazim.set_value("Nazim",103,4.00)
Nazim.display()

#Constructor----1------
print("Constructor---1---")
class car:
    name = ""
    color = ""
    madein = ""
    def __init__(self,name,color,madein):
        self.name = name
        self.color = color
        self.madein = madein

    def display(self):
        print(f"Name: {self.name}, Color: {self.color}, Color: {self.madein}")

Bmw = car("Bmw","Red","German")
Bmw.display()

Ford = car("Ford","Black","USA")
Ford.display()

#Constructor---2-------
print("Constructor---2---")
class car:
    name = ""
    color = ""
    def __init__(self,name,color):
        self.name = name
        self.color = color

    def display(self):
        print(f"Name: {self.name}, Color: {self.color}")

Bmw = car("Bmw","Red")
Bmw.display()

Ford = car("Ford","Black")
Ford.display()

#Exercise--trangle----------
print("Area of Triangle:----------")
class Triangle:
    def __init__(self,base,height):
        self.base = base
        self.height = height

    def calculate_area(self):
        area = 0.5 * self.base * self.height
        print("Area of Triangle: ",area)

t1 = Triangle(10,20)
t1.calculate_area()

t1 = Triangle(20,30)
t1.calculate_area()

#Exercise--Rectangle----------
print("Area of Rectangle:----------")
class rectangle:
    def __init__(self,base,height):
        self.base = base
        self.height = height

    def calculate_area(self):
        area = self.base * self.height
        print("Area of Rectangle: ",area)

r1 = rectangle(10,20)
r1.calculate_area()

r2 = rectangle(20,30)
r2.calculate_area()

