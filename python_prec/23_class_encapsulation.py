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
    
#     def __init__(self, initial_balance):
#         super().__init__(initial_balance)

#     def get_balance(self):
#         print( self._balance )


# a = User( 500 )
# a.get_balance()
# print(dir(a))
# a.withdraw(100)
# print( a._balance )

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
#         self.__brand = brand # -> _Car__brand
#         self.__mileage = mileage # -> _Car__mileage

#     def get_info(self):
#         print(f"This is a {self.__brand} with {self.__mileage} miles.")

# class ElectricCar(Car):

#     def __init__(self, brand, mileage, battery_level):
#         super().__init__(brand, mileage)
#         self.__battery_level = battery_level

#     def get_info(self):
#         print(f"Brand: {self._Car__brand}, Battery: {self.__battery_level}%")

# a = ElectricCar("Tata", 10000, 95)
# print(a._Car__mileage)
# a.get_info()
# print(dir(a))
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
