import requests

res = requests.get('http://localhost:5000/ping')

if 'pong' not in res.text:
    exit
else:
    print("done")