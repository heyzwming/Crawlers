#!/usr/bin/env python
# _*_ coding:utf-8 _*_

# 网络图片的爬取
# 网络图片连接的格式：    http://www.example.com/picture.jpg
# 国家地理： http://www.nationalgeographic.com.cn/
# 选取一个图片的Web页面： http://www.ngchina.com.cn/animals/facts/8770.html
# 其中一张图片：    http://image.ngchina.com.cn/2018/0727/20180727123944985.jpg

import requests
import os


def pic_crawler(url, root):
    path = root + url.split('/')[-1]  # 存储地址 + 图片的地址名的最后一段
    try:
        if not os.path.exists(root):  # 判断当前路径是否存在，如果不存在则新建
            os.mkdir(root)
        if not os.path.exists(path):  # 如果图片不存在
            r = requests.get(url)
            with open(path, 'wb') as f:
                f.write(r.content)
                f.close()
                print("file saved!")
        else:
            print("file exist!")

    except BaseException:
        print("fail")


def main():
    url = "http://image.ngchina.com.cn/2018/0727/20180727123944985.jpg"
    root = "C://Users//谢昀臻//Pictures//Saved Pictures//"
    pic_crawler(url, root)


if __name__ == '__main__':
    main()
