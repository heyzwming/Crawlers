import requests
url = "http://item.jd.com/7834050.html"
try:
    r = requests.get(url)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text)
except:
    print("fail")
