#27/October/2020--------
#Python---Classes and Objeects----
#Python String Formatting-----

price = 49
txt = "The price is {} dollars."
print(txt.format(price))

price = 49
txt = "The price is {:.2f} dollars."
print(txt.format(price))

#Mutile Values----------
quantity = 3
itemno = 567
price = 49
myorder = "I want {} pices of items number {} for {:.2f} dollars."
print(myorder.format(quantity,itemno,price))

#Mutile Values----------
quantity = 5
itemno = 500
price = 50
myorder2 = "I want {} pices of items number {} for {:.2f} dollars."
print(myorder2.format(quantity,itemno,price))

#Mutile Values----------
age = 25
name = "Arif"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age,name))

#Mutile Values----------
age = 25
name = "Arif"
class1 = "BSC"
txt = "My name is {0}. I read in {1}. My age {2} years old."
print(txt.format(name,class1,age))

#Named Indexed--------
txt = "I have a {carname}, It is a {model}."
print(txt.format(carname = "Ford",model= "Mustang"))

