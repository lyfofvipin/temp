# What is a Class?
# A class is a blueprint or a template for creating objects.
# Think of a class as a set of instructions for building something, like the blueprint for a house. 
# The blueprint defines what the house will have—rooms, doors, windows—but it isn't the house itself.
# We can use classes to create our custom DataTypes

# In Python, a class defines the attributes (data) and methods (behaviors) that all objects of that class will share.
#     Attributes: These are the data or properties of an object. For a Car class, attributes could be color, brand, and mileage.
#     Methods: These are functions that an object can perform. For a Car class, methods could be start_engine(), drive(), or honk_horn().

# Defining a Class
# You define a class using the class keyword, followed by the class name (which, by convention, should start with a capital letter).

# class my_class:
#     pass # 'pass' is a placeholder for an empty class

# Creating Objects (Instances) from a Class

# object_name = my_class()

# print(type(object_name))

# a = [1,2,3,43,4]
# b = [4,3,2,3,5,3]

# print( a, b )

# class demo:

#     c = ""
#     d = ""

# x = demo()
# y = demo()

# print( dir(x) )

# print(dir(a))

class SocialMedia:   

    CEO = "Mark"

    def like(self):
        print("Liked")

    def comment(self):
        print("Commented")

# facebook = SocialMedia()

# print( facebook.CEO )

# facebook.like()

# a = [ 23, 34, 45, 65, 657 ]


# a = SocialMedia()
# b = SocialMedia()
# c = SocialMedia()
# d = SocialMedia()

# e = [ a, b, c, d ]

# for x in e:
#     print(x.CEO)


# twitter = SocialMedia()
# twitter.CEO = "Elon Musk"
# print(facebook.CEO)
# print(twitter.CEO)

Insta = SocialMedia()
LinkedIn = SocialMedia()
Twitter = SocialMedia()

# a = list()
# c = list()
# b = list()

# print( a )
# print( b )
# print( c )

# a.append(23)

# print( a )
# print( b )
# print( c )


# print( Insta.CEO )
# print( LinkedIn.CEO )
# print( Twitter.CEO )

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

# print(a.brand)
# print(b.brand)

# b.brand = "Honda"
# b.milage = "25mph"

# print(a.brand)
# print(b.brand)
# a.drive()

# class Dog:

#     species = "GS"

#     def eat(self):
#         b = 50
#         print(f"hungry right now.")

#     def bark(self):
#         print(b)
#         print(f"says woof!")

# a = Dog()
# a.eat()
# a.bark()

# print(dir(a))

# Understanding the Self

# class Dog:

#     species = "GS"

#     def eat(self):
#         self.b = 50
#         print(f"hungry right now.")

#     def bark(self):
#         print(self.b)
#         print(f"says woof!")

# a = Dog()
# a.eat()
# a.bark()

# c = Dog()
# c.eat()
# c.bark()


# class Dog:

#     species = "GS"

#     def test(self):
#         self.a = 10
#         self.b = 20
#         self.c = 30
#         self.d = 40

#     def eat(self):
#         self.b = 50
#         print(f"hungry right now.")

#     def bark(self):
#         print(self.b)
#         print(f"says woof!")

# xyz = Dog()
# xyz.test()
# xyz.eat()
# xyz.bark()


# Attributes (The "What It Is")
# Attributes are the data or properties associated with an object.
# They store information about a specific instance. 
# Think of them as variables that belong to an object.

# Methods (The "What It Can Do")
# Methods are the functions that belong to a class.
# They define the behaviors or actions an object can perform.
# They are essentially functions that are defined within a class.


# Constructor
# The __init__() Method (The Constructor)
# The __init__() method is a special method in a class. It's automatically called whenever a new object is created.
# Its primary purpose is to initialize the object's attributes with the values you provide. It's often called the constructor.
#     self: This is the first parameter of any method in a class. It's a reference to the specific object that is being created.
#  It allows you to access and modify the object's attributes and methods.


# class Dog:

#     species = "GS"

#     def test(self):
#         self.a = 10
#         self.b = 20
#         self.c = 30
#         self.d = 40

#     def eat(self):
#         self.b = 50
#         print(f"hungry right now.")

#     def bark(self):
#         print(self.b)
#         print(f"says woof!")

# xyz = Dog()
# xyz.test()
# xyz.bark()

# class Dog:

#     species = "GS"

#     def __init__(self):
#         self.age = 30
#         print("Bhaiya Object Ban gaya h.")

#     def eat(self):
#         self.age = 5
#         print(f"hungry right now.")

