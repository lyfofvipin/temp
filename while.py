number_of_row=int(input("enter the number of row till you want to print :"))
i=1
while i<=number_of_row:
    j=number_of_row
    while j >= i:
        print(j,end = " ")
        j-=1
    print("\n")
    i+=1   
