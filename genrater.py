import random
def spr(n):
    for x in range(n):
        yield x**2
for x in spr(10):
    print(x)

#def rand(x,y,n):
 #   for r in range(1,n+1):
  #      yield randint(x,y)
#for x in rand(1,5,12):
    #print(x)

d = [12,"we",34]
d = iter(d)
print(next(d))
print(next(d))
print(next(d))