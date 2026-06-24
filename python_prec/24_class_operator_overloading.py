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



