import requests

def getHTMLText(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        print(r.text)
    except:
        print("fail")


def main():
    url = "http://item.jd.com/7834050.html"
    getHTMLText(url)
    return 0


if __name__ == '__main__':
    main()
