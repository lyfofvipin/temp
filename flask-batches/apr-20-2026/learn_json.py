import json

# Encoding

# json.dump()	Dump File: Writes a Python object directly to an open file.	Saving configuration or data permanently to disk.
# json.dumps()	Dump String: Converts a Python object into a JSON-formatted string.	Sending data over a network (e.g., in a FastAPI response).

# python_data = {
#     'name': 'Bob',
#     'items': [10, 20, 30],
#     'is_vip': False
# }

# with open("dummy.json", "w") as fobj:
#     json.dump( python_data, fobj, indent=4 )

# a = json.dumps(python_data)
# '{"name": "Bob", "items": [10, 20, 30], "is_vip": false}'
# print(a)


# Decoding

# json.load()	Load File: Reads data directly from an open file and converts it into a Python object.
# Reading saved configuration or data files.
# json.loads()	Load String: Converts a JSON-formatted string into a Python object.
# Receiving and processing a response from an API.


json_input_string = '{"city": "London", "temperature": 15.5, "unit": true}'
print(json.loads(json_input_string))


# with open('dummy.json') as f:
#     print(json.load(f))
