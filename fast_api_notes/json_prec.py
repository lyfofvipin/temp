# What is JSON? 🌐

# JSON stands for JavaScript Object Notation. It is a lightweight, human-readable format used primarily for exchanging data between a 
# server and a web application (i.e., over an API).

# Human-Readable: It uses plain text and is easy for people to read and write.
# Language Independent: While it originated from JavaScript, nearly every programming language (Python, Java, PHP, etc.) has libraries to read and write data in JSON format.
# Data Structure: JSON is built on two universal structures:
#   Objects: Represented by curly braces {}. These are collections of key-value pairs, just like a Python dictionary. Keys must be strings.
#   Arrays: Represented by square brackets []. These are ordered lists of values, just like a Python list.

# {
#   "user_id": 105,
#   "is_active": true,
#   "roles": ["admin", "editor"],
#   "profile": {
#     "city": "New York",
#     "last_login": null
#   }
# }

# The Python json Module

# The built-in json module in Python is used to convert data between native Python objects and JSON format.


# Encoding:

# json.dumps()	Dump String: Converts a Python object into a JSON-formatted string.	Sending data over a network (e.g., in a FastAPI response).
# json.dump()	Dump File: Writes a Python object directly to an open file.	Saving configuration or data permanently to disk.



# import json

# python_data = {
#     "name": "Bob",
#     "items": [10, 20, 30],
#     "is_vip": False
# }

# str_wala_json = str(python_data)
# print(str_wala_json)

# json_string = json.dumps(python_data)
# print(json_string)
# print(type(json_string))

# with open('data_output.json', 'w') as f:
#     json.dump(python_data, f, indent=4)


# Decoding:

# json.loads()	Load String: Converts a JSON-formatted string into a Python Dict.
# Receiving and processing a response from an API.
# json.load()	Load File: Reads data directly from an open file and converts it into a Python object.
# Reading saved configuration or data files.


# import json

# json_input_string = '{"city": "London", "temperature": 15.5, "unit": true}'
# python_dict = json.loads(json_input_string)
# print(python_dict)
# print(type(python_dict))


# with open('data_output.json') as f:
#     loaded_data = json.load(f)

# print(loaded_data)
# print(type(loaded_data))
































import json

def user():
    with open("data_output.json") as f:
        return json.load(f)
    
data = user()
# data = {'name': 'Bob', 'items': [10, 20, 30], 'is_vip': False}

data["name"] = "Rohit"

print(data)
# {'name': 'Rohit', 'items': [10, 20, 30], 'is_vip': False}

data["items"] = ["Bag", "Laptop", "Mobile"]

print(data)
# {'name': 'Rohit', 'items': ["Bag", "Laptop", "Mobile"], 'is_vip': False}


with open("update_data_output.json", "w") as file:
    json.dump(data, file)

