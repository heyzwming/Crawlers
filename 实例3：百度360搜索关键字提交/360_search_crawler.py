#!/usr/bin/env python
# _*_ coding:utf-8 _*_

# 百度的关键词接口
# http://www.so.com/s?q=keyword

import requests


def getHTMLText(keyword):
    try:
        kv = {'q': keyword}
        r = requests.get("http://www.so.com/s", params=kv)
        print(r.request.url)
        r.raise_for_status()
        print(r.text)
    except BaseException:
        print("fail")


def main():
    keyword = "python"
    getHTMLText(keyword)
    return 0


if __name__ == '__main__':
    main()
