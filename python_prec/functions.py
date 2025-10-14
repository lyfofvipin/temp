
# What is a Function?

# At its core, a function is a reusable block of code that performs a specific task. 
# Think of it as a small, self-contained machine. 
# You give it some input, it does its job, and then it can give you an output.

# Using functions makes your code:
#     Organized: Breaks down a large program into smaller, manageable pieces.
#     Reusable: You can call the same function multiple times without rewriting the code.
#     Easier to read and debug: If something goes wrong, you know exactly which "machine" to check.


# Type Of Functions:
    # Inbuilt Functions
    # Custom Functions

# Defining and Calling a Function

# Every function has two main parts: the definition and the call.

# Defining a Function
# You define a function using the def keyword, 
# followed by the function name, parentheses (), and a colon :
# The code inside the function must be indented.

# Syntax:
# def function_name():
#     print("Hello from inside the function!")

# a = 23
# b = 24
# print(a + b)

# def my_function():
#     print("hi I am the function.")
#     print("hi I am the function.")
#     print("hi I am the function.")


# my_function()


# def: A keyword that tells Python you're defining a new function.
# my_function: A name you choose for your function. It should be descriptive and follow Python's naming conventions (lowercase with underscores).
# (): These hold the function's parameters (inputs). In this basic example, there are no parameters.

# Calling a Function
# To make the function run, you simply "call" it by writing its name followed by parentheses.

# Example:

# def greet():
#     print("Welcome to Python functions!")

# greet()

# Output:
# Welcome to Python functions!

# Parameters and Arguments (Inputs)

# Functions often need to work with different pieces of data. 
# You can pass information into a function using parameters and arguments.
#     Parameters: The names you define in the function's parentheses when you create it. 
#     Arguments: The actual values you pass into the function when you call it.

# Example:

# # 'name' is a parameter
# def greet_person( name ):
#     print(name.upper())

# greet_person( "Vipin" )

# Doc Strings
# def cap_str( name ):

#     """
#     This Function takes a string and it print it's Upper Case
#     """

#     print(name.upper())

# cap_str( "Rohit"  )


# Functions with Multiple Parameters
# You can define a function with multiple parameters, 
# separated by commas. 
# The arguments you pass when calling it will be assigned to the parameters
# in the same order.

# Example:

# def calculate_sum(num1, num2):
#     total = num1 + num2
#     print(f"The sum is: {total}")
    

# # calculate_sum(10, 5)
# calculate_sum(20, 30)

# Output:
# The sum is: 15
# The sum is: 50

# Positional and Keyword Arguments
# You can call a function in different ways based on how you pass arguments.
# Positional Arguments
# The arguments are matched to parameters based on their position or order. This is the method we've used so far.

# Example:

# def display_info(name, age):
#     print(f"Name: {name}, Age: {age}")

# # Order matters here!
# display_info("Charlie", 25) # "Charlie" is assigned to 'name', 25 to 'age'

# Keyword Arguments
# You can specify the argument's name when you pass it, which means the order doesn't matter.

# Example:

# def display_info(name, age, city, collage, number):
#     print(f"Name: {name}, Age: {age}, {city}, {collage}, {number}")

# # display_info("Diana", 30, "Jaipur", "ABC", "8755934")
# display_info( number="865294", city="Jaipur", collage="XYZ", age=30, name="Vipin" )

# Default Arguments
# You can provide a default value for a parameter. If an argument for that parameter is not passed during the function call, the default value will be used. This makes the parameter optional.

# Example:
# def greet_with_default(name, message="Hello"):
#     print(f"{name}, {message}!")

# greet_with_default("Eve") # No message argument provided, so "Hello" is used
# greet_with_default("Frank", "Good morning") # A new message is provided, overriding the default


# def display_info(name, age, course, city="Jaipur", collage="ABC", number=66543):
#     print(f"Name: {name}, Age: {age}, {city}, {collage}, {number}, {course}")

