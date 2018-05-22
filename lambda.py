avg = lambda a,b,c,d : (a+b+c+d)/4
print(avg(2,4,6,8))
square = lambda a : a**2
print(square(5))
def fact (a):
    f = 1
    for x in range(1,a+1):
        f *= x;
    return f;
print(fact(5))
power = lambda a,b : a**b
print(power(2,9))
upper_case = lambda a:a.upper()
print(upper_case('a'))
palan = lambda a: a[::-1] == a
print(palan('arora'))
def primes(a):
    for x in range(2,a):
        if a%x == 0 and a != 1:
            return False
        else:
            return True
print(primes(7))
even = lambda a,b : a if (a>b) else b
print(even(22,23))