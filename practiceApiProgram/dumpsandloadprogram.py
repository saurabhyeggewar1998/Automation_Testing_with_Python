#json.dumps() method can convert a Python object into a JSON string
# Python program to convert
# Python to JSON
#conver python dictinory to string


import json

# Data to be written
dictionary = {
    "id": "04",
    "name": "sunil",
    "department": "HR"
}

# Serializing json
json_object = json.dumps(dictionary, indent=4)
print(json_object)

#json.dump()
#json.dump() method can be used for writing to JSON file.

# Python program to write JSON
# to a file
import json

# Data to be written
dictionary ={
	"name" : "sathiyajith",
	"rollno" : 56,
	"cgpa" : 8.6,
	"phonenumber" : "9976770500"
}

with open("sample.json", "w") as outfile:
	json.dump(dictionary, outfile,indent=6)


#json.load() takes a file object and returns the json object. It is used to read JSON encoded data from a file and
# convert it into a Python dictionary and deserialize a file itself i.e. it accepts a file object.

import json

data = {
	"name": "Satyam kumar",
	"place": "patna",
	"skills": [
		"Raspberry pi",
		"Machine Learning",
		"Web Development"
	],
	"email": "xyz@gmail.com",
	"projects": [
		"Python Data Mining",
		"Python Data Science"
	]
}
with open( "data_file.json" , "w" ) as write:
	json.dump( data , write )


#json.loads() method can be
# used to parse a valid JSON string and convert it into a Python Dictionary.

import json

# JSON string:
# Multi-line string
data = """{
	"Name": "Jennifer Smith",
	"Contact Number": 7867567898,
	"Email": "jen123@gmail.com",
	"Hobbies":["Reading", "Sketching", "Horse Riding"]
	}"""

# parse data:
res = json.loads(data)

# the result is a Python dictionary:
print(res)
