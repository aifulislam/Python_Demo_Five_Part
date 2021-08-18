#12/October/2020--------
#Python If...Elif....Else----

a = 40
b = 30
if a > b:
    print("a greater than b")


a = 40
b = 50
if a < b:
    print("a greater than b")
else:
    print("b greater than a")


a = 60
b = 50
if a < b:
    print("b is greater than to a")
else:
    print("b is not greater than a")


a = 40
b = 40
if a > b:
    print("a greater than b")
elif a==b:
    print("a and b are equal")


a = 50
b = 60
if a > b:
    print("a greater than b")
elif a==b:
    print("a and b are equal")
else:
    print("b greater than a")


a = 60
b = 70
if a>b: print("a is greater than to b")
else:
    print("a is not greater than to b")


a = 80
b = 70
print("A") if a>b else print("B")

a = 330
b = 33
c = 500
if a > b and c > a:
    print("True")

a = 330
b = 340
c = 500
if b > a and b < c:
    print("True")
else:
    print("False")

a = 430
b = 33
c = 500
if a > b or c > a:
    print("True")
else:
    print("False")

a = 40
if a > 10:
    print("above ten")
    if a > 20:
        print("and also above 20!")
    else:
        print("but not above 20!")


a = 33
b = 200
if b > a:
    pass


