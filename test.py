fruits = ["apple", "papaya", "banana"]
# Here we are printing spacefic item of list.
print(fruits[0])
print("*"*50)
# Here we are going to check the lenght of list.
print len(fruits)
print("*"*50)
# Here we are going to all item of list.
for fruit in range(len(fruits)):
 print fruits[fruit]
print "*"*50
a = [23, 45, 1]
b = [45,56,78]
# Here we are going add a item in last of list.
a.append(45)
print(a)
print("*"*50)
a.append(464646)
print(a)
print("*"*50)
# Here we are going to add item on some spasific posiction.
a.insert(0, 111)
print(a)
print("*"*50)
a.insert(1, 222)
print(a)
print("*"*50)
# Here we are going to count how many time item is rea.
print(a.count(45))
print("*"*50)
# Here we are going to remove an item from list.
a.remove(464646)
print(a)
print("*"*50)
# Here we are going to reverse the video.
a.reverse()
print(a)
print("*"*50)
print(a[-1])
print("*"*50)
# Here we are going add another string into another.
a.extend(b)
print(a)
print("*"*50)
a.append(b)
print(a)
print("*"*50)
print(a[-1])
print("*"*50)
a.remove(b)
print(a)
print("*"*50)
# Here we are going short our list.
a.sort()
print(a)
print("*"*50)
del a[-1]
print(a)
print("*"*50)
# Here we are going pop from list.
a.pop()
print(a)
print("*"*50)
a.pop(0)
print(a)
print("*"*50)
a = ["Fedora","Debian","Kubuntu","Pardus"]
print(a)
print("*"*50)
a.append("vipin")
print(a)
print("*"*50)
a =[5,6,7,8]
b=[x**2 for x in a]
print(b)
print("*"*50)
b=[x+1 for x in range(9)]
print(b)
print("*"*50)
b=[x*2 for x in range(1,4)]
print(b)
print("*"*50)
b=4,
print type(b)
b = set("abcdefvipin")
print(b)
print("*"*50)
a = set('alacazam')
print a-b
print("*"*50)
print a|b
print("*"*50)
print a&b
print("*"*50)
a = set('alacazam')
a.add('x')
print a
print("*"*50)
a.pop()
print a
print("*"*50)
dictionarie = {'vipin':'me','ombeer':'my friend','nitin':'my bro'}
print dictionarie['vipin']
print("*"*50)
dictionarie['yatender'] = 'my bff'
print dictionarie['yatender']
print("*"*50)
print dictionarie
print("*"*50)
del dictionarie['yatender']
print dictionarie
print("*"*50)
print 'harchand' in dictionarie
print("*"*50)
test = dict((('india','country'),('alwar','distric')))
print test
print("*"*50)
for key, data in dictionarie.items():
 print "%s with %s" % (key,data)
print type(test)
print("*"*50)
dictionarie = {}
dictionarie.setdefault('name',[]).append('nitin')
print dictionarie['name']
print("*"*50)
dictionarie.setdefault('name',[]).append('vipin')
print dictionarie['name']
print("*"*50)
# Enumrating
for x,y in enumerate(['pawan','vipin','nitin','tanuj']) :
    print x,y
print("*"*50)
for x,y in zip(a,b) :
 print("%d and %d"%(x,y))
print("*"*50)
