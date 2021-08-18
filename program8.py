#08/October/2020--------
#Python Collection (Array) {List, Tuple, Set, Dictionary}--
#Python List---------

thislist = ["Apple", "Banana", "Orange"]
print(thislist)

thislist = ["Apple", "Banana", "Orange"]
print(thislist[1])

thislist = ["Apple", "Banana", "Orange"]
print(thislist[-2])

thislist = ["Apple", "Banana", "kiwi","mango", "Melon", "Orange"]
print(thislist[2:5])

thislist = ["Apple", "Banana", "kiwi","mango", "Melon", "Orange"]
print(thislist[:4])

thislist = ["Apple", "Banana", "kiwi","mango", "Melon", "Orange"]
print(thislist[2:])

thislist = ["Apple", "Banana", "kiwi","mango", "Melon", "Orange"]
print(thislist[-5:-2])

thislist = ["Apple", "Banana", "kiwi","mango", "Melon", "Orange"]
thislist[1] = "blackcurrant"
print(thislist)

#Loop Through a List---
thislist = ["Apple", "Banana", "kiwi","mango", "Melon", "Orange"]

for x in thislist:
    print(x)

#Loop Through a List---
thislist = ["Apple", "Banana", "kiwi","mango", "Melon", "Orange"]

if "mango" in thislist:
    print("Yes, 'Melon' is in this list.")
else:
    print("No list")

#len()-----
thislist = ["Apple", "Banana", "Orange"]
print(len(thislist))

#append()-----
thislist = ["Apple", "Banana", "Orange"]
thislist.append("Melon")
print(thislist)


#insert()-----
thislist = ["Apple", "Banana", "Orange"]
thislist.insert(1, "Melon")
print(thislist)

#remove()-----
thislist = ["Apple", "Banana", "Orange"]
thislist.remove("Banana")
print(thislist)

#pop()-----
thislist = ["Apple", "Banana", "Orange", "Melon"]
thislist.pop()
print(thislist)

#del()-----
thislist = ["Apple", "Banana", "Orange", "Melon"]
del thislist[2]
print(thislist)

#clear()-----
thislist = ["Apple", "Banana", "Orange", "Melon"]
thislist.clear()
print(thislist)

#copy()-----
thislist = ["Apple", "Banana", "Orange", "Melon"]
mylist = thislist.copy()
print(thislist)
print(mylist)

#list()-----
thislist = ["Apple", "Banana", "Orange", "Melon"]
mylist = list(thislist)
print(thislist)
print(mylist)

#list3()-----
list1 = ["a","b","c"]
list2 = [1,2,3]
list3 = list1 + list2
print(list3)

#list() .append()-----
list1 = ["a","b","c"]
list2 = [1,2,3]
for x in list2:
    list1.append(x)
print(list1)

#list3() .extend()-----
list1 = ["a","b","c"]
list2 = [1,2,3]
list1.extend(list2)
print(list1)

#count()-----
list = [1,3,2,3,4,5,6]
x = list.count(3)
print(x)

#index()-----
list = ["Apple", "Banana", "kiwi","mango"]
x = list.index("kiwi")
print(x)

#insert()-----
list = ["Apple", "Banana", "kiwi","mango"]
list.insert(1,"Orange")
print(list)

#reverse()-----
list = ["Apple", "Banana", "kiwi","mango"]
list.reverse()
print(list)

#sort()-----
list = ["Apple", "Banana", "mango", "kiwi",]
list.sort()
print(list)

