# Understanding Recursion
# Recursion is a programming technique where a function calls itself in order to solve a problem.

# import sys
# sys.setrecursionlimit(11)


# def abc():
#     print("In function abc.")
#     return 56

# print(abc())

# def abc():
#     print("In function abc.")
#     abc()
#     return 56
# print(abc())



# def abc( x = 1 ):

#     print(x)
#     if x < 10:
#         abc( x + 1 )
# abc()


# def string_length(s):
#     print(s)
#     if s == "":
#         return 0
#     else:
#         return 1 + string_length(s[1:])

# print(string_length("hello"))


# Sum of a List of Numbers

# Recursion can be used to sum all elements in a list.

# def list_sum(numbers):
#     if not numbers:
#         return 0
#     else:
#         return numbers[0] + list_sum(numbers[1:])

# print(list_sum([1, 2, 3, 4]))


# Factorial Calculation

# The factorial of a number n is n * (n-1) * (n-2) * ... * 1. Recursion is perfect for this.

# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)

# print(factorial(5))


# Fibonacci Sequence

# The Fibonacci sequence is a series where each number is the sum of the two preceding ones.


# def fibonacci(n):
#     if n <= 1:
#         return n
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)

# print(fibonacci(6))


