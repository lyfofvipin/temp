# Write a program to print each character of a string on a new line using a loop.
# Write a program to reverse a given string using a while loop.
# Write a program to count the total number of vowels present in a string using a loop.
# Write a program to find and print the total number of spaces inside a string.
# Write a program to copy one string into another string character by character using a loop.

# a = "Hello world"
# b = ""


# i = 0

# while i < len(a):
#     b = b + a[i]
#     i = i + 1

# print(b)


# # * * * *
# # * * * *
# # * * * *
# # * * * *

# # i = 1

# # while i <= 1 :
# #     print( "*" * 5 )
# #     i += 1

# # *
# # * *
# # * * *
# # * * * *
# # * * * * *

# # i = 1

# # while i <= 5 :
# # 	print( "*" * i )
# # 	i += 1


# # * * * * *
# # * * * *
# # * * *
# # * *
# # *

# # i = int(input("Enter A number: "))
# # while i >= 1:
# # 	print( "*" * i )
# # 	i -= 1
    
# #         *
# #       * *
# #     * * *
# #   * * * *
# # * * * * *

# i = 5

# while i >= 1:
# 	print( ' ' * (i - 1), end="")
# 	print( '*' * ( 5 - ( i - 1 ) ) )
# 	i -= 1

# #     *
# #    * *
# #   * * *
# #  * * * *
# # * * * * *

# n = int(input("Enter A number: "))
# i = 1
# while i <= n:
# 	j = 1
# 	print(" " *  (n - i ), end="")
# 	while j <= (i * 2) - 1:
# 		if j % 2 == 0:
# 			print(" ", end="")
# 		else:
# 			print("*", end="")
# 		j += 1
# 	print()
# 	i += 1

# #     *
# #    * *
# #   * * *
# #  * * * *
# # * * * * *
# #  * * * *
# #   * * *
# #    * *
# #     *

# # import os
# # import sys

# # f = [' ']*10
# # def printing(a,b,c):
# # 	for x in range(4):
# # 		if x == 2:
# # 			print(" "*20,"  %c\t|  \t%c\t|  %c" %(f[a],f[b],f[c]) )
# # 		else:
# # 			print(" "*20,"    \t|  \t  \t|    " )
# # def interface():
# # 	printing(0,1,2)
# # 	print(" "*15,"-"*45)
# # 	printing(3,4,5)
# # 	print(" "*15,"-"*45)
# # 	printing(6,7,8)
# # def logic(a)	:
# # 	if a % 2 == 0:
# # 		print("   ::::::   PLAYER 2   ::::::   ")
# # 		pos = int(input("Please Enter the posiction from ' 1 - 9 ' :: "))
# # 		pos -= 1
# # 		f[pos] = 'X'
# # 	else:
# # 		print("   ::::::   PLAYER 1   ::::::   ")
# # 		pos = int(input("Please Enter the posiction from ' 1 - 9 ' :: "))
# # 		pos -= 1
# # 		f[pos] = 'O'
# # def won():
# # 	if (f[0],f[1],f[2]) == ('X','X','X') or (f[3],f[4],f[5]) == ('X','X','X') or (f[6],f[7],f[8]) == ('X','X','X') or (f[0],f[4],f[8]) == ('X','X','X') or (f[2],f[4],f[6]) == ('X','X','X') or (f[0],f[3],f[6]) == ('X','X','X') or (f[1],f[4],f[7]) == ('X','X','X') or (f[2],f[5],f[8]) == ('X','X','X'):
# # 		print("The game is over  :: \n\n    PLAYER 2 IS WINNER ")
# # 		interface()
# # 		sys.exit()
# # 	elif (f[0],f[1],f[2]) == ('O','O','O') or (f[3],f[4],f[5]) == ('O','O','O') or (f[6],f[7],f[8]) == ('O','O','O') or (f[0],f[4],f[8]) == ('O','O','O') or (f[2],f[4],f[6]) == ('O','O','O') or (f[0],f[3],f[6]) == ('O','O','O') or (f[1],f[4],f[7]) == ('O','O','O') or (f[2],f[5],f[8]) == ('O','O','O'):
# # 		print("THE gme is over :: \n\n      PLAYER 1 IS WINNER ")
# # 		interface()
# # 		sys.exit()
# # 	elif (' ' not in f ):
# # 		print("\n\n\n :::::::::::::  THE MATCH IS DROW  ::::::::::::::::: \n\n\n")
# # 		sys.exit()

# # print("\n\n\nTHE SIMPLE RULE OF GAME PLAYER 1 HAS SYMBOL   ' O  ' AND\n\n PLAYER 2 HAS    SYMBOL    'X' ")
# # print("\n\n\nCHOSE THE POSICTION IN THE BORD :) \n\n\n")
# # print("Let us Begen our game :====) \n\n\n\n")
# # for x in range(1,10):
# # 	interface()
# # 	logic(x)
# # 	os.system("clear")
# # 	won()