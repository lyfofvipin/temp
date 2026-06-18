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

#     brand = "Maruti"

# class Car(Vehicle):
#     pass

# print(dir(Car))

# print(Car.brand)

# class Vehicle:

#     def __init__(self, brand, color):
#         self.brand = brand
#         self.color = color

#     def display_info(self):
#         print(f"Brand: {self.brand}, Color: {self.color}")

# class Car( Vehicle ):

#     def wheels(self):
#         print("Car has 4 wheels")

# class Bus( Vehicle ):

#     def wheels(self):
#         print("Car has 10 wheels")


# my_car = Car("Honda", "White")
# print(my_car.brand)

# my_bus = Bus("Volvo", "Blue")
# print(my_bus.color)

# my_bus.display_info()


# Method Overriding/Overloading

# class Vehicle():

#     def __init__(self, brand, color):
#         self.brand = brand
#         self.color = color

#     def display_info(self):
#         print(f"Brand: {self.brand}, Color: {self.color}")

# class Car(Vehicle):

#     def __init__(self, wheels):
#         self.wheels = wheels

# a = Vehicle("Honda", "Black")
# a.display_info()
# print(dir(a))

# a = Car(23)
# print(dir(a))
# print(a.wheels)

# class Vehicle():

#     def __init__(self, brand, color):
#         self.brand = brand
#         self.color = color

#     def display_info(self):
#         print(f"Brand: {self.brand}, Color: {self.color}")


# class Car(Vehicle):

#     def __init__(self, wheels):
#         super().__init__("Honda", "White")
#         self.wheels = wheels

# a = Car(4)
# print(dir( a ))


# super(): Accessing the Parent Class
# The super() class is a special tool used to call methods from the parent class. This is particularly useful when the child class has its own __init__ method and you want to reuse the parent's initialization code.

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
# print(dir(my_car))
# my_car.set_car_brand_and_color(brand="Ford", color="Red")
# print(dir(my_car))
# my_car.car_info()


# class Vehicle:
#     def __init__(self, brand, color):
#         self.brand = brand
#         self.color = color

# class Car(Vehicle):
#     def __init__(self, brand, color, num_wheels):
#         self.num_wheels = num_wheels
#         super().__init__(brand, color)

#     def car_info(self):
#         print(f"This is a {self.color} {self.brand} with {self.num_wheels} wheels.")

# my_car = Car(brand="Ford", color="Red", num_wheels=4)
# print(dir(my_car))
# my_car.car_info()

# your_car = Car(brand="BMW", color="Blue", num_wheels=4)
# print(dir(your_car))
# your_car.car_info()


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

# my_car.display_info()
# my_boat.display_info() # Calls the inherited method from Vehicle


# class Vehicle:
#     def __init__(self, brand, color):
#         self.brand = brand
#         self.color = color

# class RTO:
#     def __init__(self, number, owner_id):
#         self.number = number
#         self.owner_id = owner_id

# class Car( Vehicle, RTO ):

#     def __init__(self):
#         Vehicle.__init__(self, "Honda", "White")
#         RTO.__init__(self, 1213142, "Vipin")

# a = Car()

# print(dir(a))

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
#         ParentA.test(self)
#         ParentB.test(self)
#         print("Test C")

# Create an object of the child class

# child_obj = Child()

# print(dir(child_obj))
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

#     def test(self):
#         print("A")

# class ParentB(ParentA):
#     def method_B(self):
#         print("Method from Parent B")

#     def test(self):
#         print("B")

# class Child(ParentB):
#     def method_C(self):
#         print("Method from Parent B")

#     def test(self):
#         ParentA.test(self)
#         ParentB.test(self)
#         print("C")


# obj = Child()
# # print(dir(obj))
# obj.test()

# class A:
#     def show(self):
#         print("Class A")

# class B(A):
#     def show(self):
#         super().show()
#         print("Class B")

# class D(B):
#     def show(self):
#         super().show()
#         print("Class D")

# # Create object
# obj = D()
# obj.show()

# Multiple + Multilevel 

# class ParentA:
#     def method_A(self):
#         print("Method from Parent A")

#     def show(self):
#         print("Class A")

# class ParentB(ParentA):
#     def method_B(self):
#         print("Method from Parent B")

#     def show(self):
#         ParentA.show(self.show)
#         print("Class B")

# class ParentC():
#     def method_C(self):
#         print("Method from Parent B")

#     def show(self):
#         print("Class C")

# class Child(ParentB, ParentC):
#     def method_D(self):
#         print("Method from Child")

#     def show(self):
#         ParentB.show(self.show)
#         ParentC.show(self.show)
#         print("Class D")

# child_obj = Child()
# child_obj.show()
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
#     pass

# account = BankAccount(100)

# print(dir(account))
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

#     def __init__(self, brand, mileage, battery_level):
#         super().__init__(brand, mileage)
#         self.__battery_level = battery_level

#     def get_info(self):
#         print(f"Brand: {self._Car__brand}, Battery: {self.__battery_level}%")

# a = ElectricCar()
# my_car = Car("Ford", 5000)
# my_electric_car = ElectricCar("Tesla", 10000, 95)
# print(dir(my_electric_car))

# my_car.get_info()
# my_electric_car.get_info()


# __ vs _

# It's important to understand the difference between the double and single underscore conventions:
#     __var (Double Underscore): Triggers name mangling to prevent naming conflicts in subclasses. It's a way to enforce encapsulation and a form of name protection.
#     _var (Single Underscore): This is just a convention. It signals to other developers that the variable is meant for internal use and should be treated as private,
# but it doesn't do anything to prevent direct access. This is the more common and preferred way to indicate "privacy" in Python.


# Operator Overloading
# Operator overloading allows you to redefine how standard Python operators (like +, -, *, ==)
# behave for your custom objects. This lets you use these intuitive operators on your own classes, making your code more readable and consistent.
# You implement operator overloading by defining special methods in your class. These methods have names that start and end with double underscores, such as __add__ for the + operator.
#     Syntax: You define a special method in your class that corresponds to the operator you want to overload.

# class Car:
#     def __init__(self, brand, mileage, speed):
#         self.brand = brand
#         self.mileage = mileage
#         self.speed = speed

#     def __add__(self, your_car):
#         return {
#             "name": f"{self.brand}-{your_car.brand}",
#             "speed": self.speed + your_car.speed,
#             "milage": self.mileage + your_car.mileage
#         }

#     def __sub__(self, other):
#         return self.speed - other.speed

#     def __str__(self):
#         return f"{self.brand}-{self.mileage}-{self.speed}"

#     def __len__(self):
#         return self.speed

#     def __dict__(self):
#         {
#             "name": f"{self.brand}",
#             "speed": self.speed,
#             "milage": self.mileage
#         }

#     def get_info(self):
#         print(f"This is a {self.brand} with {self.mileage} miles.")

# my_car = Car("Honda", "60", 120)
# your_car = Car("BMW", "5", 300)

# print( my_car + your_car )

# a = Car("Honda", 60, 100)

# print( a.get_info() )

# print( my_car + your_car )
# print( my_car - your_car )
# print( my_car / your_car )

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



