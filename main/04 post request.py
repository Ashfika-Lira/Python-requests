import requests

r = requests.post('https://httpbin.org/post?a=b', data={'Lira': 'value'})
print(r.text)