# display_info("vipin", age=23, course="BCA")

# Variable-Length Arguments (*args and **kwargs)
# Sometimes you don't know how many arguments a function will receive. Python handles this with special syntax.
# *args (Non-Keyword Arguments)
# The *args syntax allows a function to accept a variable number of non-keyword arguments. These arguments are bundled into a tuple inside the function.

# Example:

# def calculate_average(*numbers):
#     print(f"The average is: {numbers}")

# # calculate_average(10, 20)
# calculate_average(10, 20, 30, 40, 56, 46, 64, 46, "sdfhsadf", True, ["34r"], {"a": 243266})

# def mix_func( a, c, *b ):
#     print(a)
#     print(b)
#     print(c)

# mix_func(23, 10, 20, 30, 40, 56, 46, 64, 46 )


# Scope Of Variable in Functions

# a = 20
# print(a)

# def set_a():
#     a = 34
#     print(a)

# set_a()
# print(a)

# a = 20
# print(a)

# def set_a():
#     global a
#     a = 34

# set_a()
# print(a)


# Using Seq data types with functions

# a = 10
# def test( data ):
#     data = data + 10
#     print(data)

# test( a )
# print(a)

# a = [1, 2, 3, 4, 5, 6]

# def test( data ):
#     data.append( 7 )
#     print(data)

# test( a )
# print(a)


# **kwargs (Keyword Arguments)

# The **kwargs syntax allows a function to accept a variable number of keyword arguments.
# These are bundled into a dictionary inside the function.

# Example:

# def show_profile(**user_info):
#     print(user_info)

# show_profile(name="Grace", age=28, city="London")


# The return Statement (Output) 

# So far, Our functions have only printed results to the console. To get a value back from a function so you can use it later in your program, you use the return keyword.
# When a return statement is executed, the function immediately stops, and the value specified after return is sent back to where the function was called.

# Example:

# def chota_bacha( item ):
#     print( "Eat Chips" )
#     return item

# b = chota_bacha( "Chips" )
# print(b)

# a = "test"
# b = a.upper()
# print(b)
# print(a)

# a = [1, 3, 5, 1, 4, 2]
# b = a.sort()
# print(b)
# print(a)

# def test( a ):
#     return a

# print( test( 10 ) )


# def square( a ):
#     return a * a

# sq = square(10)
# print(sq)


# def test( number1, number2 ):
#     print(f"Sum of numbers are {number1 + number2}")
#     return number2 + number1
#     print(f"Mul of numbers are {number1 * number2}")

# print(test( 7, 3 ))

#Note: If a function doesn't have a return statement, it implicitly returns the special value None.

# def divide_checker( number ):
#     for x in range(2, number):
#         if number % x == 0:
#             return True
#     return False

# print(divide_checker( 6 ))

# def smallest_deviser( number ):
#     for x in range(2, number):
#         if number % x == 0:
#             return x
#     return number

# print(smallest_deviser( 25 ))

# def add_pos_num():
#     add = 0
#     while True:
#         a = int(input("Enter A number: "))
#         if a > 0:
#             add += a
#         else:
#             return add

# a = add_pos_num()
# print(a)


# Lambda Functions

# A lambda function (also called an anonymous function) is a small, 
# single-expression function that doesn't have a name. 
# You create them when you need a simple function for a short period, 
# typically as an argument to a higher-order function like map(), filter(), or sorted().

# The Syntax
# The syntax is simple and concise: lambda arguments: expression
#     lambda: The keyword used to create a lambda function.
#     arguments: The input arguments, just like in a regular function.
#     expression: A single expression that is evaluated and returned.

# A regular function to add two numbers
# def add(a, b):
#     return a + b

# lambda a, b: a+b
# add = lambda a, b: a + b

# print( add( 2, 3 ) )


# command = "print('hello world')"

# eval(command)

# expression = input("Enter your Exp: ")
# print(eval(expression))

# file = open("tets.py")
# data = file.read()
# eval(data)
