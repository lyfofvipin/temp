# A for loop allows you to execute a block of code repeatedly for each item in a sequence 
# or any other iterable object. Think of it as telling Python,
# "For every item in line get the samosa."
# The for loop is incredibly versatile because it works with various Python data structures.

# Iterable: An object that can be iterated over (i.e., it can return its members one by one).
# Common iterables include lists, tuples, strings, dictionaries, and range objects.
# Loop Variable: A temporary variable that takes on the value of each item in the iterable during each iteration of the loop.

# for <variable_name> in <iterator/sequence_datatype>:
    # Code block to execute for each item
    # This code is indented

# data = ["rahul", "rohit", "vikas"]

# counter = 0
# while counter < len(data):
#     print(data[counter])
#     counter += 1

# for student in data:
#     print(student)

  
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

# Print Function 2nd argument
# end="\n" is the default value of the end argument

# print("hello", end="\n")
# word = "Python"
# for x in word: print(x, end="-")

# print()
# print("hello")


# d) Using range() for Numerical Iteration:
# The range() function generates a sequence of numbers, which is very common for loops that need to run a specific number of times or iterate through indices.
#     range(stop): Generates numbers from 0 up to (but not including) stop.
#     range(start, stop): Generates numbers from start up to (but not including) stop.
#     range(start, stop, gap): Generates numbers from start up to (but not including) stop, incrementing by step.

# data = list( range(1, 100, 2) )
# print( data )

# data = list( range(-1, -100, -2) )
# print( data )


# Loop 5 times (0 to 4)

# for i in range(5):
#     print(i)

# for num in range(1, 6):
#     print(num)

# for _ in range(0, 10, 2):
#     print(_)