#     def bark(self):
#         print(self.age)
#         print(f"says woof!")

# a = Dog()
# a.eat()
# a.bark()

# Constructor with Arguments

# class Dog:

#     species = "GS"

#     def __init__(self, age=2):
#         self.age = age
#         print("Bhaiya Object Ban gaya h.")

#     def eat(self):
#         print(f"hungry right now.")

#     def bark(self):
#         print(self.age)
#         print(f"says woof!")

# a = Dog(15)
# a.bark()

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

# a = Dog("tommy")
# print(a.dog_name)

# my_dog = Dog()
# my_dog.bark()
# my_dog.eat()
# my_dog.eat()
# my_dog.eat()

# your_dog = Dog("tuffy", 3)
# # your_dog.bark()
# your_dog.eat()

# Access instance attributes
# print(f"My dog's name is {my_dog.name} and he is {my_dog.age} years old.")

# Access a class attribute
# print(f"Buddy is a member of the {my_dog.species} species.")

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
# # print(a.brand)
# # print(a.color)
# a.start_engine()
# print(a.engine_status)
# a.start_engine()
# print(a.engine_status)

# a = Car()
# print(dir(a))
# print( dir( Car ) )

# # Create a new Car object, passing arguments to __init__()
# my_car = Car(brand="Toyota", color="Blue")
# your_car = Car(brand="Ford", color="Red")

# print(f"My car is a {my_car.color} {my_car.brand}.")
# print(f"Your car is a {your_car.color} {your_car.brand}.")

# # # Call a method
# my_car.start_engine()
# print(my_car.engine_status)

# Attributes: Class vs. Object/Instance

# It's important to distinguish between two types of attributes:

#     Instance Attributes: These belong to a specific object. They are defined inside __init__() using self.. 
#     Each object has its own unique copy of these attributes.
#     Class Attributes: These belong to the class itself and are shared by all objects of that class. 
#   They are defined directly within the class body but outside any method.


# class Dog:

#     species = "GS"

#     def __init__(self, name="tom", age=2):
#         self.dog_name = name
#         self.age = age
#         self.is_hungry = True

#     def bark(self):
#         print(f"{self.dog_name} says woof!")

# print(dir(Dog))
# print()
# a = Dog()
# print(dir(a))


# class GST:

#     TAX_RATE = 18

#     def __init__(self, name):
#         self.name = name

# milk = GST(name="Saras")
# bread = GST(name="Kanha")
# biskit = GST(name="Parle")

# # print(f"{milk.name} has {milk.TAX_RATE}% tax rate.")
# # print(f"{bread.name} has {bread.TAX_RATE}% tax rate.")

# GST.TAX_RATE = 5

# print(f"{milk.name} has {milk.TAX_RATE}% tax rate.")
# print(f"{bread.name} has {bread.TAX_RATE}% tax rate.")
# print(f"{biskit.name} has {biskit.TAX_RATE}% tax rate.")

# class GST:

#     def __init__(self, name):
#         self.name = name
#         self.TAX_RATE = 18

# milk = GST(name="Saras")
# bread = GST(name="Kanha")
# biskit = GST(name="Parle")

# # print(f"{milk.name} has {milk.TAX_RATE}% tax rate.")
# # print(f"{bread.name} has {bread.TAX_RATE}% tax rate.")

# biskit.TAX_RATE = 5

# print(f"{milk.name} has {milk.TAX_RATE}% tax rate.")
# print(f"{bread.name} has {bread.TAX_RATE}% tax rate.")
# print(f"{biskit.name} has {biskit.TAX_RATE}% tax rate.")

# Methods: Class vs. Object/Instance

# class Demo:

#     def __init__(self):
#         pass

#     def test():
#         print("hi from test")

#     def test1(self):
#         print("hi")

# Demo.test()
# a = Demo()
# a.test1()

# class BankAccount:

#     BANK_NAME = "SBI"

#     def __init__(self, name, mob, age, dob, balance):
#         self.name = name
#         self.mob = mob
#         self.age = age
#         self.dob = dob
#         self.balance = balance

#     def show_info(self):
#         print( self.name,
#             self.age,
#             self.balance)
    
#     def deposit(self, amount):
#             self.balance += amount

#     def withdraw(self, amount):
#         self.balance -= amount


# demo = BankAccount(name="Vipin", mob=111, age=23,
#                 dob="23454", balance=500)
# demo.show_info()
# demo.deposit(100)
# print(demo.balance)
# demo.withdraw(2000)
# print(demo.balance)
# # demo.show_info()

