#百度的关键词接口
# http://www.baidu.com/s?wd=keyword

import requests


def getHTMLText(keyword):
    try:
        kv = {'wd':keyword}
        r = requests.get("http://www.baidu.com/s",params=kv)
        print(r.request.url)
        r.raise_for_status()
        print(r.text)
    except:
        print("fail")

def main():
    keyword = "python"
    getHTMLText(keyword)
    return 0

if __name__ == '__main__':
    main()