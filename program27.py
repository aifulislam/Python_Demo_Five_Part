#26/October/2020--------
#Python---Classes and Objeects----
#Python Try Except-----

'''
try
except
finally
'''

try:
    print(x)
except:
    print("An exception occurred")

#Many Exception---
#NameError--
try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something Wrong")

#Else----------
try:
    print("Hello")
except:
    print("Variable x is not defined")
else:
    print("Something Wrong")

#Using finally------
try:
    print(x)
except:
    print("Something went Wrong")
finally:
    print("The 'try except' is finally finished")

#Using finally------
try:
    f = open("demofile.txt")
    f.write("Ariful Islam")
except:
    print("something went wrong when writing to the file")
finally:
    f.close()

#Raise an exception------
x = -1
if x < 0 :
    raise Exception("Sorry, no numbers below zero")

#TypeError--------------
x = "Hello"
if not type(x) is int:
    raise TypeError("Only integers are allowed")

