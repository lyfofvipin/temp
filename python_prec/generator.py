# A generator is a function that acts like an iterator but is defined using the 
# yield keyword instead of return.

# The Problem Generators Solve (Memory)

# Imagine you have a function that needs to produce a sequence of one million numbers.

# def mnumber():
#     return list(range(1, 10000001))

# print(mnumber)

# Regular Function	
#  * It calculates all one million numbers, stores them all in a list (or other collection),
# and then returns the entire list at once.
#  * High. All results are held in memory simultaneously.

# Generator Function	
#  * It calculates one number, pauses execution using yield, and returns that number. When asked for the next number, 
# it resumes exactly where it left off. 
#  * Low. Only one result is held in memory at any given time.

# The Magic of yield

# The yield keyword is what defines a generator function. It behaves differently from return:
#     return: Terminates the function completely and sends a value back.
#     yield: Pauses the function, sends a value back, and saves the entire local state (variables, instruction pointer). The next time the function is called (via next()), it resumes from the exact point of the pause.

# def test():
#     yield 1
#     yield 2
#     yield 3
#     yield 4

# print(test())

# def square( number: int) -> list:

#     temp = []
#     for x in range(1, number + 1):
#         temp.append(x * x)
#     return temp

# print(square(50000000000))

# def one_time():
#     return 1
#     return 2

# g = one_time()
# print(g)

# def one_time():
#     yield 1
#     yield 2
#     yield 3
#     yield 4
#     yield 5

# a = one_time()

# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))



# def square( number: int):

#     for x in range(1, number + 1):
#         yield x * x

# for x in square(500000000000):
#     print(x)

def infinite_integers():
    n = 0
    while True:
        yield n
        n += 1

# Get the generator
# integers = infinite_integers()

# You can take values as needed without crashing your memory
# print(next(integers)) # 0
# print(next(integers)) # 1
# print(next(integers)) # 2
# print(next(integers)) # 3
# print(next(integers)) # 4
# print(next(integers)) # 5

# for x in one_time():
#     print(x)

# pk = infinite_integers()

# print(next(pk))
# print(next(pk))


class Counter(object):
    def __init__(self, low, high):
        self.current = low
        self.high = high

    def __iter__(self):
        'Returns itself as an iterator object'
        return self

    def __next__(self):
        'Returns the next value till current is lower than high'
        if self.current > self.high:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1

a = Counter(5, 10)

print(next(a))