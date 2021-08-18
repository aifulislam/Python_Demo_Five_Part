#13/October/2020--------
#Python---while--Loop-----
#Python---for--Loop-----

i = 1
while i < 6:
    print(i)
    i+=1

print("break---------")
i = 1
while i < 15:
    print(i)
    if (i == 10):
        break
    i += 1

print("Continue---------")
i = 0
while i < 6:
    i += 1
    if i== 3:
        continue
    print(i)

print("Continue---------")
i = 0
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")

#Python---for--Loop-----

fruits = ["Apple", "Banana", "Orange"]
for x in fruits:
    print(x)

for x in "banana":
    print(x)

fruits = ["Apple", "Banana", "Orange"]
for x in fruits:
    print(x)
    if x == "banana":
        break

fruits = ["Apple", "Banana", "Orange"]
for x in fruits:
    if x == "Banana":
        break
    print(x)

fruits = ["Apple", "Banana", "Orange"]
for x in fruits:
    if x == "Banana":
        break
    print(x)

fruits = ["Apple", "Banana", "Orange"]
for x in fruits:
    if x == "Banana":
        continue
    print(x)

#Using the range() function-------
for x in range(6):
    print(x)

for x in range(2,6):
    print(x)

for x in range(2,20,2):
    print(x)

#Else in for Loop-----
for x in  range(5):
    print(x)
else:
    print("Finally finished")

#Nested Loops---
adj = ["red", "big", "nice",]
fruits = ["Apple", "Banana", "Orange"]
for x in adj:
    for y in fruits:
        print(x,y)

#Pass loop--
for x in [0 , 1, 2]:
    pass

