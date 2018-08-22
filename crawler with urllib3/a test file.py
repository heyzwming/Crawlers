#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# Request URL: https://rl.mail.qq.com/cgi-bin/getinvestigate?sid=gKE0HfATm34NX2ox

import urllib.request
import


url = "http://www.iqianyue.com/mypost"
postdata = urllib.parse.urlencode({
    "name": "ceo@iqianyue.com",
    "pass": "aA123456"
}).encode('utf-8')
req = urllib.request.Request(url, postdata)
req.add_header("")

