# -*- coding: utf-8 -*-
# @Time    : 2019/7/25 10:47 AM
# @Author  : nJcx
# @Email   : njcx86@gmail.com
# @File    : observer_pattern_dev.py


from test import get
from test import html_detail


header = {'content-type': 'application/json',
          'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '
                        'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.15 Safari/537.36'
          }

api_url= "https://api.threatbook.cn/v3/scene/dns"

api_key = '1111111111111111111111111111111'


class ThreatBook(object):

    def __init__(self, ):

        self.query = {
            "apikey": api_key,
            "resource": "zzv.no-ip.info"
        }

    def ip_detect(self, ip):
        self.query["resource"] = ip
        r = get(url=api_url, header=header, data=self.query)
        html_detail(r)


if __name__ == '__main__':
    test = ThreatBook()

    test.ip_detect(ip='zzv.no-ip.info')
