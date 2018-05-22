power = lambda a,b : a**b
div = lambda a,b : a/b
def factorial (a):
    fact = 1
    for x in range(1,a+1) :
        fact = fact * x
    return fact
a = int(input("Enter the value of X :"))
b = int(input("Enter number of staps :"))
result = 1
for x,y in zip([(p*2)-1 for p in range(1,b+1)],[q for q in range(1,b+1)]):
    if y % 2 == 0:
        result = result - div(power(a,x),factorial(x))
    else:
        result = result + div(power(a,x),factorial(x))
print(result)