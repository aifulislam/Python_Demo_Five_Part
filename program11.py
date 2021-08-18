#11/October/2020--------
#Python Collection (Array) {List, Tuple, Set, Dictionary}--
# "Apple", "Banana", "kiwi","mango", "Melon", "Orange"
#Python Dictionary---

thisdict = {"brand": "Ford",
            "Model" : "Bmw",
            "Melon": "2020"}
print(thisdict)

thisdict = {"brand": "Ford",
            "Model" : "Bmw",
            "year": "2020"}
x = thisdict["Model"]
print(x)

thisdict = {"brand": "Ford",
            "Model" : "Bmw",
            "year": "2020"}
x = thisdict["Model"] = "Apple"
print(x)

thisdict = {"brand": "Ford",
            "Model" : "Bmw",
            "year": "2020"}
x = thisdict.get("Model")
print(x)

thisdict = {"brand": "Ford",
            "Model" : "Bmw",
            "year": "2020"}
for x in thisdict:
    print(x)

thisdict = {"brand": "Ford",
            "Model" : "Bmw",
            "year": "2020"}
for x in thisdict:
    print(thisdict[x])

thisdict = {"brand": "Ford",
            "Model" : "Bmw",
            "year": "2020"}
for x in thisdict.values():
    print(x)

thisdict = {"brand": "Ford",
            "Model" : "Bmw",
            "year": "2020"}
for x, y in thisdict.items():
    print(x,y)

thisdict = {"brand": "Ford",
            "Model" : "Bmw",
            "year": "2020"}
if "Model" in thisdict:
    print("Yes")
else:
    print("No")

thisdict = {"brand": "Ford",
            "Model" : "Bmw",
            "year": "2020"}
print(len(thisdict))

thisdict = {"brand": "Ford",
            "Model" : "Bmw",
            "year": "2020"
            }

thisdict["color"] = "red"
print(thisdict)

thisdict = {"brand": "Ford",
            "Model" : "Bmw",
            "year": "2020"
            }

thisdict.pop("year")
print(thisdict)

thisdict = {"brand": "Ford",
            "Model" : "Bmw",
            "year": "2020"
            }

thisdict.popitem()
print(thisdict)

thisdict = {"brand": "Ford",
            "Model" : "Bmw",
            "year": "2020"
            }

del thisdict["year"]
print(thisdict)

thisdict = {"brand": "Ford",
            "Model" : "Bmw",
            "year": "2020"
            }

thisdict.clear()
print(thisdict)

thisdict = {"brand": "Ford",
            "Model" : "Bmw",
            "year": "2020"
            }

mydict = thisdict.copy()
print(mydict)

thisdict = {"brand": "Ford",
            "Model" : "Bmw",
            "Color" : "red",
            "year": "2020"
            }

mydict = dict(thisdict)
print(mydict)

#Nested Dictionaries-----1------
thisdict = {
    "man1" : {
        "Name : " : "Arif",
        "Age : "  : 26,
        "year"    : 1994
    },
    "man2" : {
            "Name : " : "Tamim",
            "Age : "  : 20,
            "year"    : 2000
    },
    "man3" : {
                "Name : " : "Nazim",
                "Age : "  : 27,
                "year"    : 1993
        },
}
print(thisdict)

#Nested Dictionaries-----2------

Phone = {
    "Phone1" : {
        "name" : "Apple",
        "Clor" : "White",
        "Prise" : "$399.99"
    },
    "Phone2" : {
        "name" : "Samsang",
        "Clor" : "Green",
        "Prise" : "$199.99"
    },
    "Phone3" : {
        "name" : "Oppo",
        "Clor" : "Red",
        "Prise" : "$299.99"
    }
}
print(Phone)

#Nested Dictionaries------3-----

man1 = {
    "Name : " : "Arif",
    "Age : "  : 26,
    "year"    : 1994
},
man2 = {
    "Name : " : "Tamim",
    "Age : "  : 20,
    "year"    : 2000
},
man3 = {
    "Name : " : "Nazim",
    "Age : "  : 27,
    "year"    : 1993
},

thisdict = {
    "man1" : man1,
    "man2" : man2,
    "man3" : man3,
}
print(thisdict)

#Nested Dictionaries-----4------

Phone1 = {
    "name" : "Apple",
    "Color" : "White",
    "Prise" : "$399.99"
},
Phone2 = {
    "name" : "Samsang",
    "Color" : "Green",
    "Prise" : "$199.99"
},
Phone3 = {
    "name" : "Oppo",
    "Color" : "Red",
    "Prise" : "$299.99"
}

Phone = {
    "Phone1" : Phone1,
    "Phone2" : Phone2,
    "Phone3" : Phone3
}
print(Phone)

#The dict() Constructor---------
thisdict = dict(brand = "Apple",model = "7+",prise = "$399.99")
print(thisdict)

