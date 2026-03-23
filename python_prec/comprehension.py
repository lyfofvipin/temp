# One liner if else

num = 5

# if num > 5:
#     print(True)

# if num > 5: print(True)

# if num > 5:
#     print(True)
# else:
#     print(False)

# print( True if num > 5 else False )

# if num % 3 == 0 and num % 5 == 0:
#     print("Both")
# elif num % 3 == 0:
#     print("3")
# else:
#     print("5")

# "both" if num % 3 == 0 and num % 5 == 0 else "3" if  num % 3 == 0 else "5" if num % 5 == 0 else "by none"


# old_list = ( 1, 2, 3, 4, 5, 6, 7 )

# [ what_is_it_we_want_to_do_with_our_variable_name for variable_name in iterator do_this_only_if ]
# print(old_list)
# new_list = [ item + 2 for item in old_list]
# print(new_list)

# print( [ i * -1 for i in range(1, 11) ] )


# squares = []
# for i in range(10):
#     squares.append(i * i)

# print(squares)
# Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


# squares = [i * i for i in range(10)]

# print(squares)
# # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# even_numbers = []
# for i in range(10):
#     if i % 2 == 0:
#         even_numbers.append(i)

# print(even_numbers)
# Output: [0, 2, 4, 6, 8]

# even_numbers = [ i for i in range(10) if i % 2 == 0 ]

# print(even_numbers)
# # Output: [0, 2, 4, 6, 8]

# new_list = []
# for i in range(10):
#     if i % 2 == 0:
#         new_list.append( i * i )
# print(new_list)

# Get the squares of only the even numbers
# squares_of_evens = [i * i for i in range(10) if i % 2 == 0]

# print(squares_of_evens)
# # Output: [0, 4, 16, 36, 64]


# new_list = []
# for i in range(5):
#     if i % 2 == 0:
#         new_list.append("Even")
#     else:
#         new_list.append("Odd")

# print(new_list)
# # Output: ['Even', 'Odd', 'Even', 'Odd', 'Even']


# new_list = ["Even" if i % 2 == 0 else "Odd" for i in range(5)]

# print(new_list)
# # Output: ['Even', 'Odd', 'Even', 'Odd', 'Even']

# students = [13, 40, 56, 90, 15, 80, 56, 43]
# print( [ i for i in students if i >= 33 ] )
# print( [ i for i in students if i < 33 ] )
# print( [ "Pass" if i >= 33 else "Fail" for i in students ] )


# squares_dict = {}
# for i in range(5):
#     squares_dict[i] = i * i

# print(squares_dict)

# print({ x:x*x for x in range(5) })

# data = [ 2, 3, 5, 6, 7, 9 ]
# squares_dict = { i : i*i for i in data }
# print(squares_dict)


# # Create a dictionary of only the even numbers and their squares
# even_squares = {i: i * i for i in range(10) if i % 2 == 0}

# print(even_squares)
# # Output: {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}


# If a key is repeating itself it's value will be override by the new key

# a = { "rohit": 23, "vikas": 14, "aman": 90, "kamal": 56, "said": 87 }
# print({ i:a[i] for i in a if a[i] >= 33 })
