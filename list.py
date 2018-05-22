a = [ 1, 342, 223, 'India', 'Fedora']
print("*"*100)
print(a)
print("*"*100)
print(a[0:-1])
print("*"*100)
print(a[-1])
print("*"*100)
print(a[0::2])
print("*"*100)
a = ['Fedora', 'is', 'cool']
print('cool' in a)
print("*"*100)
print(len(a))
print("*"*100)
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for f in a[::2]:
   print(f)
b = [11,12,13]
print(b)
print(a)
a.append(b)
print(a)
a.extend(b)
print(a)
a.remove([11,12,13])
print(a)