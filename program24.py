#24/October/2020--------
#Python---Classes and Objeects----
#Json----------

import json
x = '{ "name": "Arif" , "age": 25, "city": "US" }'
y = json.loads(x)
print(y["name"])
print(y["age"])
print(y["city"])

#Using dumps()-------
import json
x = { "name": "Tamim",
    "age": "05",
    "city": "Uk"}
y = json.dumps(x)
print(y)

#Using dumps()-------
import json
x = {
    "name" : "Nasim",
    "age" : "25",
    "city" : "NZ",
}
y = json.dumps(x)
print(y)

#Convert----Json to paython-----
import json
print(json.dumps({ "name": "Arif" , "age": 25, "city": "US" }))
print(json.dumps(["Apple", "Banana" ]))
print(json.dumps(("Apple", "Banana" )))
print(json.dumps("Hello"))
print(json.dumps(2020))
print(json.dumps(20.20))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

#Using dumps-----
import json
y = json.dumps(x)
print(y)

#Format the Result-----
import json
y = json.dumps(x,indent=4)
print(y)

#Using separators-----
import json
print(json.dumps(x, indent=4, separators=(". ", " = ")))

#Order the Result-----
import json
print(json.dumps(x, indent=4, sort_keys=True))

