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
# print(f"Empty tuple: {empty_tuple}") 

# A tuple of integers
# numbers = (1, 2, 3, 4, 5)
# print(f"Tuple of numbers: {numbers}") 

# A tuple of strings
# fruits = ("apple", "banana", "cherry")
# print(f"Tuple of fruits: {fruits}") 

# # A tuple with mixed data types
# mixed_tuple = ("hello", 123, 3.14, False, (23, 243, ["sf"]))
# print(f"Mixed tuple: {mixed_tuple}")

# # A tuple containing a list (nested mutable object)
# nested_tuple = (1, [2, 3], 4, "test")

# print( nested_tuple[1][0] )

# nested_tuple[1][0] = 4
# nested_tuple[1][1] = 5
# print(nested_tuple)

# Important: A single-element tuple requires a trailing comma!
# Without it, Python treats it as just the item itself, not a tuple.
# single_element_tuple = (5, )
# print(f"Single-element tuple: {single_element_tuple}, type: {type(single_element_tuple)}")


# not_a_tuple = (5)
# print(f"Not a tuple: {not_a_tuple}, type: {type(not_a_tuple)}")


# Creating a tuple without parentheses (tuple packing)

# packed_tuple = "a", 10, True
# print(packed_tuple)


# Tuple unpacking

# a, b, c = 10, 20, 30
# print(a, b, c)

# my_tuple = (1, 2, 3, 4, 5)
# a, b, c, d, e = my_tuple

# print( f" a: {a}, b: {b}, c: {c}, d: {d}, e: {e} " )
# print( a, b, c, d, e )

# # Accessing elements using positive indexing
# print(f"First element: {my_tuple[0]}")  
# print(f"Third element: {my_tuple[2]}")  

# # Accessing elements using negative indexing
# print(f"Last element: {my_tuple[-1]}")   
# print(f"Second to last element: {my_tuple[-2]}") 

# numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

# Get elements from index 2 up to (but not including) index 6
# print(f"Slice [2:6]: {numbers[2:6]}")

# Get elements from the beginning up to index 5
# print(f"Slice [:5]: {numbers[:5]}")    

# Get elements from index 7 to the end
# print(f"Slice [7:]: {numbers[7:]}")    

# Get a copy of the entire tuple
# print(f"Full slice [:]: {numbers[:]}") 

# Get every second element
# print(f"Slice [::2]: {numbers[::2]}")  

# # Reverse the tuple using slicing
# print(f"Reversed slice [::-1]: {numbers[::-1]}") 


# tuple1 = (1, 2)
# tuple2 = (3, 4)

# Concatenation
# combined_tuple = tuple2 + tuple1
# print(f"Concatenated tuple: {combined_tuple}") 

# Repetition
# repeated_tuple = tuple1 * 3
# print(f"Repeated tuple: {repeated_tuple}") 

# print( tuple1 < tuple2 )

# Membership
# print(f"Is 2 in tuple1? {2 in tuple1}")     
# print(f"Is 5 not in tuple2? {5 not in tuple2}") 


# my_tuple = ("apple", "banana", "cherry")

# Attempting to change an element (will raise TypeError)
# my_tuple[1] = "grape"

# my_tuple_with_list = (1, [2, 3], 4)
# print(f"Original tuple with list: {my_tuple_with_list}") 

# my_tuple_with_list[1].append(5) # Modifying the list INSIDE the tuple
# print(f"Modified tuple with list: {my_tuple_with_list}") 
# This is allowed because you are not changing the tuple itself (i.e., you're not reassigning index 1 to a different object).
# You are changing the *contents* of the list object that index 1 points to.

# a = 5
# b = 10

# c = a

# a = b
# b = c
# print( a, b )

# Swapping variables easily using tuple unpacking
# a = 10
# b = 20
# print(a, b)
# a, b = b, a
# print(a, b)


# a, b = 20, 10 # Python first evaluates (b, a) as a tuple, then unpacks
# print(f"After swap: a={a}, b={b}") 

# Unpacking with * (star operator) for arbitrary remaining elements (Python 3+)
# coordinates = (1, 2, 3, 4, 5, 7, 8, 9, 10)
# *a, b, c, d, e = coordinates
# print(a, b, c, d, e)

# first, *middle, last = coordinates
# print(f"first={first}, middle={middle}, last={last}") 


# my_list = [1, 2, 3]
# my_tuple = tuple(my_list)
# print(f"List to tuple: {my_tuple}, type: {type(my_tuple)}") 

# my_tuple_orig = ("a", "b", "c")
# my_list_from_tuple = list(my_tuple_orig)
# print(f"Tuple to list: {my_list_from_tuple}, type: {type(my_list_from_tuple)}") 


# my_tuple = (1, 2, 3, 2, 4, 2)

# print(f"Count of 2: {my_tuple.count(2)}") 
# print(f"Index of 2: {my_tuple.index(2)}") 

# a = "this is a test class about tuples and it is a good example"
# b = a.split()
# ['this', 'is', 'a', 'test', 'class', 'about', 'tuples', 'and', 'it', 'is', 'a', 'good', 'example']
# c = tuple(b)
# ('this', 'is', 'a', 'test', 'class', 'about', 'tuples', 'and', 'it', 'is', 'a', 'good', 'example')
# print( c.count("is") )

# print(a.count("is"))

# Type Conversion

# a = [1,2,3,4,5]
# a = "Jaipur"
# a = tuple(a)

# print(a)