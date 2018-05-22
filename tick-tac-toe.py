import os
import sys
f = [' ']*10
def printing(a,b,c):
	for x in range(4):
		if x == 2:
			print(" "*20,"  %c\t|  \t%c\t|  %c" %(f[a],f[b],f[c]) )
		else:
			print(" "*20,"    \t|  \t  \t|    " )
def interface():
	printing(0,1,2)
	print(" "*15,"-"*45)
	printing(3,4,5)
	print(" "*15,"-"*45)
	printing(6,7,8)
def logic(a)	:
	if a % 2 == 0:
		print("   ::::::   PLAYER 2   ::::::   ")
		pos = int(input("Please Enter the posiction from ' 1 - 9 ' :: "))
		pos -= 1
		f[pos] = 'X'
	else:
		print("   ::::::   PLAYER 1   ::::::   ")
		pos = int(input("Please Enter the posiction from ' 1 - 9 ' :: "))
		pos -= 1
		f[pos] = 'O'
def won():
	if (f[0],f[1],f[2]) == ('X','X','X') or (f[3],f[4],f[5]) == ('X','X','X') or (f[6],f[7],f[8]) == ('X','X','X') or (f[0],f[4],f[8]) == ('X','X','X') or (f[2],f[4],f[6]) == ('X','X','X') or (f[0],f[3],f[6]) == ('X','X','X') or (f[1],f[4],f[7]) == ('X','X','X') or (f[2],f[5],f[8]) == ('X','X','X'):
		print("The game is over  :: \n\n    PLAYER 2 IS WINNER ")
		interface()
		sys.exit()
	elif (f[0],f[1],f[2]) == ('O','O','O') or (f[3],f[4],f[5]) == ('O','O','O') or (f[6],f[7],f[8]) == ('O','O','O') or (f[0],f[4],f[8]) == ('O','O','O') or (f[2],f[4],f[6]) == ('O','O','O') or (f[0],f[3],f[6]) == ('O','O','O') or (f[1],f[4],f[7]) == ('O','O','O') or (f[2],f[5],f[8]) == ('O','O','O'):
		print("THE gme is over :: \n\n      PLAYER 1 IS WINNER ")
		interface()
		sys.exit()
	elif (' ' not in f ):
	    print("\n\n\n :::::::::::::  THE MATCH IS DROW  ::::::::::::::::: \n\n\n")
	    sys.exit()
print("\n\n\nTHE SIMPLE RULE OF GAME PLAYER 1 HAS SYMBOL   ' O  ' AND\n\n PLAYER 2 HAS    SYMBOL    'X' ")
print("\n\n\nCHOSE THE POSICTION IN THE BORD :) \n\n\n")
print("Let us Begen our game :====) \n\n\n\n")
for x in range(1,10):
	interface()
	logic(x)
	os.system("clear")
	won()