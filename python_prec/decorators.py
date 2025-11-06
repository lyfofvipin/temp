# Decorators are an advanced, powerful, and fun topic. They represent a very elegant application of functions in Python.

# Understanding Decorators

# A decorator is a function that takes another function as its input, extends or modifies the behavior of that input function,
# and returns the modified function.
# The goal is to wrap a function with extra functionality without explicitly altering its source code.

# Before introducing the decorator syntax you must understand that in Python, functions are "first-class objects," meaning they can:
# Be assigned to variables:


# def greet():
#     return "Hello!"

# say_hello = greet # Assign the function object itself
# print(say_hello()) # Output: Hello!

# Be defined inside another function:

# def a():
#     print("A")
#     def b ():
#         print("B")
#     b()

# a()
    

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
#         result = func()
#         print(f"Finishing ---")
#         return result
#     return wrapper


# @func1
# def func2():
#     print("test")


# @func1
# def func3():
#     print("test1")


# func2()
# func3()



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
