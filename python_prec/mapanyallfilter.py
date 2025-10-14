# Higher-Order Functions 📚

# A higher-order function is a function that does at least one of the following:
#     Takes one or more functions as arguments.
#     Returns a function as its result.

# This is a fundamental concept in functional programming. Instead of passing data to a function, you pass an action or a behavior (another function) that the higher-order function should perform.

# typing stricttyping

# def div( a : int , b: int ) -> int:
#     return a/b

# def i_can_call_anyone( a, b = 0, c = 1 ):
#     print(a(b, c))

# i_can_call_anyone(div, 10, 5)

# map() 🗺️

# The map() function is a powerful higher-order function 
# that applies a given function to every item of an iterable (like a list) 
# and returns an iterator of the results. 

# Syntax and How It Works
# The syntax is map(function, iterable). It takes two arguments:
#     A function: The action to be performed on each item.
#     An iterable: The collection of items to be processed.

# The map() function returns a map object, which is an iterator. 
# To see the results, you typically convert it to a list using list().

# def square(x):
#     return x * x

# numbers = [1, 2, 3, 4, 5]

# # print( [ x*x for x in numbers ] )

# # Using map() to apply the square function to each number
# squared_numbers = map(square, numbers)
# result = list(squared_numbers)
# print(result)

# def is_even(a):
#     if a % 2 == 0:
#         return True
#     else:
#         return False

# numbers = [1, 2, 3, 4, 5]
# # print( [ is_even(x) for x in numbers ] )
# print(  list(map(is_even, numbers)))


# The filter() function is another higher-order function used to 
# construct an iterator from elements of an iterable for which a given function returns True.
# It "filters out" elements that don't meet a specific condition.

# Syntax and How It Works

# The syntax is filter(function, iterable). It takes two arguments:
#     A function: A function that returns a boolean value (True or False). This is the condition.
#     An iterable: The collection of items to be filtered.

# Like map(), filter() returns a filter object (an iterator), which you usually convert to a list to see the results.

# Example

# Let's say you have a list of numbers and you only want to keep the even numbers.

# def is_even(x):
#     return x % 2 == 0

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# even_numbers = filter(is_even, numbers)
# result = list(even_numbers)
# print(result)

# print( list( filter(is_even, range(1, 101)) ) )

# any() and all() 💡

# These are two built-in higher-order functions that are very useful for checking conditions across an entire iterable. They take a single iterable as an argument and return a single boolean value.

# any()

# The any() function returns True if at least one element in the iterable is True.
# If the iterable is empty, it returns False.

# # Returns True because 2 is a truthy value (non-zero number)
# list1 = [0, 0, [], "", 0, 0]

# # for x in list1:
# #     if x:
# #         print(True)
# #         break
# print(any(list1))


# Returns False because all elements are "falsy"
# list2 = [0, False, '', None]
# print(any(list2))


# all()

# The all() function returns True if all elements of the iterable are True. If the iterable is empty, it returns True.

# Returns True because all elements are truthy (non-zero)
# list1 = [1, 2, 3, 4, 5]
# print(all(list1))

# Returns False because 0 is a falsy value
# list2 = [1, 2, 0, 4, 5]
# print(all(list2))


# from functools import reduce

# reduce(lambda x,y: x*y, range(1,6))

# 1-10

# sum = 0
# for x in range(1, 11):
#     sum += x

# print(sum)


# def add( a, b ):
#     return a+b

# print( reduce( add, range(1,101) ) )

# print( reduce( lambda a, b : a * b , range(1, 101) ) )
