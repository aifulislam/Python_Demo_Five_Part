#15/October/2020--------
#Python---Array----
#append(), clear(), copy(), count(), extend(),index(),
#insert(), pop(), remove(), reverse(), sort()--------

cars = ["Ford", "BMW", "Volvo"]
print(cars)

cars = ["Ford", "BMW", "Volvo"]
print(cars[1])

cars = ["Ford", "BMW", "Volvo"]
x = cars[2]
print(x)

cars = ["Ford", "BMW", "Volvo"]
cars[2] = "Toyata"
print(cars)

#Len()----
cars = ["Ford", "BMW", "Volvo"]
x = len(cars)
print(x)

#Looping Array Elements----for in---
cars = ["Ford", "BMW", "Volvo", "Toyata"]
for x in cars:
    print(x)

#Using append()------------
cars = ["Ford", "BMW", "Volvo", "Toyata"]
cars.append("Honda")
print(cars)

#Using pop()------------
cars = ["Ford", "BMW", "Volvo", "Toyata"]
cars.pop(1)
print(cars)

#Using Remove()------------
cars = ["Ford", "BMW", "Volvo", "Toyata"]
cars.remove("BMW")
print(cars)

#Using count()------------
cars = ["Ford", "BMW", "Volvo", "Toyata"]
x = cars.count("BMW")
print(x)