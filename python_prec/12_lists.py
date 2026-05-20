# Lists are one of the most fundamental and versatile data structures in Python.
# They are ordered, mutable (changeable) sequences of items. 
# This means you can store a collection of items, the order in which you add them is preserved,
# and you can modify them after they've been created.
# In a List we separate data using , operator

# What is a List?

# Think of a list as a container that can hold various items, like a shopping list or a to-do list.
# Each item in the list has a specific position, called an index.

#     Ordered: The items have a defined order, and that order will not change.
#     Mutable: You can change, add, or remove items after the list has been created.
#     Heterogeneous: Lists can contain items of different data types (integers, strings, floats, even other lists or objects).

# numbers = [ 2334 ,45 ,56 ,67 ,68 ,78 ]
# print( numbers )
# print( numbers[-4] )

# print([ 23, 34 ,45 ,56 ,67 ,68 ,78 ][0])
# print([ 23, 34 ,45 ,56 ,67 ,68 ,78 ])

# number = [12.23, 34, 54.45, 34,234.34]
# print(number)

# data = [ 23, 234.3, True, "vipin", False, [1,2,3] ]
# Data manipulation in list
# data[0] = 90
# print(data)


# a = [ 10, 20, True, "india", False, [1,2,3] ]
# # Data manipulation in list
# a[-1][-1] = 78
# print(a)


# abc = [ "Vipin", 25, "Jaipur", 302020, True, [ "Test", 43, [23242, [ 234234]] ] ]

# abc = [ "Vipin",
#        25,
#        "Jaipur",
#        302020,
#        True,
#        [ "Test", 43, [23242, [ 234234 ]] ] 
#     ]

# print( abc[5][2][-1] )

# a = [ [ [ [ 123 ] ] ] ]
# [ [ [ 123 ] ] ]
# [ [ 123 ] ]
# [ 123 ]
# 123

# print(a[0][0][0][0] )



# Reference Variable

# a = 34
# b = a
# print(a, b)
# a = 23
# print(a, b)

# a = [ "sdf", 1, 4, 5 ,6  ]
# b = a
# print( a, b )
# b[0] = "Vipin"
# print( a, b )

# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Get elements from index 2 up to (but not including) index 6
# print(f"Slice [2:6]: {numbers[2:6]}")   

# # Get elements from the beginning up to index 5
# print(f"Slice [:5]: {numbers[:5]}")    

# Get elements from index 7 to the end
# print(f"Slice [7:]: {numbers[7:]}")    

# # Get a copy of the entire list
# print(f"Slice [:]: {numbers[:]}") 

# # Get every second element
# print(f"Slice [::4]: {numbers[::4]}")  

# # Reverse the list using slicing
# print(f"Reversed slice [::-1]: {numbers[::-1]}") 

# print(f"Slice [1:8:2]: {numbers[-8:-1:2]}")  

# numbers = [123, 34, 5, 23, 5, 23, 566, 88, 98]
# print(numbers[-3: -8 : -2])

my_list = ["apple", "banana", "cherry", "date"]
# print(my_list[1][2:4])

# Change a single element
# my_list[1] = "grape"
# print(f"Modified single element: {my_list}") 

# Change a slice of elements
# my_list[ 0:2 ] = ["mango", "blueberry"]
# print(f"Modified slice: {my_list}") 
# Change a slice of elements
# my_list[ 0:3 ] = ["mango", "blueberry"]
# print(f"Modified slice: {my_list}") 

# Replace a slice with more or fewer elements (length can change)
# my_list[2:4] = ["mango", "orange", "guava"]
# print(f"Replaced slice with different length: {my_list}") 

# Operations

# list1 = [1, 2]
# list2 = [3, 4]

# Concatenation
# combined_list = list1 + list2 
# print(f"Concatenated list: {combined_list}") 

# Repetition
# repeated_list = list1 * 3
# print(f"Repeated list: {repeated_list}") 

# Membership
# print(f"Is 2 in list1? {2 in list1}")     
# print(f"Is 5 not in list2? {5 not in list2}")

# a = [ 1, 2, 3 , [ 4, 5 ] ]

# print( 5 in a )
# print( 5 in a[-1] )
# print( [4, 5 ] in a )


# Identity operator

# a = [1, 2]
# b = a
# print(a is not b)


