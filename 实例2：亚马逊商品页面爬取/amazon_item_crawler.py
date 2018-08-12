#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import requests


def getHTMLText(url):
    try:
        #kv={'user-agent':'Mozilla/5.0'}
        r=requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        print(r.text)
    except BaseException:
        return "fail "


def main():
    url = "http://amazon.cn/gp/product/B01M8L5Z3Y"
    getHTMLText(url)


if __name__ == '__main__':
    main()
