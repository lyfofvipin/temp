# Errors are an unavoidable part of programming. 
# Error handling is the process of anticipating and managing these errors
# so your program doesn't crash unexpectedly. 
# In Python, this is primarily done using exception handling.

# An exception is an event that occurs during the execution of a program that disrupts the normal flow of the program's instructions.

# The try...except Block
# The try...except block is the fundamental tool for handling exceptions. It works like this:
#     The code inside the try block is executed normally.
#     If an exception occurs within the try block, 
#     the rest of the try block is skipped.
#     The program then looks for an except block that matches the type of exception that occurred.
#     The code inside the matching except block is executed.


# try:
#     number = int(input("Enter A number: "))
# except:
#     print("Please Enter Only Integers.")


# try:
#     a = int(input("Enter Number 1: "))
#     b = int(input("Enter Number 2: "))
#     print(a*b)
# except:
#     print("There is an error from our side we are working on fixing it.")

# a = int(input("Enter A number: ")) # 34
# b = int(input("Enter A number: ")) # 0

# try:
#     print( a / b)
# except:
#     print("You Can not divide any number by 0.")

# print('calculation complete.')

# try:
#     a = int(input("Enter Number 1: "))
#     b = int(input("Enter Number 2: "))
#     print( a / b )
# except ZeroDivisionError:
#     print("You Can not divide any number by 0.")

# try:
#     a = int(input("Enter Number 1: "))
#     b = int(input("Enter Number 2: "))
#     print(a/b)
# except ValueError:
#     print("Please enter Numbers only.")
# except ZeroDivisionError:
#     print("Please enter Numbers other then 0.")


# try:
#     # Code that might raise an exception
#     numerator = 10
#     denominator = 0
#     result = numerator / denominator  # This will cause a ZeroDivisionError
#     print(result)
# except ZeroDivisionError:
#     # This code runs if a ZeroDivisionError occurs
#     print("Error: Cannot divide by zero.")
# except ValueError:
#     # This code would run if a ValueError occurred
#     print("Error: Invalid value was provided.")

# In this example, the try block is executed. When the ZeroDivisionError occurs, the program jumps to the corresponding except block and prints the error message.
# The print(result) line is never reached.


# Common Exception Types
# Python has many built-in exceptions to handle different types of errors. It's good practice to handle specific exceptions rather than a general one. Some of the most common exceptions are:
#     ZeroDivisionError: Raised when you divide by zero.
#     TypeError: Raised when an operation is performed on an object of an inappropriate type (e.g., adding a string and an integer).
#     ValueError: Raised when a function receives an argument of the correct type but an inappropriate value (e.g., trying to convert "hello" to an integer with int("hello")).
#     NameError: Raised when a variable is not found.
#     IndexError: Raised when a sequence index is out of range.
#     KeyError: Raised when a dictionary key is not found.
#     FileNotFoundError: Raised when a file cannot be found.

# You can handle multiple exceptions in a single except block using a tuple.


# try:
#     my_list = [0, 1]
#     user_input = int(input("Enter an index: "))
#     print(my_list[user_input])
# except (IndexError, ValueError) as e:
#     print(f"Error Found: {e}")


# Using as e allows you to access the exception object and print its message,
#  which can be useful for debugging.

# You can also use a generic except block without specifying an exception.
# This will catch any exception that occurs. While this is useful as a final catch-all, it can hide bugs, so it's generally best to handle specific exceptions first.

# try:
#     # Some code
#     ...
# except ZeroDivisionError:
#     print("ZeroDivisionError occurred.")
# except Exception as e:
#     # This will catch all other exceptions
#     print(f"A general error occurred: {e}")

# The else and finally Clauses
# The try block can have two optional clauses: else and finally.
#     The else block runs only if the code in the try block completes without any exceptions. This is a great way to separate the code that might fail from the code that depends on it succeeding.
#     The finally block runs no matter what. It's executed whether an exception occurred or not. This is perfect for cleanup operations like closing files or network connections.


# try:
#     a = int(input("Enter A number: "))
# except:
#     print("Type conversion error.")
# else:
#     print("No error")
# finally:
#     print("I will run at all cost.")
"""
this is a test file.
"""

# for x in range(5):
#     print(x)
# else:
#     print("asdfs")

# a = ""
# b = "sadfsfd"
# c = 2324

# print(locals())

# If my_file.txt exists, the else block runs.
# If my_file.txt does not exist, the except block runs.
# In both cases, the finally block runs and closes the file, ensuring resources are properly managed.

# Raising Your Own Exceptions
# Sometimes you want to intentionally stop your program's
# flow if a condition is not met. You can do this using the raise keyword.
# This is useful for validating user input or ensuring data integrity.

# age = 16

# if age >= 18:
#     print("Yes you can vote.")
# else:
#     raise ValueError("No you can not vote.")

# raise IndexError("Bhaiya y number list m h he nahi.")

# a = Exception("Test", "Hello I am test error")
# raise a

# Here, we manually raise a ValueError if the age is invalid. The try...except 
# block can then catch this exception and handle it gracefully.


# def test():

#     """dummy function
#     """
#     try:
#         return 1
#     finally:
#         return 2

# print(test())

# with open('/path/to/some/file/you/want/to/read') as file_1, \
#     open('/path/to/some/file/being/written', 'w') as file_2, \
#     open('/path/to/some/file/being/written', 'w') as file_3:
    # file_2.write(file_1.read())