# Methods:
# Insert
# if we give an invalid +ve index value then it will add the data in the end of the list
# if we give an invalid -ve index then it will add the data in the 0 index
# -ve index values in index method auto do a +1 for ex insert(-1, "xyz") it will add the data to -2 index

# if we have multiple duplicate then the .remove method will only remove the fist accuracy


# my_list = ["apple", "banana", "cherry", "banana", 123, [1, 2]]

# Append
# my_list.append("date")
# print(my_list)

# Insert
# my_list.insert(-345, "grape")
# print(f"After insert: {my_list}") 

# my_list.insert( -2, "mango")
# print(my_list)

# Remove
# my_list.remove("apple")
# print(f"After remove: {my_list}") 

# a = 23
# print(a)

# del a
# print(a)

# del my_list[-1]
# print(f"After remove: {my_list}") 

# my_list = ["apple", "banana", "cherry", "banana"]
 # Pop (last item)
# my_list.pop( 0 )
# print(my_list)

# print(f"Popped item (last): {popped_item}, List: {my_list}") 


# my_list = ["apple", "banana", "cherry", "banana"]

# print(my_list.pop())
# print(my_list)

# a = "vipin"
# print(a.upper())
# print(a)


# Pop (at index)
# popped_item_at_index = my_list.pop(0)
# print(f"Popped item (index 1): {popped_item_at_index}, List: {my_list}") 

# numbers = [5, 2, 8, 1, 9, 11]

# Using .sort() (in-place)
# numbers.sort( reverse=True )
# print(numbers)

# print(numbers) 
# [11, 9, 8, 5, 2, 1]

# # Sorting a list of strings
# words = ["banana", "Vipia", "apple", "cherry", "vipin"]
# words.sort( reverse= True )
# print(f"Sorted words: {words}") 

# Using sorted() (returns new list)
# new_sorted_list = sorted(numbers, reverse=True)
# print(f"New sorted list: {new_sorted_list}") 
# print(f"Original numbers after sorted(): {numbers}") 

# sorted_list = sorted("sjhfygr4ikpok093jf09")
# print("".join(sorted_list))

# Reverse sort
# numbers.sort(reverse=True)
# print(f"Reverse sorted in-place: {numbers}") 


# my_list = [1, 2, 3, 2, 4, 2]

# print(f"Count of 2: {my_list.count(2)}") 
# print(f"Count of 67: {my_list.count(67)}") 

# my_list = ["apple", "banana", "cherry", "banana"]
# number_of_banana = my_list.count("banana")
# print(number_of_banana)

# counter = 1
# while counter <= number_of_banana:
#     my_list.remove("banana")
#     counter += 1
# print(my_list)

# Index
# print(my_list.index(2)) 
# print(f"Index of 1: {my_list.index(1)}") 
# print(f"Index of 2: {my_list.index(2)}") 
# print(f"Index of 2: {my_list.index(2, 2)}") 


# a = [5, 6]
# b = [1, 2]

# a.append(b)
# print(a)

# my_list = [ 1, 23443 ,334, 34 ]

# # print( my_list[ :: -1 ] )
# # print(my_list)

# my_list.reverse()
# print(my_list)

# a = [ 34, 34,5 ,23, 12, 565 ]
# b = a.copy()
# b.append(342)
# print(a)
# print(b)

# a = [ 34, 34,5 ,23, 12, 565 ]
# a.clear()
# a=[]
# print(a)

# a = [ 1, 2 ,3, 34, "saa", "abc", "xyz" ]

# a.clear() # a = []
# print(a)

# counter = 1
# number_list = []

# while counter <= 10:

#     number = int(input("Enter A Number: "))
#     if number > 0:
#         counter += 1
#         number_list.append(number)

# print(number_list)


# "".join()
# print(b)

# a = ['my', 'name', 'is', 'vipin']

# b = "------".join(a)

# print(b)




# a = """I am from jaipur
# And Jaipur Is In Raj
# I Live In India"""

# a = ['I am from jaipur\nAnd Jaipur Is ', ' Raj\nI Live ', ' ', 'dia']

# print(a.split("In"))

# a = ['20', '5', '2026']

# print( "In".join( a ) )


# a = "ABCDEFGH"
# print( "-".join(a) )
