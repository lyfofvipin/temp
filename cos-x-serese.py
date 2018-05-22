div = lambda a,b:a/b
sqr = lambda a,b:a**b
def fact (a):
    factroial = 1
    for x in range(1,a+1):
        factroial = factroial * x
    return factroial
def serese ():
    a = int(input("Enter value of X : "))
    b = int(input("Enter number of steps :: "))
    odd = [ x*2 for x in range(0,b)]
    seres = [x for x in range(1,b+1)]
    res = 1
    for x,y in zip(odd,seres):
        if y % 2 == 0:
            res = res-div(sqr(a,x),fact(x))
        else:
            res = res+div(sqr(a,x),fact(x))
    print(odd,seres)
    return res
print(serese())