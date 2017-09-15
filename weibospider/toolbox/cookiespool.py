# -*- coding: utf-8 -*-
import requests
import json
COOKIES_POOL = []
while len(COOKIES_POOL) < 1:
   cookies_url = requests.get('http://127.0.0.1:5000/weibo/random')
   COOKIES_POOL.append(json.loads(cookies_url.text))

print(COOKIES_POOL)
