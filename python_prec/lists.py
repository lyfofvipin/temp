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

# "0123456789"
# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# numbers[0] = 90

# print(numbers)

abc = [ "Vipin", 25, "Jaipur", 302020, True, [ "Test", 43, [23242, [ 234234]] ] ]

print( abc[-1] )

# # print( abc[ 2: ] )

# # print( "abc[ 0 ]"[ 0 ] )
# # print( abc[ 0 ][ 0 ].lower() )

# # print(abc[5][2][1][0])

# # Reference Variable
# a = [ "sdf", 1, 4, 5 ,6  ]

# b = a

# b[0] = "Vipin"

# print( a, b )


# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# # Get elements from index 2 up to (but not including) index 6
# print(f"Slice [2:6]: {numbers[2:6]}")   # Output: Slice [2:6]: [2, 3, 4, 5]

# # Get elements from the beginning up to index 5
# print(f"Slice [:5]: {numbers[:5]}")    # Output: Slice [:5]: [0, 1, 2, 3, 4]

# # Get elements from index 7 to the end
# print(f"Slice [7:]: {numbers[7:]}")    # Output: Slice [7:]: [7, 8, 9]

# # Get a copy of the entire list
# print(f"Full slice [:]: {numbers[:]}") # Output: Full slice [:]: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# # Get every second element
# print(f"Slice [::2]: {numbers[::2]}")  # Output: Slice [::2]: [0, 2, 4, 6, 8]

# # Reverse the list using slicing
# print(f"Reversed slice [::-1]: {numbers[::-1]}") # Output: Reversed slice [::-1]: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]


# my_list = ["apple", "banana", "cherry", "date"]

# Change a single element
# my_list[1] = "grape"
# print(f"Modified single element: {my_list}") # Output: Modified single element: ['apple', 'grape', 'cherry', 'date']

# Change a slice of elements
# my_list[ 0:2 ] = ["apricot", "blueberry"]
# print(f"Modified slice: {my_list}") # Output: Modified slice: ['apricot', 'blueberry', 'cherry', 'date']

# Replace a slice with more or fewer elements (length can change)
# my_list[2:4] = ["elderberry", "fig", "guava"]
# print(f"Replaced slice with different length: {my_list}") # Output: Replaced slice with different length: ['apricot', 'blueberry', 'elderberry', 'fig', 'guava']

# Operations

list1 = [1, 2]
list2 = [3, 4]

# Concatenation
# combined_list = list1 + list2 # [ 1, 2] + [3, 4] = [ 1, 2, 3 ,4 ]
# print(f"Concatenated list: {combined_list}") # Output: Concatenated list: [1, 2, 3, 4]

# # Repetition
# repeated_list = list1 * 3
# print(f"Repeated list: {repeated_list}") # Output: Repeated list: [1, 2, 1, 2, 1, 2]

# Membership
# print(f"Is 2 in list1? {2 in list1}")     # Output: Is 2 in list1? True
# print(f"Is 5 not in list2? {5 not in list2}") # Output: Is 5 not in list2? True

# a = [ 1, 2, 3 , [ 4, 5 ] ]
# print( 5 in a )
# print( [4, 5 ] in a )
# print( 1 in a[-1] )
# print( 5 in a[-1] )


# Methods:

# -ve index values in index method auto do a +1 for ex insert(-1, "xyz") it will add the data to -2 index
# if we give an invalid +ve index value then it will add the data in the end of the list
# if we give an invalid -ve index then it will add the data in the 0 index
# if we have multiple duplicate then the .remove method will only remove the fist accuracy


# my_list = ["apple", "banana", "cherry", "banana"]

# Append
# my_list.append("date")
# print(f"After append: {my_list}") # Output: After append: ['apple', 'banana', 'cherry', 'date']

# Insert
# my_list.insert(1, "grape") # Insert 'grape' at index 1
# print(f"After insert: {my_list}") # Output: After insert: ['apple', 'grape', 'banana', 'cherry', 'date']

# my_list.insert( -1, "mango")
# print(my_list)

# my_list.insert( -50, "guava")
# print(my_list)


# # Remove
# my_list.remove("banana")
# print(f"After remove: {my_list}") # Output: After remove: ['apple', 'grape', 'cherry', 'date']

# my_list = ["apple", "banana", "cherry", "banana"]
# Pop (last item)
# my_list.pop( 1 )
 
# print(my_list)

# print(f"Popped item (last): {popped_item}, List: {my_list}") # Output: Popped item (last): date, List: ['apple', 'grape', 'cherry']


# my_list = ["apple", "banana", "cherry", "banana"]

# # Pop (at index)
# popped_item_at_index = my_list.pop(0)
# print(f"Popped item (index 1): {popped_item_at_index}, List: {my_list}") # Output: Popped item (index 1): grape, List: ['apple', 'cherry']

numbers = [5, 2, 8, 1, 9, 11]

# # Using .sort() (in-place)
# numbers.sort( reverse = True )

# print(numbers) 
# [11, 9, 8, 5, 2, 1]


# # Sorting a list of strings
# words = ["banana", "vipia", "apple", "cherry", "vipin"]
# words.sort( reverse=True )
# print(f"Sorted words: {words}") # Output: Sorted words: ['apple', 'banana', 'cherry']

# Using sorted() (returns new list)
# new_sorted_list = sorted(numbers, reverse=True)
# print(f"New sorted list: {new_sorted_list}") # Output: New sorted list: [1, 2, 5, 8, 9]
# print(f"Original numbers after sorted(): {numbers}") # Output: Original numbers after sorted(): [5, 2, 8, 1, 9]

# sorted_list = sorted("sjhfygr4ikpok093jf09")
# print("".join(sorted_list))

# Reverse sort
# numbers.sort(reverse=True)
# print(f"Reverse sorted in-place: {numbers}") # Output: Reverse sorted in-place: [9, 8, 5, 2, 1]


my_list = [1, 2, 3, 2, 4, 2]

# print(f"Count of 2: {my_list.count(2)}") # Output: Count of 2: 3
# print(f"Count of 67: {my_list.count(67)}") # Output: Index of 4: 4

# my_list = ["apple", "banana", "cherry", "banana"]
# number_of_banana = my_list.count("banana")
# counter = 1
# while counter <= number_of_banana:
#     my_list.remove("banana")
#     counter += 1
# print(my_list)

# Index

# print(my_list.index(4)) # Output: 4
# print(f"Index of 1: {my_list.index(1)}") # Output: Index of 1: 0
# print(f"Index of 2: {my_list.index(2)}") # Output: Index of 2: 1
# print(f"Index of 2: {my_list.index(2, 2)}") # Output: Index of 2: 1


# new_items = [5, 6]
# new_list = [1, 2]

# new_items = new_items + new_list

# new_items.extend( new_list )
# print(new_items)

# my_list = [ 1, 2 ,3, 34, "saa", "abc", "xyz" ]

# print( my_list[ :: -1 ] )
# print(my_list)

# my_list.reverse()
# print(my_list)


# a = [ 1, 2 ,3, 34, "saa", "abc", "xyz" ]
# # b = a.copy()

# # b.pop()

# # print(a)
# # print(b)

# a.clear() # a = []

# print(a)

# counter = 1
# sum = 0
# number_list = []

# while counter <= 10:

#     number = int(input("Enter A Number: "))
#     if number > 0:
#         sum += number
#         counter += 1
#         number_list.append(number)

# print(sum)
# print(number_list)
