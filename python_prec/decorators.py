# Decorators are an advanced, powerful, and fun topic. They represent a very elegant application of functions in Python.

# Understanding Decorators

# A decorator is a function that takes another function as its input, extends or modifies the behavior of that input function,
# and returns the modified function.
# The goal is to wrap a function with extra functionality without explicitly altering its source code.

# Before introducing the decorator syntax you must understand that in Python, functions are "first-class objects," meaning they can:
# Be assigned to variables:

# def sub(a, b):
#     print(a + b)

# def cal(func, a, b):
#     func(a,b)

# cal( sub, 4,5)

# def greet():
#     print("Hello!")

# def greet_with_name( func ):
#     name = input("Enter Your Name: ")
#     greet()
#     print(name)

# # greet()
# greet_with_name(greet)

# say_hello = greet # Assign the function object itself
# print(greet()) # Output: Hello!

# Be defined inside another function:

# def a():
#     print("A")
#     def b ():
#         print("B")
#     b()
# a()


# def test():
#     a = 4
#     return a

# print(test())


# def outer_function(msg):
#     def inner_function():
#         print(msg)
#     return inner_function


# # greeting is now the 'inner_function' object
# greeting = outer_function("Welcome!")
# greeting()

# The Core Decorator Concept

# def func1():
#     print("test")


# def func2(x): # It has to be a function

#     print("Starting ... ")
#     x()
#     print("Ending ... ")

# func2(func1)


# def func1(func):
#     def wrapper():
#         print(f"Starting ---")
#         func()
#         print(f"Finishing ---")
#     return wrapper

# @func1
# def test():
#     print("test")

# a = func1(test)
# a()
# func1(test)()

# test()


# def dec( func ):

#     def inner( a, b ):
#         if a > b:
#             func( a, b )
#         else:
#             func( b, a )
#     return inner

# @dec
# def sub( a, b ):
#     print( a - b)

# sub(12, 10)





# def func1(func):
#     def wrapper(*args):
#         print(f"Starting ---")
#         result = func(*args)
#         print(f"Finishing ---")
#         return result
#     return wrapper

# @func1
# def func2(a):
#     print(a)

# func2("Vipin")



# def func1(func):
#     def wrapper(*args, **kwargs):
#         print(f"Starting ---")
#         result = func(*args, **kwargs)
#         print(f"Finishing ---")
#         return result
#     return wrapper

# @func1
# def func2(a):
#     print(a)

# func2("Vipin")

# def changecase(func):
#   def myinner():
#     return func().upper()
#   return myinner

# @changecase
# def myfunction():
#   return "Hello Sally"

# print(myfunction())
