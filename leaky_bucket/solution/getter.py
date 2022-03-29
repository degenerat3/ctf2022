import requests

url = "http://cyberdelia.online/get/object"
bucket_name = "hold-my-secret-stuff-q673c5f6ns"
object_name = "flag.txt"
magic_str = "yldzzf9vi5"

data = {"bucket": bucket_name, "object": "flag.txt", "magic_str": magic_str}

a = requests.post(url, json=data)
print(a.text)