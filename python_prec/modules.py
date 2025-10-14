# import folder1.cal as cal

# print( cal.add( 10, 20 ) )
# print( cal.a )

# from folder1.cal import *
# print( add( 10, 20 ) )
# print( mul( 10, 20 ) )
# print( sub( 10, 20 ) )
# print( div( 10, 20 ) )
# print( a )

# import cal as calculator
# print( calculator.mul( 7, 3 ) )


# When you use import, Python looks for the module in a list of directories called the Python Path. 
# This path is stored in the sys.path list.
# import sys
# print(sys.path)

# By default, the Python Path includes:
#     The directory of the script you are currently running.
#     The directories where Python is installed.


#  Using a __init__.py File (The standard practice)
# Python treats a directory as a "package" if it contains a file named __init__.py
# (it can be an empty file). This allows you to import modules from that directory as if it were a package.


# Using  import *


# Write a program that asks the user to enter a positive integer N.
# Use a while loop to iterate from 1 up to N. Inside the loop, 
# Use an if statement to check if the current number is even.
# If it is, add it to a running total. Finally, print the sum of all even numbers up to N.




# def sum_of_even_number( number ):
#     sum = 0
#     for x in range( 2, number + 1 ):
#         if x % 2 == 0:
#             sum += x
#     return sum


# number = int(input("Enter A Number"))
# result = sum_of_even_number(number)
# print(result)

# print(dir( set() ))

# os
# datetime

import os
# print( os.uname() )
print(os.listdir())
