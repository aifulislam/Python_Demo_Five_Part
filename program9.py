#09/October/2020--------
#Python Collection (Array) {List, Tuple, Set, Dictionary}--
#Python Tuple---

thistuple = ("Apple", "Banana","Orange")
print(thistuple)

thistuple = ("Apple", "Banana","Orange")
print(thistuple[2])

thistuple = ("Apple", "Banana","Orange")
print(thistuple[-2])

thistuple = ("Apple", "Banana","Orange", "kiwi","mango", "Melon",)
print(thistuple[2:5])

thistuple = ("Apple", "Banana","Orange", "kiwi","mango", "Melon",)
print(thistuple[-5:-2])

x = ("Apple", "Banana","Orange", "Melon",)
y = list(x)
y[1] = "mango"
x = tuple(y)
print(x)

thistuple = ("Apple", "Banana","Orange", "Melon",)
for x in thistuple:
    print(x)

thistuple = ("Apple", "Banana","Orange", "Melon",)
if "Apple" in thistuple:
    print("Yes")
else:
    print("No")

thistuple = ("Apple", "Banana","Orange", "Melon",)
print(len(thistuple))

thistuple = ("Apple", "Banana","Orange", "Melon",)
print(type(thistuple))

thistuple = ("Apple")
print(type(thistuple))

tuple1 = ("Apple", "Banana","Orange", "Melon",)
tuple2 = (1,2,3)
tuple3 = tuple1 + tuple2
print(tuple3)

thistuple = tuple(("Apple", "Banana","Orange", "Melon",))
print(thistuple)

thistuple = ("Apple", "Banana","Orange", "Apple", "Melon",)
x = thistuple.count("Apple")
print(x)

thistuple = ("Apple", "Banana","Orange", "Apple", "Melon",)
x = thistuple.index("Orange")
print(x)

