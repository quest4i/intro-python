import requests


url = "http://headers.jsontest.com"
response = requests.get(url)
data = response.json()
print(type(data))
for item in data:
    print(data[item])