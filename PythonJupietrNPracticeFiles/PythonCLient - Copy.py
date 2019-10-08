import requests
import json


resp = requests.get('http://127.0.0.1:5000')

print (resp.status_code)
print(resp.text)

resp = requests.get('http://127.0.0.1:5000/greet')

print (resp.status_code)
print(resp.text)

resp = requests.get('http://127.0.0.1:5000/get_time')

print (resp.status_code)
print(resp.text)

resp = requests.get('http://127.0.0.1:5000/get_value')

print (resp.status_code)
print(resp.text)

resp = requests.get('http://127.0.0.1:5000/bye')

print (resp.status_code)
print(resp.text)

resp = requests.get('http://127.0.0.1:5000/bye')

print (resp.status_code)
print(resp.text)
