import requests

r = requests.put("https://httpbin.org/put", data={"a": 1,"b": 3})
# print(r.text)
r = requests.delete('https://httpbin.org/delete')
# print(r.text)
r = requests.head('https://httpbin.org/get')
# print(r.text)
r = requests.options('https://httpbin.org/get')
print(r.text)