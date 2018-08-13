#!/usr/bin/env python
# _*_ coding:utf-8 _*_

# 输入 大学排名URL链接
# 输出 大学排名信息的屏幕输出（排名，大学名称，总分）
# 技术路线： requests-bs4
# 定向爬虫： 仅对输入的URL进行爬取，不拓展爬取

# 结构设计
# 步骤1： 从网络上获取大学排名网络内容       getHTMLText()
# 步骤2： 提取网页内容中信息到合适的数据结构  fillUnivList()
# 步骤3： 利用数据结构展示并输出结果         printUnivList()
#
import bs4
import requests
from bs4 import BeautifulSoup


def getHTMLText(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except BaseException:
        return " fali to crawle the web "


def fillUnivList(ulist, html):
    soup = BeautifulSoup(html, "html.parser")
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')
            ulist.append([tds[0].string, tds[1]].string, tds[3].string)


def printUnivList(ulist, num):
    tplt = "{:^10}\t{1:{3}^10}\t{2:^10}"
    print(tplt.format("排名", "学校名称", "总分",chr(12288)))
    for i in range(num):
        u = ulist[i]
        print(tplt.format(u[0], u[1], u[2],chr(12288)))


def main():
    unifo = []
    url = 'http://www.zuihaodaxue.cn/zuihaodaxuepaiming2016.html'
    html = getHTMLText(url)
    fillUnivList(unifo, html)
    printUnivList(unifo, 20)    # 前20 所大学


if __name__ == '__main__':
    main()
