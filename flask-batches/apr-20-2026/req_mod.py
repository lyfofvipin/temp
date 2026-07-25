import requests

a = requests.get("http://localhost:5000/test")

print(a.json())
