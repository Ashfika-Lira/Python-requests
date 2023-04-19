import requests

http_proxy  = "http://iproyal227480Add:K2gceTX@geo.iproyal.com:12321"
https_proxy = "https://iproyal227480Add:K2gceTX@geo.iproyal.com:12321"
ftp_proxy   = "ftp://10.10.1.10:3128"

proxies = {
              "http"  : http_proxy,
              "https" : https_proxy
            }

r = requests.get("https://httpbin.org/get", proxies=proxies)
print(r.text)