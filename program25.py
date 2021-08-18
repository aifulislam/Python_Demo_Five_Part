#25/October/2020--------
#Python---Classes and Objeects----
#RegEx----Regular Expresion------

#The search()----
import re
txt = "The rain in Spain"
x = re.search("portugal",txt)
print(x)

#The search()----
import re
txt = "The rain in Spain"
x = re.search("^The.*Spain$",txt)
if x:
    print("Yes! We have a match!")
else:
    print("No match")

#The findall()----
import re
txt = "The rain in Spain"
x = re.findall("in",txt)
print(x)

#The findall()----
import re
txt = "The rain in Spain"
x = re.findall("portugal",txt)
print(x)
if (x):
    print("Yes")
else:
    print("No")

#start position:
import re
txt = "The rain in Spain"
x = re.search("\s",txt)
print("The first white-space character is located in start position:", x.start())

import re
txt = "This is our country."
x = re.search("\s",txt)
print("The first white-space character is located in start position:", x.start())

#The split()----
import re
txt = "The rain in Spain"
x = re.split("\s",txt)
print(x)

#The maxsplit()----
import re
txt = "The rain in Spain"
x = re.split("\s",txt, 1)
print(x)

#The sub()----
import re
txt = "The rain in Spain"
x = re.sub("\s","9", txt)
print(x)

#The count()----
import re
txt = "The rain in Spain"
x = re.sub("\s","9", txt, 2)
print(x)

#Match Object()----
import re
txt = "The rain in Spain"
x = re.search("ai", txt)
print(x)

#Match Object()----span()---
import re
txt = "The rain in Spain"
x = re.search(r"\bS\w+",txt)
print(x.span())

#Match Object()----string-----
import re
txt = "The rain in Spain"
x = re.search(r"\bS\w+",txt)
print(x.string)

#Match Object()----group()-----
import re
txt = "The rain in Spain"
x = re.search(r"\bS\w+",txt)
print(x.group())

#Regular expressions----------

#match----------------
import re
pattern = r"love"
if re.match(pattern,"love, Bangladesh is my country . I love my country"):
    print("Match")
else:
    print("Not Match")

#search----------------
import re
pattern = r"love"
if re.search(pattern,"Bangladesh is my country . I love my country"):
    print("Match")
else:
    print("Not Match")

#search------2----------
import re
pattern = r"love"
text = "Bangladesh is my country . I love my country"
match = re.search(pattern,text)
if match:
    print(match.start())
    print(match.end())
    print(match.span())

#findall--------------
import re
pattern = f"love"
print(re.findall(pattern,"Bangladesh love is my country . I love my country"))

#Search And Replace--------
import re
pattern = f"love"
text1 = "Bangladesh love is my country . I love my country"
txt2 =  re.sub(pattern,"like",text1,count=1)
print(txt2)

#Search And Replace--------
import re
pattern = f"teacher"
txt3 = "I am a teacher. I am BSC pass."
txt4 = re.sub(pattern,"student",txt3,count=0)
print(txt4)

#Meta Characters----------
#dot Meta Character------
import re
pattern = f"lo.e"
if re.search(pattern,"love"):
    print("Matched1")

# ^....& Meta Character-------
import re
pattern = f"^lo.e$"
if re.search(pattern,"love"):
    print("Matched2")

# * / 0 or more / Meta Character-------
import re
pattern = f"o*"
if re.search(pattern,"love"):
    print("Matched3")

# * / 0 or more / Meta Character-------
import re
pattern = f"l*o"
if re.search(pattern,"love"):
    print("Matched4")

# + / one or more / Meta Character-------
import re
pattern = f"o+"
if re.search(pattern,"love"):
    print("Matched5")

# + / one or more / Meta Character-------
import re
pattern = f"l+o"
if re.search(pattern,"love"):
    print("Matched6")

# ? /0 or one / Meta Character-------
import re
pattern = f"ice(-)?cream"
if re.search(pattern,"ice-cream"):
    print("Matched7")

# {} /0 or one / Meta Character-------
import re
pattern = r"a{1,3}$"
if re.search(pattern,"aaa"):
    print("Matched8")

#Character Class---------
#[aeiou]---------
import re
pattern = r"[aeiou]"
if re.match(pattern,"alove"):
    print("matched9")

#[a-z]----------
import re
pattern = r"[a-z]"
if re.match(pattern,"love"):
    print("matched10")

#[A-Z]-----------
import re
pattern = r"[A-Z]"
if re.match(pattern,"Alove"):
    print("matched11")

#[a-z,A-Z,0-9]--------
import re
pattern = r"[a-z,A-Z,0-9]"
if re.match(pattern,"5ScASKLAnDLD"):
    print("matched12")

#[a-z,A-Z,0-9]--------
import re
pattern = r"[a-z][A-Z][0-9]"
if re.match(pattern,"aA1love"):
    print("matched13")

#[!@#$%^&*()?~]--------
import re
pattern = r"[!@#$%^&*(){}?~]"
if re.match(pattern,"{)%dfaf"):
    print("matched14")


