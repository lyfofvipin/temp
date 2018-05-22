div = lambda a,b : a/b
X = int(input("Enter value of X : "))
res = 0
for x in range(1,X+1):
    res = res+div(X,x)
print("%.2f" % res)