d = {'key' : 'value','key1':234}
print(d)
d['k1'] = 'my'
d['k2'] = 'name'
d['k3'] = 'is'
d['k4'] = 'vipin'
d['k5'] = 'and'
print(d)
print(d.keys())
print(d.values())
print(d.items())
print("keys  \t values")
d.setdefault('lang', []).append('Python')
print(d['lang'])
d.setdefault('lang', []).append('C')
print(d['lang'])
d.setdefault('lang', []).append('C++')
print(d['lang'])