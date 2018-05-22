print(">><<"*25)
number=int(input(" \n enter a number till you want to cheak \n : "))
print("="*50)
j=2
while j <= number :
    i = 2
    while j%i != 0 and j > 1:
        i+=1
    if i < j or j == 1:
        print(" \n %d is not a  prime number \n "%j)
    else :
       print("\n %d is a prime number \n"% j)
    print("="*50)
    j+= 1
