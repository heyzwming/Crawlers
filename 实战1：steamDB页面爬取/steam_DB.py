#!/usr/bin/env python
# _*_ coding:utf-8 _*_

# steamDatabase的地址：https://steamdb.info/

import requests


def getDB(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        print(r.text)
    except BaseException:
        print("fail")


def main():
    url = "https://steamdb.info/"
    getDB(url)


if __name__ == '__main__':
    main()
