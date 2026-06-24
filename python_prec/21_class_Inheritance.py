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

# Multiple Inheritance 

# class A:

#     P = 10

# class B:

#     Q = 20

# class C( A, B ):
#     R = 30

# print(dir(C))


# class A:

#     def __init__(self):
#         self.P = 10

# class B:

#     def __init__(self):
#         self.Q = 10

# class C( A, B ):

#     def __init__(self):
#         A.__init__(self)
#         B.__init__(self)
#         self.R = 10

# abc = C()

# print(dir(abc))


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
# print(a.owner_id)


# def a(x):
#     print(x)

# def b(y):
#     print(y)

# def c( x,y ):
#     a(x)
#     b(y)

# c(10, 20)

# class Vehicle:
#     def __init__(self, brand, color):
#         self.brand = brand
#         self.color = color

# class RTO:
#     def __init__(self, number, owner_id):
#         self.number = number
#         self.owner_id = owner_id

# class Car( Vehicle, RTO ):

#     def __init__(self, brand, color, number, owner_id):
#         Vehicle.__init__(self, brand, color)
#         RTO.__init__(self, number, owner_id)

# a = Car("BMW", "Black", "234-234-2342", "Rohit")
# print(dir(a))
# print(a.color)


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

# class ParentA:
#     def method_A(self):
#         print("Method from Parent A")

#     def method_B(self):
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

# child_obj = Child()
# child_obj.method_B()

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

# Create object
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
#         ParentB.show(self)
#         ParentC.show(self)
#         print("Class D")

# child_obj = Child()
# child_obj.show()
# child_obj.method_A()
# child_obj.method_B()
# child_obj.method_C()
