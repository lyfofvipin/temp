# print("Hello World!")


# print( type(x) )


# result = 5 // 2     # 2
# result = 5 % 2      # 1
# result = 5 ** 2     # 25


# print(result)

# y = -10
# print( x < y )




# a = 45
# b = 0

# # print(a and b)
# # print(a or b) 
# print(not b)  


# x = 10

# x += 5 
# # 15

# x -= 5 
# # 10

# x *= 5 
# # 50

# x /= 5 
# # 10

# x //= 3
# # 3

# x %= 3 
# # 0

# x **= 2
# # 0



# a = "my name is vipin and we are learning python"
# b = "vinit"

# print( b in a )


# x = [1, 2, 3]
# y = x
# z = [1, 2, 3]


# print(x is y)    # True (x and y refer to the same object)
# print(x is z)    # False (x and z are different objects, even with the same content)
# print(x is not z) # True


# print("Hello")

# length = len("Python")
# print(length)           # Output: 6

# data_type = type(10)
# print(data_type)      # Output: <class 'int'>

# converted_int = int("123")
# print(converted_int) # Output: 123

# converted_float = float("123.45")
# print(converted_float) # Output: 123.45

# text = str(123)
# print(text)          # Output: "123"

# value = bool(0)
# print(value)         # Output: False

# user_input = input("Enter your name: ")
# print("Hello, " + user_input)

# numbers = range(5)
# print(list(numbers))  # Output: [0, 1, 2, 3, 4]

# total = sum([1, 2, 3, 4])
# print(total)         # Output: 10

# maximum = max([1, 5, 2, 8])
# print(maximum)       # Output: 8
# minimum = min([1, 5, 2, 8])
# print(minimum)       # Output: 1

# all = min([1, 5, 2, 0])
# print(minimum)       # Output: False
# any = min([1, 0, 0, 0])
# print(minimum)       # Output: True


# str1 = "V"
# result = str1 * 100

# print(result)


# my_string = "0123456789"

# print( my_string[ ::-1 ] )


# text = "  Python is Fun  "
# upper_text = text.upper()       # "  PYTHON IS FUN  "
# lower_text = text.lower()       # "  python is fun  "
# stripped_text = text.strip()     # "Python is Fun"
# index = text.find("Fun")       # 11
# replaced_text = text.replace("Fun", "Awesome") # "  Python is Awesome  "
# words = text.split()          # ['Python', 'is', 'Fun']
# joined_text = "-".join(words)    # "Python-is-Fun"
# formatted_text = "{} is {}".format("Python", "Awesome") # "Python is Awesome"
# f_string = f"{'Python'} is {'Awesome'}"      # "Python is Awesome"


# class Person():

#     def __init__(self, name, age, mob):
#         self.name = name
#         self.age = age
#         self.mob = mob
    
#     def test(self):
#         print(" Hello I am Person.")

# class Student( Person ):

#     def __init__(self, name, age, mob, semester, degree):
#         super().__init__(name, age, mob )
#         self.semester = semester
#         self.degree = degree

#     def test(self):
#         # super().test()
#         print(" Hello I am Student.")


# class Teacher( Person ):

#     def __init__(self, name, age, mob, sal):

#         self.sal = sal

# class Admin( Person ):

#     def __init__(self, name, age, mob, sal):

#         self.sal = sal


# abc = Student("Vipin", 23, 998844545, 5, "BCA")

# print( abc.test() )


# try:
#     a = int( input("Enter A Number: ") )
#     try:
#         print( 100 / a )
#     except ZeroDivisionError:
#         print("Do not enter 0")
# except ValueError:
#     print("Harkat maro bee")


# a = int( input("Enter your age: ") )

# if a > 18:
#     print("yes you can vote")
# else:
#     raise()


# import re

# a = "87.232/sadfsAZ"

# match = re.findall(r"[A-Z]*", a)

# print(match)


# import threading
# import time

# print("Before Function")
# def print_numbers():
#     time.sleep(10)
#     print("In function")

# thread = threading.Thread(target=print_numbers)
# print("After Function")

# thread.start()
# print("Program complete.")

