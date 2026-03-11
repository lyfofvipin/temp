class Car:
    def __init__(self, brand, mileage, speed):
        self.brand = brand
        self.mileage = mileage
        self.speed = speed

    def get_info(self):
        print(f"This is a {self.brand} with {self.speed} speed.")
    
    def __gt__(self, right_arg):
        return self.speed > right_arg.speed

    def __lt__(self, right_arg):
        return self.speed < right_arg.speed

    def __eq__(self, right_arg):
        return self.speed == right_arg.speed

    def __ge__(self, right_arg):
        return self.speed >= right_arg.speed
    
    def __add__(self, right_arg):
        return self.speed + right_arg.speed
    
    def equt(self, right_arg):
        return self.speed == right_arg.speed


a = Car("BMW", 10, 200)
b = Car("Honda", 30, 120)

print(a + b)

int