# What is Inheritance? 

# Inheritance is a fundamental concept in Object-Oriented Programming (OOP) 
# that allows a new class to inherit attributes and methods from an existing class.
# Think of it like a family tree. A child class (the subclass or derived class)
# inherits traits (attributes and methods) from its parent class (the superclass or base class). 
# The subclass can then add its own unique traits or override the inherited ones.
# The Basics of Inheritance

# To create a subclass, you define a new class with the parent class name in parentheses.
# class Parent:
#     pass

# class Child(Parent):
#     pass

# class Vehicle:

#     def __init__(self, brand, color):
#         self.brand = brand
#         self.color = color

#     def display_info(self):
#         print(f"Brand: {self.brand}, Color: {self.color}")

# class Car( Vehicle ):
    
#     def wheels(self):
#         print("Car has 4 wheels")

# my_car = Car("Honda", "White")
# print(my_car.brand)

# super(): Accessing the Parent Class
# The super() function is a special tool used to call methods from the parent class. This is particularly useful when the child class has its own __init__ method and you want to reuse the parent's initialization code.

# class Vehicle:
#     def __init__(self, brand, color):
#         self.brand = brand
#         self.color = color
#         print("Vehicle __init__ called.")

# class Car(Vehicle):
#     def __init__(self, num_wheels):
#         self.num_wheels = num_wheels
#         print("Car __init__ called.")
#         super().__init__("Honda", "White")

#     def car_info(self):
#         print(f"This is a {self.color} {self.brand} with {self.num_wheels} wheels.")


# my_car = Car(4)
# print(my_car.num_wheels)
# my_car.car_info()

# class Vehicle:
#     def __init__(self, brand, color):
#         self.brand = brand
#         self.color = color
#         print("Vehicle __init__ called.")

# class Car(Vehicle):
#     def __init__(self, num_wheels):
#         self.num_wheels = num_wheels
#         print("Car __init__ called.")

#     def set_car_brand_and_color(self, brand, color):
#         super().__init__(brand, color)

#     def car_info(self):
#         print(f"This is a {self.color} {self.brand} with {self.num_wheels} wheels.")

# my_car = Car(num_wheels=4)
# my_car.set_car_brand_and_color(brand="Ford", color="Red")
# my_car.car_info()


# class Vehicle:
#     def __init__(self, brand, color):
#         self.brand = brand
#         self.color = color
#         print("Vehicle __init__ called.")

# class Car(Vehicle):
#     def __init__(self, brand, color, num_wheels):
#         self.num_wheels = num_wheels
#         print("Car __init__ called.")
#         super().__init__(brand, color)

#     def car_info(self):
#         print(f"This is a {self.color} {self.brand} with {self.num_wheels} wheels.")

# my_car = Car(brand="Ford", color="Red", num_wheels=4)
# my_car.car_info()

# Method Overriding

# Method overriding is when a subclass provides its own specific implementation
# of a method that is already defined in its parent class.
# The method in the subclass "overrides" the one in the superclass.

# class Vehicle:
#     def display_info(self):
#         print("This is a generic vehicle.")

# class Car(Vehicle):
#     # This method overrides the one in the parent class
#     def display_info(self):
#         print("This is a specific car.")

# class Boat(Vehicle):
#     # This class inherits and does not override the method
#     pass

# my_car = Car()
# my_boat = Boat()

# my_car.display_info() # Calls the overridden method in Car
# my_boat.display_info() # Calls the inherited method from Vehicle

# Multiple Inheritance

# Python allows a class to inherit from more than one parent class. This is called multiple inheritance.

# class A:
#     pass

# class B:
#     pass

# class C(A, B):
#     pass

# class GasEngine:
#     def start(self):
#         print("Gas engine starting...")

# class ElectricMotor:
#     def charge(self):
#         print("Electric motor charging...")

# class HybridCar(GasEngine, ElectricMotor):
#     def drive(self):
#         self.start()
#         self.charge()
#         print("Hybrid car is driving.")

# my_hybrid = HybridCar()
# my_hybrid.drive()


# Magic Methods: __repr__

# Magic Methods

# a = 34

# class test:
    
#     def __repr__(self):
#         return "<class 'test'>"

# b = test()

# print(a)
# print(b)



# Multiple Inheritance

# Multiple inheritance is when a class inherits from two or more parent classes.
# This allows the child class to combine attributes and methods from all of its parent classes,
# promoting code reuse across different parts of a program.


# class ParentA:
#     def method_A(self):
#         print("Method from Parent A")

#     def test(self):
#         print("Test A")

# class ParentB:
#     def method_B(self):
#         print("Method from Parent B")

#     def test(self):
#         print("Test B")

# class Child(ParentA, ParentB):
#     def method_C(self):
#         print("Method from Child")

#     def test(self):
#         print("Test C")
#         ParentB.test(self)
#         ParentA.test(self)

# # # Create an object of the child class
# child_obj = Child()
# child_obj.method_A()
# child_obj.method_B()
# child_obj.method_C()
# child_obj.test()

# Method Resolution Order (MRO): When a method is called on a child class that has multiple parents, Python follows a specific search order to find the correct method.
# This order is called the Method Resolution Order (MRO). 
# Python searches the child class first, then its parents from left to right, and then their parents, until it finds the method.


# Multi Level

# class ParentA:
#     def method_A(self):
#         print("Method from Parent A")

# class ParentB(ParentA):
#     def method_B(self):
#         print("Method from Parent B")

# class ParentC():
#     def method_C(self):
#         print("Method from Parent B")

# class Child(ParentB, ParentC):
#     def method_D(self):
#         print("Method from Child")

