# Arithmetic Operators

# +  Add
# -  Sub
# *  Mul
# /  Div
# // Floor div
# %  Modules
# ** Exponential

# a = 20
# b = -20

# print(  b * a )

# BODMAS
# print ( 2 * 2 + 2 / 2 )


# print( "Hello " + "World" )
# print( 3 * "Hello" )
# print( "-" * 50.5 )


# a = input("Enter A number: ") # "2"
# b = input("Enter A number: ") # "3"

# a = int(a) # 2
# b = int(b) # 3

# print( a + b )


# Take 2 number from user and perform -, /, * on them.


# Comparison Operators

# These are used to compare two values.
# > 	Greater than	a > b
# <	Less than	a < b
# ==	Equal to	a == b
# >=	Greater than or equal to	a >= b
# <=	Less than or equal to	a <= b
# !=	Not equal to	a != b


# Short Hand Operators, Assignment Operators

# =     It help us in assigning any datatype to a variable
# +=	Add and assign	a += 3
# -=	Subtract and assign	a -= 2
# *=	Multiply and assign	a *= 2
# /=	Divide and assign	a /= 2
# //=	Floor divide and assign	a //= 2
# %=	Modulus and assign	a %= 3
# **=	Exponential and assign	a *= 2

# b = 1
# b **= 5
# b += 10
# b *= 10
# b /= 10
# b %= 10
# print(b)



#  +=
# perform the math operation 80
# assign the new value into the variable


# a = 60
# a += 20
# a = a + 20
# a = 80
# a -= 20

# a **= 10

# a = 60 *60 *60 *60 *60 *60 *60 *60 *60 *60
 
# print(a)





# # It will pick the first true value it got in the eq

# print( 1 or 3 or 43 or 324 or 4 or 89 )

# in and if we got a non true value it will capture that 
# or it will pick the right most

# print( 23 and 4 and 0 or 34 )


# a = 0
# b = None
# c = "Hello"
# d = []

# result = a or b or c and d
# print(result)  # What do you think this will output?


# not 
# a = 0

# print( not a )


# Membership Operators

# Test membership in sequences like lists, strings:

# in	True if present	"a" in "cat"
# not in	True if not present	"x" not in "cat"

# a = "I live in India."

# print( "India" not in a )

# Identity Operators

# Check if two variables refer to the same object:

# is	Same object	x is y
# is not	Not the same object	x is not y

# a = 23

# b = 23.0

# # a = 23
# # b = 23.0

# print( a is not b )


# age = int( input( "Enter Your Age: " ) )

# print( age >= 18 )


# a = 9
# b = 12
# c = 3

# x = a - b / 3 + c * 2 - 1
# y = a - b / (3 + c) * (2 - 1)
# z = a - (b / (3 + c) * 2) - 1








# +, -, /, *, %, //, **

# / -> Always return a float
# % modules 2 / 2 -> 0
# // floor division -> it will always return the integer par of divide
# // -> 19 / 2 -> 9
# ** exponential -> it will give us x ** y
# 2 ** 4 -> 2 * 2 * 2 * 2 -> 16


# +=	Add and assign	a += 3
# -=	Subtract and assign	a -= 2
# *=	Multiply and assign	a *= 2
# /=	Divide and assign	a /= 2
# //=	Floor divide and assign	a //= 2
# %=	Modulus and assign	a %= 3
# **=	Exponentiate and assign	a *= 2

# a = 30

# a **= 5

# print( a )



# Logical Operators

# Used to combine expressions:

# and	Logical AND	a and b
# or	Logical OR	a or b
# not	Logical NOT	not a

# or
# -> Return False only if both the values are False
# -> If both the values are true then it will pick the left one

# Left  |  Right | Output
# True    |  False | True
# False   |  True  | True
# True    |  True  | True
# False   |  False | False

# and
# -> If any value is false It will return the false one
# -> If both the values are true it will pick the right one

# Left  |  Right | Output
# True    |  False | False
# False   |  True  | False
# False   |  False | False
# True    |  True  | True

# number = 70

# print( True )



# Membership Operators

# Test membership in sequences like lists, strings:

# in	True if present	"a" in "cat"
# not in	True if not present	"x" not in "cat"


# a = "Vipin"

# print("v" not in a)


# a = 6
# b = a

# # a alag h
# # b alag h

# a = [ 1, 2 ]
# b = [ 1, 2 ]

# a = b

# print ( a is b )

# a = 9
# b = 12
# c = 3

# x = a - b / 3 + c * 2 - 1
# a - 4.0 + c * 2 -1
# 11 -1
# 10

# y = a - b / (3 + c) * (2 - 1)

# 7



# l * w

# l = int(input("Enter length of the rectangle: "))
# w = int(input("Enter width of the rectangle: "))

# area = l * w

# print( "Area of rectangle is", l * w )

# print( "Parameter of rectangle is", 2 * l * w )

# 3.14*r2

# radius = int(input("Entre radius: "))

# print( "Area of a circle is ", 3.14* radius * radius )

# milk_quantity = int( input("Enter number of thalli:  ") )
# sugar_quantity = int( input("Enter number of suger packets:  ") )

# milk_price = milk_quantity * 10
# sugar_price = sugar_quantity * 20

# print("Total amount is ", milk_price + sugar_price)

# If-Else
