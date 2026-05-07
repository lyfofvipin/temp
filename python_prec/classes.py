# What is a Class?
# A class is a blueprint or a template for creating objects.
# Think of a class as a set of instructions for building something, like the blueprint for a house. 
# The blueprint defines what the house will have—rooms, doors, windows—but it isn't the house itself.

# In Python, a class defines the attributes (data) and methods (behaviors) that all objects of that class will share.
#     Attributes: These are the data or properties of an object. For a Car class, attributes could be color, brand, and mileage.
#     Methods: These are functions that an object can perform. For a Car class, methods could be start_engine(), drive(), or honk_horn().

# Defining a Class
# You define a class using the class keyword, followed by the class name (which, by convention, should start with a capital letter).

# class ClassName:
#     # Class body (attributes and methods)
#     pass # 'pass' is a placeholder for an empty class

# class SocialMedia:   

#     CEO = "Mark"

#     def like(self):
#         print("Liked")

#     def comment(self):
#         print("Commented")

# facebook = SocialMedia()

# print( facebook.CEO )
# facebook.like()

# twitter = SocialMedia()
# twitter.CEO = "Elon Musk"

# print(facebook.CEO)
# print(twitter.CEO)

# def test():
#     print("test")

# test()


# # Creating Objects (Instances) from a Class

# # object_name = ClassName()

# Insta = SocialMedia()
# LinkedIn = SocialMedia()
# Twitter = SocialMedia()
# LinkedIn.CEO = "Ryan"
# Twitter.CEO = "Elon Musk"

# print( Insta.CEO )
# print( LinkedIn.CEO )
# print( Twitter.CEO )

# class car:

#     color = "Black"
#     brand = "Rolls Royce"
#     milage = "3mph"

#     def engin(self):
#         print("RR Engin.")

#     def drive(self):
#         print("Driving")

#     def honk(self):
#         print("Peeeeeeeeeeeeeeeeee")


# a = car()
# b = car()

# # print(a.brand)
# # print(b.brand)

# b.brand = "Honda"
# b.milage = "25mph"

# print(a.brand)
# print(b.brand)
# a.honk()

# Attributes (The "What It Is")
# Attributes are the data or properties associated with an object.
# They store information about a specific instance. 
# Think of them as variables that belong to an object.

# Methods (The "What It Can Do")
# Methods are the functions that belong to a class.
# They define the behaviors or actions an object can perform.
# They are essentially functions that are defined within a class.

# print( dir(a) )

# class Dog:

#     # species = "GS"

#     def __init__(self, abc):
#         print("Bhaiya Object Ban gaya h.")

#     def eat(self):
#         print(self.abc)
#         print(f"hungry right now.")

#     def bark(self):
#         print(f"says woof!")
#         self.abc = 23

# a = Dog(455)
# a.eat()
# a.bark()

# print(dir(Dog))

# class Dog:
#     species = "GS"

#     def __init__(self, name="tom", age=2):
#         self.dog_name = name
#         self.age = age
#         self.is_hungry = True

#     def bark(self):
#         print(f"{self.dog_name} says woof!")

#     def eat(self):
#         if self.is_hungry:
#             print(f"{self.dog_name} is eating...")
#             self.is_hungry = False
#         else:
#             print(f"{self.dog_name} is not hungry right now.")
#             self.is_hungry = True

# my_dog = Dog()
# # my_dog.eat()

# your_dog = Dog("tuffy", 3)
# # your_dog.bark()
# your_dog.eat()


# print(my_dog.species, your_dog.species, third_dog.species)

# Access instance attributes
# print(f"My dog's name is {my_dog.name} and he is {my_dog.age} years old.")

# Access a class attribute
# print(f"Buddy is a member of the {my_dog.species} species.")

# The __init__() Method (The Constructor)
# The __init__() method is a special method in a class. It's automatically called whenever a new object is created.
# Its primary purpose is to initialize the object's attributes with the values you provide. It's often called the constructor.
#     self: This is the first parameter of any method in a class. It's a reference to the specific object that is being created.
#  It allows you to access and modify the object's attributes and methods.


# class Car:


#     def __init__(self, brand="Tata", color="White"):
#         self.brand = brand
#         self.color = color
#         self.engine_status = "off"

#     def start_engine(self):
#         if self.engine_status == "on":
#             print(f"The {self.brand}'s engine is now on.")
#             self.engine_status = "off"
#         else:
#             print(f"The {self.brand}'s engine is now off.")
#             self.engine_status = "on"


# a = Car()
# print(a.brand)
# print(a.color)
# a.start_engine()
# a.start_engine()

# # Create a new Car object, passing arguments to __init__()
# my_car = Car(brand="Toyota", color="Blue")
# your_car = Car(brand="Ford", color="Red")

# print(f"My car is a {my_car.color} {my_car.brand}.")
# print(f"Your car is a {your_car.color} {your_car.brand}.")

# # # Call a method
# my_car.start_engine()
# print(my_car.engine_status)

# Attributes: Class vs. Instance

# It's important to distinguish between two types of attributes:

#     Instance Attributes: These belong to a specific object. They are defined inside __init__() using self.. 
#     Each object has its own unique copy of these attributes.
#     Class Attributes: These belong to the class itself and are shared by all objects of that class. 
#   They are defined directly within the class body but outside any method.

# class GST:

#     TAX_RATE = 18

#     def __init__(self, name):
#         self.name = name

# milk = GST(name="Saras")
# bread = GST(name="Amul")

# print(f"{milk.name} has {milk.TAX_RATE} rate.")
# print(f"{bread.name} has {bread.TAX_RATE} rate.")

# GST.TAX_RATE = 5

# print(f"{milk.name} has {milk.TAX_RATE} rate.")
# print(f"{bread.name} has {bread.TAX_RATE} rate.")

# Methods: Class vs. Instance


class a:

    def __init__(self):
        pass

    def test1():
        print("hi")

    def test(self):
        print("hi")

# a.test1()

class BankAccount:

    BANK_NAME = "SBI"

    def __init__(self, name, mob, age, dob, balance):
        self.name = name
        self.mob = mob
        self.age = age
        self.dob = dob
        self.balance = balance

    def show_info(self):
        print( self.name,
            self.mob,
            self.age,
            self.balance)
        
    def deposit(self, amount):
        if amount < 0:
            print("Invalid Amount")
            exit(1)
        self.balance += amount
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Invalid Amount")
            exit(1)
        self.balance -= amount

vipin = BankAccount("Vipin", 232424243, 23, "23454", 500)