# child_obj = Child()
# child_obj.method_A()
# child_obj.method_B()
# child_obj.method_C()


# Encapsulation is a core principle of Object-Oriented Programming (OOP) that involves bundling data (attributes) and the methods (functions) that operate on that data into a single unit,
# which is the class. 
# It's the practice of hiding the internal state of an object from the outside world and only exposing a controlled interface to interact with it.
# Think of a TV remote control. . The remote's buttons (the public methods) are what you use to interact with it.
# You don't know or need to know about the internal wiring, circuits, or how the infrared signal is generated (the private data and methods). The internal complexity is hidden from you, and you can only change the volume or channel through the exposed interface (the buttons).
# Key Concepts of Encapsulation
#     Data Hiding: Encapsulation restricts direct access to an object's internal data. In Python, this is achieved by convention using a single underscore (_) or, more strictly, with double underscores (__) before an attribute name. These are not truly private but signal to other programmers that the attribute is intended for internal use only.
#     Access Control: All interaction with the object's data happens through its methods. This allows you to control how the data is read (getters) or modified (setters), ensuring that the data remains in a valid state.

# In this example, the BankAcount class encapsulates the _balance data. You can't directly change the balance from outside the class. Instead, you must use the deposit() and withdraw() methods, which contain logic to ensure the operations are valid.

# class BankAccount:
#     def __init__(self, initial_balance):
#         self._balance = initial_balance

#     def get_balance(self):
#         return self._balance

#     def deposit(self, amount):
#         if amount > 0:
#             self._balance += amount
#             print(f"Deposited {amount}. New balance is {self._balance}")
#         else:
#             print("Deposit amount must be positive.")

#     def withdraw(self, amount):
#         if 0 < amount <= self._balance:
#             self._balance -= amount
#             print(f"Withdrew {amount}. New balance is {self._balance}")
#         else:
#             print("Invalid withdrawal amount.")

# class User(BankAccount):
#     self._balance
#     pass

# account = BankAccount(100)

# # Interact with the object through its public methods
# account.deposit(50)
# account.get_balance()
# account.withdraw(25)


# Double underscores (__) are used for a feature called name mangling. This is a specific way Python implements data hiding to prevent name clashes in subclasses, not for creating truly private variables.
# __private_vars (Name Mangling)
# When you name an instance variable with a double underscore prefix (e.g., __balance), 
# Python's interpreter automatically changes the name to _ClassName__balance behind the scenes. This makes it much harder for a subclass or an external user to accidentally overwrite or access the variable, thereby preventing naming conflicts.

# class Car:
#     def __init__(self, brand, mileage):
#         self.__brand = brand
#         self.__mileage = mileage

#     def get_info(self):
#         print(f"This is a {self.__brand} with {self.__mileage} miles.")

# class ElectricCar(Car):
#     _Car__brand
#     def __init__(self, brand, mileage, battery_level):
#         super().__init__(brand, mileage)
#         self.__battery_level = battery_level

#     def get_info(self):
#         print(f"Brand: {self._Car__brand}, Battery: {self.__battery_level}%")

# my_car = Car("Ford", 5000)
# my_electric_car = ElectricCar("Tesla", 10000, 95)

# my_car.get_info()
# my_electric_car.get_info()


# __ vs _

# It's important to understand the difference between the double and single underscore conventions:
#     __var (Double Underscore): Triggers name mangling to prevent naming conflicts in subclasses. It's a way to enforce encapsulation and a form of name protection.
#     _var (Single Underscore): This is just a convention. It signals to other developers that the variable is meant for internal use and should be treated as private, but it doesn't do anything to prevent direct access. This is the more common and preferred way to indicate "privacy" in Python.


# Operator Overloading
# Operator overloading allows you to redefine how standard Python operators (like +, -, *, ==)
# behave for your custom objects. This lets you use these intuitive operators on your own classes, making your code more readable and consistent.
# You implement operator overloading by defining special methods in your class. These methods have names that start and end with double underscores, such as __add__ for the + operator.
#     Syntax: You define a special method in your class that corresponds to the operator you want to overload.

class Car:
    def __init__(self, brand, mileage, speed):
        self.brand = brand
        self.mileage = mileage
        self.speed = speed

    def get_info(self):
        print(f"This is a {self.brand} with {self.mileage} miles.")
    
    def compare(self, right_wala):
        return self.speed > right_wala.speed

    def __gt__(self, another_obj):
        return self.speed > another_obj.speed

    def __add__(self, right_wala):
        return self.speed + right_wala.speed

    def __sub__(self, right_wala):
        return self.speed - right_wala.speed

    def __truediv__(self, right_wala):
        return self.speed / right_wala.speed

my_car = Car("Honda", "60", 120)
rosan_car = Car("BMW", "5", 300)


print( my_car + rosan_car )
print( my_car - rosan_car )
print( my_car / rosan_car )

# +	__add__	p1 + p2
# -	__sub__	p1 - p2
# *	__mul__	p1 * p2
# ==	__eq__	p1 == p2
# <	__lt__	p1 < p2


# class Vector:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     # Overload the + operator
#     def __add__(self, other):
#         # Create a new Vector object with the sum of the components
#         new_x = self.x + other.x
#         new_y = self.y + other.y
#         return Vector(new_x, new_y)

#     def __str__(self):
#         # This method is for string representation (e.g., when you print the object)
#         return f"Vector({self.x}, {self.y})"

# # Create two Vector objects
# v1 = Vector(2, 3)
# v2 = Vector(5, 7)

# # Use the overloaded + operator
# v3 = v1 + v2

# print(v3) # Output: Vector(7, 10)
