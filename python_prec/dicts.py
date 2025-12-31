# What is a Dictionary?

# A dictionary is an unordered collection of items. Each item is stored as a key-value pair.
#     Unordered : Historically, dictionaries were unordered. From Python 3.7 onwards, dictionaries maintain insertion order.
#     Mutable: You can add, remove, and modify key-value pairs after the dictionary has been created.
#     Values can be anything: Values can be of any data type and can be duplicates.
#     Keys: Keys are the unique data in a dict and any immutable datatype can be a key
#     Mapping: Dictionaries are often referred to as "mappings" because they map keys to values.
#     We use the : operator to separate the key and value


# An empty dictionary
# empty_dict = {} # dict()
# print(empty_dict)

# # A dictionary with string keys and various values
# person = { "name": "Alice", "age": 30, "city": "New York" }
# person = {
#     "name": "Alice",
#     "age": 30,
#     "city": "New York"
# }
# print(person)

# data = {
#     1: "Alice",
#     2: 30,
#     3: "New York",
#     3: "test"
# }
# print(data)


# # A dictionary with mixed key types (valid because all are immutable and unique)
# mixed_keys_dict = {
#     "name": "Bob",
#     1: "one",
#     3.14: "pi",
#     (1, 2): "tuple key"
# }
# print(mixed_keys_dict)


# # Creating a dictionary using the dict() constructor 
# Note If you are using the dict method you can only pass the strings as key
# student = dict(
#     name="Charlie",
#     id=101,
#     grade="A"
# )
# print(student)

# Accessing Values
# a = {"name": "Alice", "age": 30, "city": "New York"}

# print( a[ "age" ] )

# a = {
#     "name": "Alice",
#     "age": 30,
#     "city": "New York",
#     "data1": { 
#         "level": "Advanced",
#         "data2": [ 1, 2, 3, 4, 5, { "data3": "dummy_value" } ]
#     }
# }

# print(a["data1"]["data2"][-1][ "data3" ])
# print( a.get("data1").get("data2")[-1].get("data3") )
# print( a[ "data1" ][ "data2" ][-1]["data3"] )
# print( a.get("agee") )

# # Accessing with a default value
# print( a.get("cityy", "Jaipur") )

# Modifying Dictionaries
# grades = {"math": 90, "science": 85}
# print(grades)
# grades["history"] = 78
# print(grades)
# grades["math"] = 40
# print(grades)

# Delete a key-value pair using del
# del grades["science"]
# print(grades) # Output: After del 'science': {'math': 92, 'history': 78}
# a = [ 1, 2, 3]
# del a[-1]

# Pop an item
# popped_value = grades.pop("math")
# print(popped_value)
# print(grades)

# # Pop a non-existent item with a default
# missing_value = grades.pop("english", "Not found")
# print(missing_value) # Output: Popped missing: Not found, After pop missing: {'math': 92}

# Pop an arbitrary item (Python 3.7+ is last inserted)
# grades = {"math": 90, "science": 85}
# grades["art"] = 95
# grades["music"] = 88
# print(f"Before popitem: {grades}")
# popped_item_pair = grades.popitem()
# popped_item_pair = grades.popitem()
# print(f"Popped item pair: {popped_item_pair}, After popitem: {grades}")

# LIFO -> Last in First Out
# FIFO -> First In First Out

# grades.clear()
# print(grades)

# Basic Dictionary Operations

# profile = {
#     "name": "Bob",
#     "age": 25,
#     "gender": "Male"
# }

# Length
# print(len( profile ))

# Membership (checks for key)
# print('age' in profile)
# print('Bob' in profile)


# Dictionary Methods

# d1 = {"a": 1, "b": 2}
# d2 = {"b": 3, "c": 4}

# d1.update(d2)
# print(f"After update: {d1}") # Output: After update: {'a': 1, 'b': 3, 'c': 4}

# d2.update(d1)
# print(d2)

# data = {"name": "Alice"}
# email = data.setdefault("email", "unknown@example.com")
# print(data, email)

# data = {}

