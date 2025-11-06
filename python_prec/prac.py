# a = [
#     [ 1, 2 ],
#     [ 3, 4 ],
#     [ 5, 6 ],
# ]

# b = [
#     [ 7, 8 ],
#     [ 9, 10 ],
#     [ 11, 12 ],
# ]

# c = [
#     [ 0, 0 ],
#     [ 0, 0 ],
#     [ 0, 0 ],
# ]


# if len(a) != len(b):
#     print("Matrix are not of same size so you can add them.")
#     exit(0)

# for i, y in enumerate(a):
#     for j, q in enumerate(y):
#         c[i][j] = a[i][j] + b[i][j]
#         print( a[i][j] + b[i][j] )

# i = 0

# while i < len(a):
#     j = 0
#     while j < len(a[i]):
#         c[i][j] = a[i][j] + b[i][j]
#         j += 1
#     i += 1

# print(c)

# a = [1, 2, 3, 4, 5, 6, 7, 8]

# i = 0
# length = len(a)

# while i < length // 2:

#     last = -1 - i

#     a[i], a[last] = a[last], a[i]

#     i += 1

# print(a)

# Write a function, that replaces all vowels in a string with a specified vowel.

# Output Should Look Like this:
# Examples
# vow_replace("apples and bananas", "u") ➞ "upplus und bununus"
# vow_replace("cheese casserole", "o") ➞ "chooso cossorolo"
# vow_replace("stuffed jalapeno poppers", "e") ➞ "steffed jelepene peppers"
# Notes
# All words will be lowercase.

def vow_replace( data: str, new_word: str ) -> str:
    for x in data:
        if x in "aeiou":
            data = data.replace(x, new_word)
    return data

print(vow_replace("apples and bananas", "u"))