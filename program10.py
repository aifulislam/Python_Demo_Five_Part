#10/October/2020--------
#Python Collection (Array) {List, Tuple, Set, Dictionary}--
#Python Set---

thisset = {"Apple", "Banana","Orange", "Apple", "Melon",}
print(thisset)

thisset = {"Apple", "Banana","Orange", "Melon",}
for x in thisset:
    print(x)

thisset = {"Apple", "Banana", "Orange", "Melon",}
print("Apple" in thisset)
#print("Apple" not in thisset)

thisset = {"Apple", "Banana", "Melon"}
thisset.add("Orange")
print(thisset)

thisset = {"Apple", "Banana", "Melon"}
thisset.update(["Orange","kiwi","tomato"])
print(thisset)

thisset = {"Apple", "Banana", "Melon"}
print(len(thisset))

thisset = {"Apple", "Banana", "Melon", "tomato"}
thisset.remove("Melon")
print(thisset)

thisset = {"Apple", "Banana", "Melon", "tomato"}
thisset.discard("Melon")
print(thisset)

thisset = {"Apple", "Banana", "Melon", "tomato"}
x = thisset.pop()
print(x)
print(thisset)

thisset = {"Apple", "Banana", "Melon", "tomato"}
thisset.clear()
print(thisset)

thisset1 = {"Apple", "Banana", "Melon", "tomato"}
thisset2 = {1,2,3,4}
thisset3 = thisset1.union(thisset2)
print(thisset3)

thisset1 = {"Apple", "Banana", "Melon", "tomato"}
thisset2 = {1,2,3,4}
thisset1.update(thisset2)
print(thisset1)

thisset = set(("Apple", "Banana", "Melon", "tomato"))
print(thisset)

