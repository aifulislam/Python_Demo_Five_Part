#19/October/2020--------
#Python---Classes and Objeects----

#Iterators----------
print("Iterators-----------")
mytuple = ("Apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

#Iterators---------
print("Iterators-----------")
student = ("Arif","Tamim","Nazim")
weAre = iter(student)

print(next(weAre))
print(next(weAre))
print(next(weAre))

#Iterators---------
print("Iterators-----------")
me = ("Arif")
weAre = iter(me)

print(next(weAre))
print(next(weAre))
print(next(weAre))
print(next(weAre))

#Looping an Iterators---------
print("Looping an Iterators----------")
student = ("Arif", "Tamim", "Nazim")
for x in student:
    print(x)

#Looping an Iterators---------
print("Looping an Iterators----------")
mytuple = ("Apple", "banana", "cherry")
for x in mytuple:
    print(x)

#Looping an Iterators---------
print("Looping an Iterators----------")
mytuple = ("Ariful Islam")
for x in mytuple:
    print(x)

#Create an Iterators by function---------
print("Create an Iterators by function----------")
class MyNumbers:
    def __iter__(self):
        self.a =  1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

#Stopiteration an Iterators by function---------
print("Stopiteration an Iterators by function----------")
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)
for x in myiter:
    print(x)


#Method_Overriding-----------
print("Method_Overriding--------")
class Phone:
    def __init__(self):
        print("I am in Phone class")

class samsung(Phone):
    def __init__(self):
        super().__init__()
        print("I am in samsung class")

s = samsung()

#Method_Overriding-----------
class me:
    def __init__(self):
        print("I am Ariful Islam")

class who:
    def __init__(self):
        super().__init__()
        print("He is Tamim Iqbal")

w = who()

#A practical example of inheritance---------

class Shape:
    def __init__(self,dim1,dim2):
        self.dim1 = dim1
        self.dim2 = dim2

    def area(self):
        print("I am area method of shape class")

class Triangle(Shape):
    def area(self):
        area = 0.5 * self.dim1 * self.dim2
        print("Area of Triangle : ",area)

class Rectangle(Shape):
    def area(self):
        area = self.dim1 * self.dim2
        print("Area of Rectangle : ",area)

t1 = Triangle(20,30)
t1.area()

r1 = Rectangle(20,30)
r1.area()

#A practical example of inheritance---------
class shape:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2

    def area(self):
        print("I am in main class")

class triangle(shape):
    def area(self):
        area = 0.5 * self.num1 * self.num2
        print("Area of Triangle : ",area)

class rectangle(shape):
    def area(self):
        area = self.num1 * self.num2
        print("Area of Rectangle : ",area)

t1 = triangle(20,30)
t1.area()

r1 = rectangle(20,30)
r1.area()

