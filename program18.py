#18/October/2020--------
#Python---Classes and Objeects----
#Inheritance----------
#Parent class---
#Child class---

#Create a Parant Class-----
class Person:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname

    def printname(self):
        print(self.fname, self.lname)

x = Person("Ariful", "Islam")
x.printname()

#Create a Parant Class-----
class student:
    def __init__(self,name,class1):
        self.name = name
        self.class1 = class1

    def printname(self):
        print(self.name, self.class1)

y1 = student("Arif","MA")
y1.printname()

#Create a Child Class-----
class student:
    def __init__(self,name,class1):
        self.name = name
        self.class1 = class1

    def printname(self):
        print(self.name, self.class1)
class Studenthere(student):
        pass
y1 = student("Arif","MA")
y1.printname()

#Add the __init__()-----
class Person:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname

    def printname(self):
        print(self.fname, self.lname)

class Student(Person):
    def __init__(self,fname,lname):
        Person.__init__(self,fname,lname)

x = Person("Ariful", "Islam")
x.printname()

'''
#Use the super()-----
class Person:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname

    def printname(self):
        print(self.fname, self.lname)

class Student(Person):
    def __init__(self,fname,lname):
        super().__init__(self,fname,lname)

x = Person("Ariful", "Islam")
x.printname()

#Add Properties-----
class Person:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname

    def printname(self):
        print(self.fname, self.lname)

class Student(Person):
    def __init__(self,fname,lname):
        super().__init__(self, fname, lname)
        self.graduationyear = 2019

x = Student("Ariful", "Islam")
print(x.graduationyear)
'''

#Inheritance------
#Parent, Super, Base Class--------
#Child, Sub, Derived Class--------
class Phone:
    def call(self):
        print("You can call")
    def message(self):
        print("You can message")

class Samsang(Phone):
    def photos(self):
        print("You can photos")

s = Samsang()
s.call()
s.message()
s.photos()
print(issubclass(Samsang,Phone))

#Inheritance------
class car:
    def name(self):
        print("It is Bmw")
    def Clour(self):
        print("It is red")

class bus(car):
    def price(self):
        print("It has bought $50000.")

c = bus()
c.name()
c.Clour()
c.price()
print(issubclass(bus,car))


#Types Of Inheritance-----------
#Multilavel Inheritance------

print("Multilavel Inheritance------")
class a():
    def display1(self):
        print("I am in a class")

class b(a):
    def display2(self):
        print("I am in b class")

class c(b):
    def display3(self):
        super().display1()
        super().display2()
        print("I am in c class")

obj1 = c()
obj1.display3()

#Multiple Inheritance------

print("Multiple Inheritance------")
class a:
    def display(self):
        print("I am in a class")

class b:
    def display(self):
        print("I am in b class")

class c(a,b):
    pass

obj1 = c()
obj1.display()

