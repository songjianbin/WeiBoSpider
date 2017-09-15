# -*- coding: utf-8 -*-
import re
import hashlib

def extract_num(text):#提取数字为int
    match_re = re.search('.*?(\d+).*',text)
    if match_re:
        nums = int(match_re.group(1))
    else:
        nums = 0

    return nums

def get_md5(url):
    if isinstance(url,str):
        url = url.encode('utf-8')

    m = hashlib.md5('a'.encode('utf-8'))#增加'a'.encode('utf-8')可以防止被撞库
    m.update(url)
    return m.hexdigest()

if __name__ == '__main__':
    print(get_md5("www.baidu.com"))
    print(get_md5("www.baidu.com1"))

