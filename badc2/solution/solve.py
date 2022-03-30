import requests

host = "http://maliciouspayload.delivery"

data = {"please": "true"}
url = host + "/get/secret"
a = requests.post(url, json=data)
print(a.text)
