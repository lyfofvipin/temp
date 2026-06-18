# A for loop allows you to execute a block of code repeatedly for each item in a sequence 
# or any other iterable object. Think of it as telling Python,
# "For every person in line get a samosa."
# The for loop is incredibly versatile because it works with various Python data structures.

# Iterable: An object that can be iterated over (i.e., it can return its members one by one).
# Common iterables include lists, tuples, strings, dictionaries, and range objects.
# Loop Variable: A temporary variable that takes on the value of each item in the iterable during each iteration of the loop.

# for <variable_name> in <iterator/sequence_datatype>:
    # Code block to execute for each item
    # This code is indented

# a = ( 9, 8, 7, 6, 5 )

# counter = 0

# while counter < len(a):
#     print( a[counter] )
#     counter += 1

# data = ( 9, 8, 7, 6, 5, 1, 2, 3 )

# for x in data:
#     print(x)

# for x in "India":
#     print(x)

# data = ["rahul", "rohit", "vikas"]

# for student in data:
#     print(student.upper())
  
# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#     print(x)

# coordinates = (10, 20, 30)
# for coord in coordinates:
#     print(coord)

# word = "Python"
# for x in word:
#     print(x)

# for x in {1, 2, 3 ,4 ,5 ,5}:
#     print(x)

# a = [ (1,2,3), (3,4,5), (5,6,4), [7,8,7], (9, 10,12) ]

# for x, y, z in a:
#     print( f"X = {x}, Y = {y}, Z = {z}" )

# Print Function 2nd argument
# end="\n" is the default value of the end argument

# print( "hello", end="" )
# print(" world.")

# print("hello", end="\n")
# word = "Python"
# for x in word: print(x, end="-")

# print()
# print("hello")

# for x in [1,2,3,4,5,6,7,8,9,10]:
#     print(x)

# Using range() for Numerical Iteration:
# The range() function generates a sequence of numbers, which is very common in for loops that need to run a specific number of times or iterate through indices.
#     range(stop): Generates numbers from 0 up to (but not including) stop.
#     range(start, stop): Generates numbers from start up to (but not including) stop.
#     range(start, stop, gap): Generates numbers from start up to (but not including) stop, incrementing by step.

# a = range(34, 50, 2)

# print( tuple(a) )


# 1 - 9

# print( [1,2,3,4,5,6,7,8,9,10] )

# print( list(a) )
# print( tuple(range( 20 )) )
# print(set( range( 10 , 30 ) ))

# print( list(range( 1, 10, 3 )) )

# print( list(range( 1, 90, 2 )) )

# data = list( range(1, 100, 2) )
# print( data )

# data = list( range(-1, -100, -2) )
# print( data )


# Loop 5 times (0 to 4)

# for i in range(1, 51):
#     print(i)

# for num in range(1, 6):
#     print(num)

# for _ in range(0, 10, 2):
#     print(_)


# enumerate() enumerate function

# a = [ "a", "b", "c", "d", "e", "f", "g", "h" ]

# print( tuple(enumerate(a)) )

# for x, y in enumerate(a): # for x in ((0, 'a'), (1, 'b'), (2, 'c'), (3, 'd'), (4, 'e'), (5, 'f'), (6, 'g'), (7, 'h'))
#     print(x, y)


# zip() for Parallel Iteration

# The zip() function allows you to iterate over multiple iterables in parallel, pairing up corresponding elements. It stops when the shortest iterable is exhausted.

# names = ["Mohan", "Bob", "Charlie"]
# ages = [30, 24, 35, 56]

# print( list(zip(names, ages)) )

# names = ["Mohan", "Bob", "Charlie", "Vipin"]
# ages = [30, 24, 35]
# cities = ["NY", "LA"]

# data = zip( names, ages, cities )
# print(tuple(data))

# for x in data:
#     print(x)

# a = "abc"
# b = "def"

# for x, y in zip(a, b):
#     print(x, y)

# for name, age, city in zip(names, ages, cities):
#     print(f"{name} is {age} years old and lives in {city}.")

 
# c = {}

# for x, y in zip(a,b):
#     c[x] = y

# print(c)
