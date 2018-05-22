def change(b):
    a = 90
    print(a)
a = 9
print("Before the function call ", a)
print("inside change function")
change(a)
print("After the function call ", a)
def high(func, value):
     return func(value)

lst = high(dir, int)
print(lst[-3:])
print(lst)