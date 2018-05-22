Day=int(input("enter day :"))
Month=int(input("enter Month :"))
Year=int(input("enter year :"))
Days=int(input("enter number of days you want to add :"))
i=1
while i<=Days:
      Day=Day+1
      if Month==1 or Month==3 or Month==5 or Month==7 or Month==8 or Month==10 or Month==12:
         last=31
      if Month==2 or Month==4 or Month==6 or Month==9 or Month==11 :
           last=30
      if Year%4==0 and Year%100!=0 or Year%400==0 :
           last=28

      if Day>last:
        Day=1
        Month+=1

      if Month>12:
         Month=1
         Year+=1

      i+=1
print(Day,Month,Year)      
