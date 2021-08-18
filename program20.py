#20/October/2020--------
#Python---Classes and Objeects----
#Scope----------
#Local Scope-------

def myfunction():
    x = 300
    print(x)

myfunction()

#Local Scope-------
def myfunction():
    x = 200
    return x
y = myfunction()
print(y)

#local scope--------
#Function Inside Funtction---
def myfunction():
    x = 300
    def myinnerfunc():
        print(x)
    myinnerfunc()

myfunction()

#Globa scope---------
x = 300
def myfunction():
    print(x)

myfunction()
print(x)

#Globa scope---------
#Naming Variables------
x = 300
def myfunction():
    x = 200
    print(x)

myfunction()
print(x)

#Global Keyword------
def myfunction():
    global x
    x = 300

myfunction()
print(x)

#Global Keyword------
x = 300
def myfunction():
    global x
    x = 200

myfunction()
print(x)

#Global Keyword------
y = 300
def myfunction():
    global x
    x = 200

myfunction()
print(y)

