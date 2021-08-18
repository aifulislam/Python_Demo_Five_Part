#14/October/2020--------
#Python---Lambda-----

x = lambda  a: a + 10
print(x(5))

a = lambda x : x - 10
print(a(20))

x = lambda a, b: a * b
print(x(5,6))

x = lambda a,b : a / b
print(x(6, 3))

x = lambda a, b,c: a + b + c
print(x(2,3,4))

x = lambda a, b,c: a * b * c
print(x(2,3,4))

def myfunc(n):
    return lambda a : a * n
mydoubler = myfunc(2)

print(mydoubler(11))

def cube(n):
    return lambda a : a*a*a
sumofcube = cube(2)

print(sumofcube(10))

def myfunc(n):
    return lambda a: a * n
qube = myfunc(2)
qube1 = myfunc(3)

print(qube(10))
print(qube1(20))

def myfunc(n):
    return lambda a : a - n
myminus = myfunc(10)
myminus1 = myfunc(100)

print(myminus(20))
print(myminus1(200))

