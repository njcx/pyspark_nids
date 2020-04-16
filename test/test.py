# -*- coding: utf-8 -*-
# @Time    : 2019-03-21 16:15
# @Author  : nJcx
# @Email   : njcx86@gmail.com
# @File    : test.py

import requests
try:
    import orjson as json
except ImportError:
    try:
        import ujson as json
    except ImportError:
        import json


def dict_to_json(dict):
    return json.dumps(dict)


def get(url, data=None, header=None):
    params = data
    if not header:
        header = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '
                                'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.15 Safari/537.36'}
        r = requests.get(url, headers=header, params=params)
    else:
        r = requests.get(url, headers=header, params=params)
    return r


def post(url, data=None, header =None):
    data = data
    if not header:
        header = {
            'Content-Type': 'application/json;charset=UTF-8',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36'
                          ' (KHTML, like Gecko) Chrome/59.0.3071.15 Safari/537.36'}
        r= requests.post(url, headers=header, data=data)
    else:
        r = requests.post(url, headers=header, data=data)
    return r


def delete(url, header=None):

    if not header:
        header = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '
                                'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.15 Safari/537.36'}
        r = requests.delete(url, headers=header)
    else:
        r = requests.delete(url, headers=header)
    return r


def put(url, data=None, header =None):
    data = data
    if not header:
        header = {
            'Content-Type': 'application/json;charset=UTF-8',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36'
                          ' (KHTML, like Gecko) Chrome/59.0.3071.15 Safari/537.36'}
        r= requests.put(url, headers=header, data=data)
    else:
        r = requests.put(url, headers=header, data=data)
    return r


def html_detail(r):
    print r.headers
    print 'http_code:'+str(r.status_code)
    try:
        print r.content
    except Exception:
        pass
    try:
        print r.json()
    except Exception:
        pass


if __name__ == "__main__":
    header = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '
                            'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.15 Safari/537.36',
              }
    r = get("http://www.baidu.com", header=header)
    html_detail(r)