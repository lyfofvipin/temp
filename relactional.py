class relactional:
    def __init__ (self,a=0,b=1):
        self.num,self.den = a,b
    def __str__(self):
       return "%d/%d"%(self.num,self.den)
    def inputd(self):
       self.num = int(input("Enter value of num : "))
       self.den = int(input("Enter value of den : "))
    def add(self,a):
        z = relactional();
        z.num = self.num*b.den + b.num*self.den
        z.den = self.den*b.den
        return z
    def sub(self,a):
        z = relactional();
        z.num = self.num*b.den - b.num*self.den
        z.den = self.den*b.den
        return z
a = relactional(2,2)
b = relactional()
b.inputd()
c = a.sub(b)
print(c)
c = a.add(b)
print(c)