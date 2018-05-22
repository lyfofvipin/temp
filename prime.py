print(">><<"*25)
number=int(input(" \n enter a number you want to cheak \n : "))
print("="*50)
i=2
while number%i != 0 and number > 1:
    i+=1
if i < number or number == 1:
    print(" \n %d is not a  prime number \n "%number)
else :
    print("\n %d is a prime number \n"% number)
print("="*50)    
