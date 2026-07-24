def even_filter(data):

    even = []
    for x in data:
        if x % 2 == 0:
            even.append(x)
    return even

a = even_filter([10, 20, 3, 5, 7, 90])
print(a)
