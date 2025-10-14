# What is a Tuple?

# Think of a tuple as a fixed, unchangeable sequence of items. 
# If a list is a shopping list you can constantly update, 
# a tuple is more like a fixed set of coordinates (latitude, longitude) 
# or a record of a person's birth date that won't change.

#     Ordered: The items have a defined order, and that order is preserved.
#     Immutable: Once created, you cannot change, add, or remove items.
#     Heterogeneous: Tuples can contain items of different data types (integers, strings, floats, even other lists or objects).

# # An empty tuple
# empty_tuple = ()
# print(f"Empty tuple: {empty_tuple}") # Output: Empty tuple: ()

# # A tuple of integers
# numbers = (1, 2, 3, 4, 5)
# print(f"Tuple of numbers: {numbers}") # Output: Tuple of numbers: (1, 2, 3, 4, 5)

# # A tuple of strings
# fruits = ("apple", "banana", "cherry")
# print(f"Tuple of fruits: {fruits}") # Output: Tuple of fruits: ('apple', 'banana', 'cherry')

# # A tuple with mixed data types
# mixed_tuple = ("hello", 123, 3.14, False)
# print(f"Mixed tuple: {mixed_tuple}") # Output: Mixed tuple: ('hello', 123, 3.14, False)


# # A tuple containing a list (nested mutable object)
# nested_tuple = (1, [2, 3], 4, "test")
# # print(f"Nested tuple: {nested_tuple}") # Output: Nested tuple: (1, [2, 3], 4)
# nested_tuple[1][0] = 4
# nested_tuple[1][1] = 5
# print(nested_tuple)

# Important: A single-element tuple requires a trailing comma!
# Without it, Python treats it as just the item itself, not a tuple.
# single_element_tuple = (5,)
# print(f"Single-element tuple: {single_element_tuple}, type: {type(single_element_tuple)}")
# Output: Single-element tuple: (5,), type: <class 'tuple'>

# not_a_tuple = (5) # This is just an integer 5
# print(f"Not a tuple: {not_a_tuple}, type: {type(not_a_tuple)}")
# Output: Not a tuple: 5, type: <class 'int'>

# # Creating a tuple without parentheses (tuple packing)
# packed_tuple = "a", 10, True
# print(f"Packed tuple: {packed_tuple}, type: {type(packed_tuple)}")
# # Output: Packed tuple: ('a', 10, True), type: <class 'tuple'>

# my_tuple = ("a", "b", "c", "d", "e")

# # Accessing elements using positive indexing
# print(f"First element: {my_tuple[0]}")  # Output: First element: a
# print(f"Third element: {my_tuple[2]}")  # Output: Third element: c

# # Accessing elements using negative indexing
# print(f"Last element: {my_tuple[-1]}")   # Output: Last element: e
# print(f"Second to last element: {my_tuple[-2]}") # Output: Second to last element: d

# numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

# # Get elements from index 2 up to (but not including) index 6
# print(f"Slice [2:6]: {numbers[2:6]}")   # Output: Slice [2:6]: (2, 3, 4, 5)

# # Get elements from the beginning up to index 5
# print(f"Slice [:5]: {numbers[:5]}")    # Output: Slice [:5]: (0, 1, 2, 3, 4)

# # Get elements from index 7 to the end
# print(f"Slice [7:]: {numbers[7:]}")    # Output: Slice [7:]: (7, 8, 9)

# # Get a copy of the entire tuple
# print(f"Full slice [:]: {numbers[:]}") # Output: Full slice [:]: (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

# # Get every second element
# print(f"Slice [::2]: {numbers[::2]}")  # Output: Slice [::2]: (0, 2, 4, 6, 8)

# # Reverse the tuple using slicing
# print(f"Reversed slice [::-1]: {numbers[::-1]}") # Output: Reversed slice [::-1]: (9, 8, 7, 6, 5, 4, 3, 2, 1, 0)


tuple1 = (1, 2)
tuple2 = (3, 4)

# Concatenation
# combined_tuple = tuple2 + tuple1
# print(f"Concatenated tuple: {combined_tuple}") # Output: Concatenated tuple: (1, 2, 3, 4)

# Repetition
# repeated_tuple = tuple1 * 3
# print(f"Repeated tuple: {repeated_tuple}") # Output: Repeated tuple: (1, 2, 1, 2, 1, 2)

# # Membership
# print(f"Is 2 in tuple1? {2 in tuple1}")     # Output: Is 2 in tuple1? True
# print(f"Is 5 not in tuple2? {5 not in tuple2}") # Output: Is 5 not in tuple2? True


# my_tuple = ("apple", "banana", "cherry")

# # Attempting to change an element (will raise TypeError)
# my_tuple[1] = "grape"

# my_tuple_with_list = (1, [2, 3], 4)
# print(f"Original tuple with list: {my_tuple_with_list}") # Output: Original tuple with list: (1, [2, 3], 4)

# my_tuple_with_list[1].append(5) # Modifying the list INSIDE the tuple
# print(f"Modified tuple with list: {my_tuple_with_list}") # Output: Modified tuple with list: (1, [2, 3, 5], 4)
# # This is allowed because you are not changing the tuple itself (i.e., you're not reassigning index 1 to a different object).
# # You are changing the *contents* of the list object that index 1 points to.

# Tuple packing
# my_data = 10, "hello", True
# print(f"Packed data: {my_data}") # Output: Packed data: (10, 'hello', True)

# # Tuple unpacking
# # The number of variables on the left must match the number of elements in the tuple.

# x, y, z = 10, "hello", True

# # x = 10
# # y = "hello"
# # z = True

# print(f"Unpacked: x={x}, y={y}, z={z}") # Output: Unpacked: x=10, y=hello, z=True

# Swapping variables easily using tuple unpacking
# a = 10
# b = 20

# a, b = 20, 10 # Python first evaluates (b, a) as a tuple, then unpacks
# print(f"After swap: a={a}, b={b}") # Output: After swap: a=20, b=10

# Unpacking with * (star operator) for arbitrary remaining elements (Python 3+)
# coordinates = (1, 2, 3, 4, 5)
# # x, y, *rest, z = coordinates
# # print(f"x={x}, y={y}, rest={rest}, z={z}") # Output: x=1, y=2, rest=[3, 4, 5]

# first, *middle, last = coordinates
# print(f"first={first}, middle={middle}, last={last}") # Output: first=1, middle=[2, 3, 4], last=5


# my_list = [1, 2, 3]
# my_tuple = tuple(my_list)
# print(f"List to tuple: {my_tuple}, type: {type(my_tuple)}") # Output: List to tuple: (1, 2, 3), type: <class 'tuple'>

# my_tuple_orig = ("a", "b", "c")
# my_list_from_tuple = list(my_tuple_orig)
# print(f"Tuple to list: {my_list_from_tuple}, type: {type(my_list_from_tuple)}") # Output: Tuple to list: ['a', 'b', 'c'], type: <class 'list'>


# my_tuple = (1, 2, 3, 2, 4, 2)

# print(f"Count of 2: {my_tuple.count(2)}") # Output: Count of 2: 3
# print(f"Index of 4: {my_tuple.index(2, 2)}") # Output: Index of 4: 4
