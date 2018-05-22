class circle():
    pi = 3.14
    def __init__(self,radius = 1):
        self.radius = radius
    def area(self):
        return (self.radius**2) * circle.pi
    def paraeter(self):
        return (self.radius*2)*circle.pi
    def get_radius(new_radius):
        self.radius = new_radius
a = circle(4)
print(a.area())