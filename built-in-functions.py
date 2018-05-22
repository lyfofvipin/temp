import functools
str = input("ENTER A STRING WHOSE WORDS U WANT TO COUNT :: ")
print(list(map(len,str.split(' '))))
number = [0,7,8,9]
print(functools.reduce(lambda a,b:a*10+b,number))
print(list(filter(lambda word :'a' in word,str.split(' '))))
print({y:x for x,y in enumerate(number)})
print (len([y for y,x in enumerate(number) if x == y]))
