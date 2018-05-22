class complex_class():
    def __init__ (self,a = 0 ,b = 0):
        real,img = a,b
    def inputc(self):
            self.real = int(input("Enter real value:"))
            self.img = int(input("Enter imagnary value:"))
    def __str__(self):
        return "%s + %si"%(self.real,self.img)
    def add(self,a):
        z = complex_class()
        z.real = self.real+a.real
        z.img = self.img+a.img
        return z
    def adding(a,b):
        z = complex_class()
        z.real = a.real+b.real
        z.img = a.img+b.img
        return z
number1 = complex_class()
number2 = complex_class()
number1.inputc()
number2.inputc()
a = number1.add(number2)
print(a)
number2.inputc()
a = complex_class.adding(number1,number2)
print(a)