# vipin = BankAccount("Vipin", 212, 23, "3434334", 1000)
# rohit = BankAccount("Rohit", 212, 23, "34343344", 1000)

# vipin.withdraw(500)
# rohit.show_info()


# all_accounts = []

# while True:
#     print( """
#     A. Create New Account
#     B. Check Account Details
#     C. Deposit Money
#     D. Withdraw Money
#     E. Exit
#     """)

#     user_data = input("Enter A Choice: ")

#     match user_data:

#         case "A":
#             name = input("Enter Your Name: ")
#             age = int(input("Enter Your Age: "))
#             mob = input("Enter Your Mob: ")
#             dob = input("Enter Your DOB: ")
            
#             all_accounts.append(
#                 BankAccount(name=name, mob=mob, dob=dob, age=age, balance=500)
#             )

#         case "B":
#             mob = input("Enter Your Mob: ")
#             for x in all_accounts:
#                 if x.mob == mob:
#                     print()
#                     x.show_info()
#                     print()
#         case "C":
#             mob = input("Enter Your Mob: ")
            

# bank_accounts = []
# for x in ["Vipin", "Vikas", "Priya", "Bhaskar"]:
#     bank_accounts.append(
#         BankAccount(x, 232424243, 23, "23454", 500)
#     )
# print(bank_accounts[0].name)
# for x in bank_accounts:
#     print(x.name)


# def search_account(user_data, mob):
#     account = ""
#     for x in user_data:
#         if x.mob == mob:
#             account = x
#     if account:
#         return account
#     else:
#         False

# bank_accounts = []
# while True:

#     print("""
# A: Creating A New Account
# B: For Checking Bank Balance
# C: Deposit
# D: Withdraw
# """)
#     a = input("Enter Your Choice: ")
#     number = input("Enter Your Mob")

#     match a:

#         case "A":
#             name = input("Enter Your Name")
#             age = input("Enter Your Age")
#             dob = input("Enter Your DOB")
        
#             bank_accounts.append(
#                 BankAccount(name, number, age, dob, 500)
#             )

#         case "B":
#             account = search_account(bank_accounts, number)
#             if account:
#                 account.show_info()
#             else:
#                 print("\n --- Bank Account Not Found. --- ")

#         case "C":
#             account = search_account(bank_accounts, number)
#             amount = int(input("Enter Amount: "))    
#             if account:
#                 account.deposit(amount)
#             else:
#                 print("\n --- Bank Account Not Found. --- ")
        
#         case "D":
#             account = search_account(bank_accounts, number)
#             amount = int(input("Enter Amount: "))    
#             if account:
#                 account.withdraw(amount)
#             else:
#                 print("\n --- Bank Account Not Found. --- ")

#         case _:
#             print("Please Enter A  Valid Choice.")



# A bank stores information about many customers. Each customer has their own bank account with personal details and a balance. Instead of creating separate variables for every customer, we use a class to represent a bank account and store all account objects inside a list.
# The program should repeatedly display a menu and allow the user to perform different banking operations.
# Since many operations (like checking balance, depositing money, and withdrawing money) require finding a customer's account first, create a separate function that searches for an account using the customer's mobile number. If the account exists, return the account object; otherwise, indicate that no account was found.

# Functional Requirements

# Create a BankAccount class that stores:

# Customer Name
# Mobile Number
# Age
# Date of Birth
# Account Balance

# The class should provide the following methods:

# Deposit Money
# Accept an amount.
# Add the amount to the current balance.
# Display the updated balance.
# Withdraw Money
# Accept an amount.
# Allow withdrawal only if sufficient balance is available.
# Display the remaining balance.
# If the balance is insufficient, display an appropriate message.
# Display Account Information
# Show all customer details.
# Show the current account balance.

# Menu Operations

# The program should display the following menu repeatedly:

# A. Create New Account
# B. Check Account Details
# C. Deposit Money
# D. Withdraw Money
# E. Exit


# E-Commerce (ShoppingCart)
#     The Real-World Scenario: When shopping online (like on Amazon), a user needs a temporary "container" to hold items they intend to buy. The system needs to dynamically update as items are added or removed, and calculate the final bill with tax.
#     State (Attributes): * user_id: Links this specific cart to a specific logged-in user.
#         items: A collection (like a dictionary) that pairs product names with their respective prices.
#     Behavior (Methods): * add_item & remove_item: Dynamically modify the internal collection of goods based on user actions.
#         calculate_total: Loops through all the items currently in the container, sums up their prices, applies a local sales tax rate, and returns the final checkout cost.

