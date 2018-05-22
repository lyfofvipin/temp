N = int(input("tell me how much number you have :"))
sum,count = (0,0)
while count < N:
    temp = int(input("enter a number"))
    print("-"*20)
    sum = sum + temp
    count+= 1
temp=float(sum)/N
print(" \n Sum = %f \n" %sum)
print(" \n Average = %f \n" % temp)
