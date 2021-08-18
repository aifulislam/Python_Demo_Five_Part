#06/October/2020--------
#Python Booleans-------
#True or False--------

print(10>9)
print(10==9)
print(10<9)

a = 80
b = 133
if a > b:
    print("a is greater than b.")
else:
    print("b is greater than a.")

print(bool("Hello"))
print(bool(15))

x = "Hello"
y = 15
print(bool(x))
print(bool(y))

print(bool("abc"))
print(bool(123))
print(bool(["Apple","banana","orange"]))

#False-----
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool({}))
print(bool([]))

class myclass():
    def __len__(self):
        return True
        #return False
        #return 0
        #return 1

myobj = myclass()
print(bool(myobj))

def myFunction():
    return True

if myFunction():
    print("Yes!")
else:
    print("No!")

x = 100
print(isinstance(x, int))

x = 100.50
print(isinstance(x, float))
