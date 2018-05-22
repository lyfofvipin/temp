number_of_raw = int(input("enter number of raw  : "))
i , j = 1 , 1
while i<=number_of_raw:
    j = 1
    while j <= i:
      print("*", end='')
      j+= 1
    i+= 1  
