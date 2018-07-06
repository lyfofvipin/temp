import requests
req = requests.get('https://dgplug.org/irclogs/2018/Logs-2018-07-04-13-29.txt')
with open('sayanclass.txt','w') as fobj
l = [ x[7:] for x in str(req.content).split('\\n') if '*-' in x ]
for x in l:
    fobj.write(x+'\n')
fobj.close
