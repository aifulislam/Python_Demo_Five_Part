#01/October/2020--------
#Syntex,Comments,variables----------
#Correct variables-----

myname = "Arif"
my_name = "Arif"
_my_name = "Arif"
myName = "Arif"
MYNAME = "Arif"
myname1 = "Arif"


x = 5
y = "Arif"
print(x)
print(y)

a = 5
a = "Arif"
print(a)

x,y,z = "Arif", "Tamim" , "Nazim"
print(x)
print(y)
print(z)

x = y = z = "Arif"
print(x)
print(y)
print(z)

x = "Best"
y = "program"
print("Python is "+ x + " " + y)

x = "python is "
y = "program"
z = x + y
print(z)

x = 5
y = 10
z = x + y
print(z)

x = 5
y = 10
print(x + y)

x = "Arif"
def myfunc():
    print("I am "+ x)

myfunc()

x = "Arif"
def myfunc():
    x = "Tamim"
    print("I am "+ x)

myfunc()
print("I am "+ x)

def myfunc():
    global x
    x = "Arif"

myfunc()
print("I am "+ x)

x = "Tamim"
def myfunc():
    global x
    x = "Arif"

myfunc()
print("I am "+ x)

