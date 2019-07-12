from sys import modules

def a1():
    print("I am  A1")

def a2():
    print("I am  A2")

def a3():
    print("I am  A3")

def a4():
    print("I am  A4")

def a5():
    print("I am  A5")


for x in dir():
    module_name = modules[__name__]
    func = getattr(module_name, x)
    if callable(func):
        func()