# counter = 0
# while counter < 50:
#     data[counter] = "key" + str(counter)
#     counter += 1

# print(data)

# new_dict = dict.fromkeys(["key1", "key2", "key3"], 0)
# print(new_dict)

# company = {
#     "CEO": {
#         "name": "John Doe",
#         "department": "Executive"
#     },
#     "employees": {
#         "101": {
#             "name": "Alice",
#             "role": "Engineer"
#         },
#         "102": {
#             "name": "Bob",
#             "role": "Designer"
#         }
#     },
#     "departments": ["HR", "Engineering", "Design"]
# }

# print( company["employees"]["101"]["name"] )
# person = { "name": "Alice", "age": 30, "city": "New York" }

# data1 = tuple(person.keys())
# data = tuple(person.values())
# data2 = person.items()

# print(data)
# print(data1)
# print(list(data2))

# Intermediate Level: More Dictionary Manipulations & Concepts
person = { "name": "Alice", "age": 30, "city": "New York" }

# for x in person:
#     print(x)

# for x in person.values(): # for x in dict_values(['Alice', 30, 'New York']):
#     print(x)

# for x in person.items(): # for x in dict_items([('name', 'Alice'), ('age', 30), ('city', 'New York')]):
#     print(x)

# for x, y in person.items(): # for x in dict_items([('name', 'Alice'), ('age', 30), ('city', 'New York')]):
#     print(x, y)

# new_data = {}
# for x, y in person.items():
#     new_data[y] = x
# print(new_data)

# data = [('name', 'Alice', 1), ('age', 30, 2), ('city', 'New York', 3)]

# for x, y, z in data:
#     print( f"x is {x} and y is {y} and z in {z}")


# From a list of (key, value) tuples
# a = [("USA", "Washington"), ("France", "Paris")]
# countries = dict(a)
# print(countries)


# enumerate() for Index and Value
# When you need both the index and the value of items while iterating, enumerate() is very helpful. It returns pairs of (index, item).

# fruits = ["apple", "banana", "cherry"]

# data = enumerate(fruits)

# # print( dict(data) )

# for x, y in data:
#     print(x, y)


a = ["a", "b", "c", "d", "e"]
b = ["p", "q", "r", "s"]
c = {}


# zip() for Parallel Iteration

# The zip() function allows you to iterate over multiple iterables in parallel, pairing up corresponding elements. It stops when the shortest iterable is exhausted.

# names = ["Alice", "Bob", "Charlie", "Vipin"]
# ages = [30, 24, 35]
# cities = ["NY", "LA"]

# data = zip( names, ages, cities )
# print(data)

# for x in data:
#     print(x)

# for x, y in zip(a, b):
#     c[x] = y
# print(c)

# for name, age, city in zip(names, ages, cities):
#     print(f"{name} is {age} years old and lives in {city}.")



# Nested for Loops
# You can place a for loop inside another for loop. The inner loop will complete all its iterations for each single iteration of the outer loop. This is commonly used for working with 2D data structures (like matrices) or generating combinations.
    
# a = {
#     "number": [ 1, 2, 3, 4, 5, 6, 7, 8 ],
#     "float": [ 1.1, 2.2, 3.3, 4.4, 5.0, 6.0, 7.0, 8.0],
#     "string": "this is a string"
# }


# for x in a:
#     print(x) # "float"
#     for y in a.get(x):
#         print(y)

# *
# **
# ***
# ****
# *****

# for x in range(1, 6):
#     print( "*" * x )


# sticks = 21

# print("There are 21 sticks, you can take 1-4 number of sticks at a time.")
# print("Whoever will take the last stick will lose")

# while True:
#     print("Sticks left: " , sticks)
#     sticks_taken = int(input("Take sticks(1-4):"))
#     if sticks == 1:
#         print("You took the last stick, you lose")
#         break
#     if sticks_taken >= 5 or sticks_taken <= 0:
#         print("Wrong choice")
#         continue
#     print("Computer took: " , (5 - sticks_taken) , "\n")
#     sticks -= 5
