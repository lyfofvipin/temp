# Jump Statements

# break -> break statement help us to break the flow of a loop when it's executed
# continue -> continue statement is a jump statement that can help us to skip a certain part of the code
# exit() -> Exit function in python help us to terminate the program based on any condition and it also sends a signal back to the computer for analytics.

# counter = 1
# while True:
#     print(counter)
#     counter += 1
#     if counter == 5:
#         break


# number = 49

# counter = 2

# while counter <= number -1:
#     if number % counter == 0:
#         print(counter)
#         break
#     counter += 1


# counter = 1

# while counter <= 10:

#     print(counter)
#     if counter % 2 == 0:
#         continue
#     counter += 1

# name = "vipin"
# counter = 1

# while counter <= 10:

#     if name == "bhaskar":
#         counter += 1
#         print("Hi bhaskar")
#         continue
#     counter += 1
#     print("Hi")

# take 10 number as input from user and sum all the +ve one
# counter = 1
# while counter <= 10:
#     print(counter)
#     if counter == 10:
#         continue
#     counter += 1


# sum = 0

# while True:

#     price = int(input("Enter Item Price: "))
#     if price < 0:
#         continue
#     sum += price
#     print(sum)



# sum = 0

# while True:

#     price = int(input("Enter Item Price: "))
#     if price < 0:
#         break
#     sum += price
#     print(sum)

# print("Total: ", sum)


sum = 0

while True:
    price = int(input("Enter Item Price: "))
    if price < 0:
        exit(8)
    sum += price
    print(sum)

# print("Total: ", sum)


# total = 0

# while True:

#     number = int( input("Enter A number: ")) # -1

#     if number == 0:
#         print("0 is not added")
#         continue

#     print("Doing calculations")
#     if number < 0:
#         exit(1)
#     else:
#         total = total + number

# print(f"Sum of all values are {total}")
# print("hello")
# print("hello")
# print("hello")
# print("hello")

# from mapanyallfilter import div

# print(div( 10, 5))

# from class_Inheritance import product_version

# Formatted String/ FString

# name = "Vipin"
# age = 25
# city = "Jaipur"

# # My name is vipin and age 25 and city is Jaipur.

# print( "My name is ", name, " and age ", age, " and city is ", city, "." )

# print(f"My name is {name} and age is {age} and city is {city}.")

