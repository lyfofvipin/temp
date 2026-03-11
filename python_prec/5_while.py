
# while "False":
#     print("Hello World1!")
#     print("Hello World2!")
#     print("Hello World3!")

# counter = 10

# while counter >= 1:
#     print(counter)
#     counter = counter - 1

# Iteration

# counter = 2
# while counter <= 50:
#     print(counter)
#     counter = counter + 2


# counter = 5
# while counter <= 50:
#     print(counter)
#     counter = counter + 5


# 1 - 50
# 50 - 1
# -1 -50
# -50 -1
# odd numbers from 10 - 20
# even numbers from 50 - 80
# 13
# keyboard input and print it's table
# *
# **
# ***
# ****
# *****

# 55555
# 4444
# 333
# 22
# 1

# *****
# ****
# ***
# **
# *

# Take 5 ints from user and show there sum
# Take 5 ints from user and show there multiply
# Give me sum of all the numbers from 1 to 5:
# Give me multiply of all the numbers from 1 to 5:



# counter = 1

# while counter <= 5:

#     print( "*" * counter )
#     counter += 1

# counter = 5

# while counter != 0:

#     print(str(counter) * counter)
#     counter -= 1


# counter = 1
# sum = 0

# while counter <= 5:

#     number = int(input("Enter A Number: "))
#     print(number)

#     sum = sum + number
#     print(sum)

#     counter += 1



# sum = 1
# counter = 1

# while counter <= 5:

#     sum = sum * counter
#     print(sum)

#     counter += 1

# Factorial

# counter = 2

# while counter <= 50:
#     print(counter)
#     counter += 2

# 1, 3, 5, 7, 9, 11, 13, 15, 17.......

# -v counting

# counter = 50

# while counter > 0:

#     if counter % 2 != 0:
#         print(counter)
#     counter -= 1

# print( f"Final Counter Value is {counter}" )


# 1, 2, 3, 4, 5, 6, 7, 8, 9, 10


# Sum of Even Numbers: Write a program that asks the user to enter a positive integer N. 
# Use a while loop to iterate from 1 up to N.
# Inside the loop, use an if statement to check if the current number is even. 
# If it is, add it to a running total. Finally, print the sum of all even numbers up to N.


# number = int(input("Enter A number:"))
# sum = 0
# counter = 1

# while counter <= number:
#     if counter % 2 == 0:
#         sum += counter
#     counter += 1

# print(sum)


# Use a while loop to keep prompting the user to enter the password until they enter it correctly. Inside the loop
# Use if-else statements to tell the user if their attempt was "Incorrect password. Try again." or "Password accepted!".
# Use dummy data like "admin", "1234" for password validation.
# Limit the number of attempts to 3.
# If the user fails 3 times, print "Account locked.".

# counter = 1

# while counter <= 3:

#     username = input("Enter Username: ")
#     password = input("Enter Password: ")

#     if username == "admin" and password == "1234":
#         print("Password Accepted.")
#         break
#     else:
#         print("Incorrect password. Try again.")

#     counter += 1


# if counter == 4:
#     print( "Account locked." )


# Ask the user to enter an integer greater than 1. 
# Use a while loop to find and print the smallest divisor of that number (excluding 1).
# Use an if-else statement to handle the case where the number itself is prime (its smallest divisor will be itself).

# counter = 2

# number = int(input("Enter A Number: "))

# while number > 1 and  number % counter != 0:

#     print(number, counter)
#     counter += 1


# if number == counter:
#     print("Failed to find the smallest divisor as it's a Prime Number.")
# else:
#     print(f"Number is divisible by {counter}")


# Positive Number Accumulator: 
# Write a program that continuously asks the user to enter numbers.
# Use a while loop to keep taking input until the user enters a negative number.
# For each positive number entered, add it to a running total.
# Finally, print the total sum of all positive numbers entered.


# number = 0
# total = 0

# while number >= 0:

#     number = int( input("Enter A number: ")) # -1
#     if number > 0:
#         total = total + number # 150

# print(f"Sum of all values are {total}")

