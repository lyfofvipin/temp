
# counter = 1

# while counter <= 5:
#     print(counter)
#     counter += 1


# print( f"Final Counter Value is {counter}" )



# sum of 5 numbers

# sum 0
# 1 2 3 4 5
# 1
# sum 0 + 1 = 1
# 2
# sum = 1 + 2 = 3
# 3
# sum = 3 + 3 = 6
# 4
# sum = 6 + 4 = 10
# 5
# sum = 10 + 5 = 15


# counter = 1
# sum = 0

# while counter <= 5:
#     sum = sum + counter
#     print(f"Number is {counter}")
#     print(f"New sum is {sum}")
#     counter += 1

# print(sum)


# counter = 1
# mul = 1

# while counter <= 5:
#     mul = mul * counter
#     print(f"Number is {counter}")
#     print(f"New multiply is {mul}")
#     counter += 1

# print(mul)


# Sum of Even Numbers: Write a program that asks the user to enter a positive integer N. Use a while loop to iterate from 1 up to N. Inside the loop, use an if statement to check if the current number is even. If it is, add it to a running total. Finally, print the sum of all even numbers up to N.

# counter = 1
# sum = 0

# while counter <= 10:

#     if counter % 2 == 0:
#         sum = sum + counter
#         print(counter, sum)
#     counter += 1

# print(sum)



# Use a while loop to keep prompting the user to enter the password until they enter it correctly. Inside the loopU
# Use if-else statements to tell the user if their attempt was "Incorrect password. Try again." or "Password accepted!".
# Limit the number of attempts to 3.
# If the user fails 3 times, print "Account locked.".

# counter = 1
# password = ""

# while counter <= 3 and password != "123":
#     password = input("Enter your password: ")
#     if password == "123":
#         print("Login Done")
#     else:
#         print("Incorrect password")
#     counter += 1

# if counter == 4:
#     print("Account Locked.")



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




