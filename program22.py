#22/October/2020--------
#Python---Classes and Objeects----
#Datetime----------

import datetime
x = datetime.datetime.now()
y = datetime.datetime(1994, 3, 2)
print(x)
print(y)
print(x.year)
print(x.month)
print(x.day)

#Legal format codes:--------
print(x.strftime("%a"))
print(x.strftime("%A"))
print(x.strftime("%b"))
print(x.strftime("%B"))
print(x.strftime("%c"))
print(x.strftime("%d"))
print(x.strftime("%D"))
print(x.strftime("%f"))
print(x.strftime("%F"))
print(x.strftime("%H"))
print(x.strftime("%I"))
print(x.strftime("%j"))
print(x.strftime("%m"))
print(x.strftime("%M"))
print(x.strftime("%p"))
print(x.strftime("%S"))
print(x.strftime("%U"))
print(x.strftime("%W"))
print(x.strftime("%x"))
print(x.strftime("%X"))
print(x.strftime("%y"))
print(x.strftime("%Y"))
print(x.strftime("%z"))
print(x.strftime("%Z"))
print(x.strftime("%%"))

