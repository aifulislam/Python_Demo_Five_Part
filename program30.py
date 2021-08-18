#28/October/2020--------
#Python---Classes and Objeects----
#Python File Open-----
#open()-- r, a , w, x, t , b-----

f = open("demofile.txt")

f1 = open("demofile.txt", "rt")

f2 = open("demofile.txt", "r")
print(f.read(25))

#readline()--------
f3 = open("demofile.txt")
print(f.readline())

f = open("demofile.txt", "r")
print(f.read(5))

f = open("demofile.txt", "r")
print(f.readline())

#Loop--------
f = open("demofile.txt", "r")
for x in f:
    print(x)

f = open("demofile.txt", "r")
for x in f:
    print(x)

#Close File-------
f = open("demofile.txt", "r")
print(f.readline())
f.close()

#Write File--------
f = open("demofile2.txt", "a")
f.write("I love my Mother")
f.close()

f = open("demofile2.txt", "r")
print(f.read())

#Write File--------
f = open("demofile2.txt", "w")
f.write("I love my Father")
f.close()

f = open("demofile2.txt", "r")
print(f.read())

#Python Delete File----------
"""
os.remove()
import os
os.remove()
os.path.exists()
os.rmdir()
"""

