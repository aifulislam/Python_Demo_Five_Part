#16/October/2020--------
#Python---Function----

def my_function():
    print("Hello from a function")

my_function()

#Using Arguments--------
def my_function(fname):
    print(fname + " Refsnes")

my_function("Email")
my_function("Lobias")
my_function("Linus")

#number of Arguments-----
def my_function(fname,lname):
    print (fname + " " + lname)

my_function("Ariful","Islam")

#----------
def my_function(fname,lname):
    print (fname + " Alex " + lname)

my_function("Evan","Arif")

# *args----------
def my_function(*name):
    print(name[1] + " I am a student  " )

my_function("Evan", "Alex", "Arif")

#Keyword Arguments----------
def my_function(child1,child2,child3):
    print("I am a student in " +child1)

my_function(child1= "CSC",child2= "MSS",child3= "CSS")

#Keyword Arguments----2------
def my_function(child1,child2,child3):
    print("I am " + child2)

my_function(child1= "Evan", child2= "Alex", child3= "Arif")

#Arbitary Keyword Arguments---**Keyargs-------
def my_function(**kid):
    print("His last name is " +kid["lname"])

my_function(fname = "Ariful", lname= "Islam")

#Defult Parametter Value--------
def my_function(country = "Schengen Country_26"):
    print("I want to go " + country)

print("My favourite Countrys for Job---")
my_function("US")
my_function("CN")
my_function("NZ")
my_function("AU")
my_function("UK")
my_function()

#Passing a list as an Arguments--------
def my_function(food):
    for x  in food:
        print(x)

fruites = ["Apple", "Banana", "Orange"]

my_function(fruites)


# Passing a list as an Arguments--------
def my_function(car):
    for x in car:
        print(x)


car_bus = ["Honda", "BMW", "Toyata"]

my_function(car_bus)

#Return Values--------
def my_function(x):
    return 5 * x

print(my_function(3))
print(my_function(4))
print(my_function(5))
print(my_function(6))

#Return Values--------
def my_function(x):
    return 6 / x

print(my_function(2))

#Pass--------
def my_function():
    pass

#Recursion---------
def tri_recursion(k):
    if (k > 0 ):
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result
print("\n \n Rrcursion Example ---------")
tri_recursion(6)

