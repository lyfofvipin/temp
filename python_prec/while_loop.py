# while loo and string

# a = "23wewasnjANSKJNAXjnaAXNKJANSAJNXSAJKNXS232"

# length = len(a)
# i = 10

# count_a = 0

# while i < length:
    
#     if a[i] == "d":
#         count_a += 1

#     i += 1


# if count_a:
#     print(True)
# else:
#     print(False)


# test = "My Name is Vipin."

# count = 0
# i = 0

# while i < len(test):

#     if test[i] not in "aeiouAEIOU":
#         count += 1
#     print(count)

#     i += 1


test = "vipin"

# rev = test[::-1]

# print( test == rev )

rev = ""
length = len(test) - 1

while length >= 0:

    rev += test[length]

    length -= 1

print(rev == test )

