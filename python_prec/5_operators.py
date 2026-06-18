# Arithmetic Operators

# +  Add
# -  Sub
# *  Mul
# /  Div
# %  Modules
# // Floor div
# ** Exponential

# a = 5
# b = 2

# print( 49 ** .33 )


# print ( "*" * 50 )

# a = input("Enter Number: ")
# b = input("Enter Number: ")
# a = float(a)
# b = float(b)
# print( a ** b )

# Priority

# a = 20
# b = -20

# Find the 10% of a given number 
# a = float(input("Enter A Number: "))
# print( (a * 10) / 100 )

# a = 10
# b = 10
# print( f"A={a} and B={b}, a+b = {a+b}" )

# print(  b * a )

# BODMAS
# print ( 2 * 2 + 2 / 2 )

# a = input("Enter A Number: ")
# b = input("Enter A Number: ")

# print( a + b)

# a = "Hello"
# b = "world"

# print( a + b )

# print( "Hello " + "World" )

# *

# print("Hello" * 5)
# print( 3 * "Hello")
# print( "-" * 50 )

# a = input("Enter A number: ") # "2"
# b = input("Enter A number: ") # "3"

# a = int(a) # 2
# b = int(b) # 3

# print( a + b )


# basic pay = 1500
# per cam bonus = 200
# comm = 2% -> .02

# basic_pay = 1500
# num = int(input("Enter Num Of Cam sold: "))
# total_bonus = num * 200
# print( basic_pay, total_bonus )
# total_comm = (total_bonus + basic_pay) * .02
# total_pay = basic_pay + total_bonus + total_comm

# print(total_pay)


# Take 2 number from user and perform -, /, *, +, **, // on them.
# a = int(input("Enter a number: "))
# b = int(input("Enter a number: "))

# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a//b)
# print(a**b)
# print(a%b)

# Comparison Operators

# These are used to compare two values.
# > 	Greater than	a > b
# <	Less than	a < b
# ==	Equal to	a == b
# >=	Greater than or equal to	a >= b
# <=	Less than or equal to	a <= b
# !=	Not equal to	a != b


# > Greater Then
# print(5 > 10)

# < Less Then
# print(50 < 10)

# == Double =
# print(18 == 8)

# != Not =
# print(18 != 18)

# >= Greater Then = 
# print(188 >= 18)

# >= Less Then = 
# print(1 <= 18)


# Short Hand Operators, Assignment Operators
# =     It help us in assigning any datatype to a variable
# +=	Add and assign	a += 3
# -=	Subtract and assign	a -= 2
# *=	Multiply and assign	a *= 2
# /=	Divide and assign	a /= 2
# //=	Floor divide and assign	a //= 2
# %=	Modulus and assign	a %= 3
# **=	Exponential and assign	a *= 2

# a = 4
# a = a + 5

# +=
# a = 4
# a+=5 # a = a + 5

# a = 10
# a = a // 2

# print(10 // 2)

# a = 10
# a = a + 5
# print(a)
# a += 5
# print(a)
# a -= 5
# print(a)
# a **= 3
# print(a)
# a *= 2
# print(a)

# a += 6
# print(a)

# a -= 5
# print(a)

# a /= 5
# print(a)

# a *= 1
# print(a)


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


# Membership Operators

# Test membership in sequences like lists, strings:

# in	True if present	"a" in "cat"
# not in	True if not present	"x" not in "cat"

# a = "I live in India."
# print( "I" not in a )

# Identity Operators

# Check if two variables refer to the same object:

# is	Same object	x is y
# is not	Not the same object	x is not y

# a = 23
# b = 23.0

# print( a is b )


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

# a = 19
# print( a%3 == 0  )

# a = int(input("Enter A Number: "))
# print( a > 18 )

# print( 'A' > 'a' )

# print( "Z" > "BAAA" )

# Logical Operators

# Used to combine expressions:

# and	Logical AND	a and b
# or	Logical OR	a or b
# not	Logical NOT	not a

# print( "" or [] or 0 or None )

# 0, "", [], {}, (), None

# or
# -> Return False only if both the values are False
# -> If both the values are true then it will pick the left one
# -> If all values are false it will select the right most

# Left  |  Right | Output
# True    |  False | True
# False   |  True  | True
# True    |  True  | True
# False   |  False | False


# print( 23 and 25 and "" and 9 and 5 )

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

# a = "x"
# print( a == "a" or a == "e" or a == "i" or a == "o" or a == "u" )


# The Concept Of True And False


# print( True and True and "False" and 321 and True )

# Check a number if that divide by either 3 either 5

# a = 37
# print(a % 3 == 0 or a % 5 == 0)

# Check a number if that divide by both 3 and 5

# a = 45
# print(a % 3 == 0 and a % 5 == 0)


# print( (34 and " ") or (45 and 67) or 93 or (45 and 23) )

# Membership Operators
# Test membership in sequences like lists, strings:

# in	True if present	"a" in "cat"
# not in	True if not present	"x" not in "cat"

# a = "I live in Gujrat."
# print("ive" in a)

# print( "abc" not in "Jaipur is a really nice city." )

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
