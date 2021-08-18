#05/October/2020--------
#Python String-----

print("Hello")

a = "Arif"
print(a)

b ="""I am Arif.I am studeent.
I live in Bangladesh"""
print(b)

a = "Hello World!"
print(len(a))
print(a[2])
print(a[-4])
print(a[2:5])
print(a[-5:-2])

a = " Hello World! "
print(a.strip())

a = "HELLO WORLD"
print(a.lower())

a = "hello world"
print(a.upper())

a = "Hello World"
print(a.replace("H","J"))

a = "Hello World"
b = a.split(" , ")
print(b)

tex = "The rain in Spain stays mainly in the plain"
x = "ain" in tex
print(x)

tex = "The rain in Spain stays mainly in the plain"
x = "ain" not in tex
print(x)

a = "Hello "
b = "World"
c = a + b
print(c)

a = "Hello"
b = "World"
c = a + " " + b
print(c)

age = 26
text = "My name is Ariful Islam, I am {}"
print(text .format(age))

quantity = 3
itemno = 265
price = 49.99
myorder = "I want {} pieces of item {} for dollars ${}."
print(myorder.format(quantity,itemno,price))

gpa = 4.50
year = 2009
ssc = "SSC"
me = "I am Ariful Islam. I passed {2}. My passing year was {1} and My gpa point was {0}"
print(me.format(gpa,year,ssc))

text = 'It\'s alright.'
print(text)

text = "I am Ariful \\Islam"
print(text)

text = "I am Ariful \nIslam"
print(text)

text = "Ariful\rIslam"
print(text)

text = "Ariful\tIslam"
print(text)

text = "Ariful\bIslam"
print(text)

text = "Ariful\fIslam"
print(text)

#Octal value---
text = "\110\145\154\154\157"
print(text)

#Hexa value----
text = "\x48\x65\x6c\x6c\x6f"
print(text)

#capitalize()----
text = "hello ,and welcome to my world."
x = text.capitalize()
print(x)

#casefold()----
text = "Hello ,and welcome to my world."
x = text.casefold()
print(x)

#center()----
text = "Arif"
x = text.center(20)
print(x)

#center()----
text = "Arif"
x = text.center(20, "*")
print(x)

#count()----
text = "I love apples, apple are my favorite fruit"
x = text.count("apple")
print(x)

#count()----
text = "I love apples, apple are my favorite fruit"
x = text.count("apple" , 5 ,15)
print(len(text))
print(x)

#endswith()----
text = "I love apples, apple are my favorite fruit"
x = text.endswith("t")
print(x)

#endswith()----
text = "I love apples, apple are my favorite fruit"
x = text.endswith("fruit" ,30,42)
print(len(text))
print(x)

#expandtabs()----
text = "H\te\tl\tl\to"
x = text.expandtabs(2)
print(x)

#find()----
text = "Hello, welcome to my world"
x = text.find("welcome")
print(x)

#find()----
text = "Hello, welcome to my world"
x = text.find("o")
print(x)

#format()----
text = "For  only {price:.2f} taka!"
x = text.format(price = 49)
print(x)

#format()----
text1 = "My name is {fname},I am {age}".format(fname = "Arif",age= "26")
print(text1)
text2 = "My name is {0},I am {1}".format("Arif",26)
print(text2)
text2 = "My name is {},I am {}".format("Arif",26)
print(text2)