# Hotel Management (HotelRoom)
#     The Real-World Scenario: A hotel front desk clerk needs software to see which rooms are vacant, which are occupied, and how much to charge per night depending on whether the room is a standard suite or a deluxe room.
#     State (Attributes): * room_number: Unique identifier for the physical room (e.g., Room 302).
#         room_type: Keeps track of the category (e.g., "King Suite", "Double Bed").
#         price: The nightly cost for that specific room type.
#         is_occupied: A true/false flag (boolean) representing the room's current availability status.
#     Behavior (Methods): * check_in: Changes the availability flag to occupied, but only after checking to make sure another guest isn't already sleeping there.
#         check_out: Frees up the room state so the front desk knows it is ready to be cleaned and sold again.

# The Real-World Scenario: An app like Uber or Lyft needs to coordinate a trip. It captures where a passenger is, where they want to go, who is driving them, and how much the ride will cost once completed.
# State (Attributes): * rider: The name of the passenger requesting the ride.
#     pickup & dropoff: The starting and ending physical locations.
#     driver: The name of the driver who accepted the trip (initially empty).
#     status: A text string tracking the lifecycle of the trip (e.g., "Searching", "En Route", "Completed").
# Behavior (Methods): * assign_driver: Binds a driver object/name to the request and advances the trip's status.
#     complete_ride: Marks the trip as finished and uses a mathematical formula (Base Fare + Miles Driven) to calculate what the rider should be billed.

# Digital Library (Book)
#     The Real-World Scenario: A library needs to keep track of its physical catalog. If a book is checked out, other patrons cannot borrow it until it is safely returned to the shelves.
#     State (Attributes): * title & author: The core metadata identifying the physical book.
#         isbn: The unique barcoded serial number of that specific copy.
#         is_available: A boolean flag tracking whether the book is sitting on the shelf or sitting in a student's backpack.
#     Behavior (Methods): * borrow_book: Checks the availability flag. If true, it flips the flag to false and logs who took it. If false, it alerts the user that they must wait.
#         return_book: Resets the flag back to true, making it visible and available for the next reader.


# class ShoppingCart:
#     def __init__(self, user_id):
#         self.user_id = user_id
#         self.items = {}  # Format: {item_name: price}

#     def add_item(self, item_name, price):
#         self.items[item_name] = price
#         print(f"Added {item_name} to cart.")

#     def remove_item(self, item_name):
#         if item_name in self.items:
#             del self.items[item_name]
#             print(f"Removed {item_name} from cart.")

#     def calculate_total(self, tax_rate=0.08):
#         subtotal = sum(self.items.values())
#         total = subtotal + (subtotal * tax_rate)
#         return round(total, 2)

# class HotelRoom:
#     def __init__(self, room_number, room_type, price_per_night):
#         self.room_number = room_number
#         self.room_type = room_type
#         self.price = price_per_night
#         self.is_occupied = False

#     def check_in(self):
#         if not self.is_occupied:
#             self.is_occupied = True
#             print(f"Room {self.room_number} is now checked in.")
#         else:
#             print(f"Room {self.room_number} is already occupied!")

#     def check_out(self):
#         if self.is_occupied:
#             self.is_occupied = False
#             print(f"Room {self.room_number} is now vacant and needs cleaning.")
#         else:
#             print(f"Room {self.room_number} is already vacant.")


# class RideRequest:
#     def __init__(self, rider_name, pickup_location, dropoff_location):
#         self.rider = rider_name
#         self.pickup = pickup_location
#         self.dropoff = dropoff_location
#         self.driver = None
#         self.status = "Searching for driver"

#     def assign_driver(self, driver_name):
#         self.driver = driver_name
#         self.status = "Driver en route"
#         print(f"Driver {driver_name} has accepted {self.rider}'s request.")

#     def complete_ride(self, distance_miles):
#         self.status = "Completed"
#         fare = 2.50 + (distance_miles * 1.75)  # Base fare + per mile rate
#         print(f"Ride finished. Total fare billed to {self.rider}: ${fare:.2f}")

# class Book:
#     def __init__(self, title, author, isbn):
#         self.title = title
#         self.author = author
#         self.isbn = isbn
#         self.is_available = True

#     def borrow_book(self, borrower_name):
#         if self.is_available:
#             self.is_available = False
#             print(f"'{self.title}' has been successfully lent to {borrower_name}.")
#         else:
#             print(f"Sorry, '{self.title}' is currently checked out.")

#     def return_book(self):
#         self.is_available = True
#         print(f"'{self.title}' has been returned and placed back on the shelf.")