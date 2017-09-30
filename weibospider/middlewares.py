# -*- coding: utf-8 -*-
import json
import logging
import random
import requests
from requests.exceptions import ConnectionError
from scrapy.exceptions import IgnoreRequest

class CookiesMiddlewares(object):
    def __init__(self, ckookies_pool_url):
        self.logger = logging.getLogger(__name__)
        self.ckookies_pool_url = ckookies_pool_url

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            ckookies_pool_url=crawler.settings.get('COOKIES_POOL_URL')
        )

    def process_request(self, request, spider):
        cookies = random.choice(self.ckookies_pool_url)
        if cookies:
            request.cookies = cookies
            self.logger.debug('正在使用：' + json.dumps(cookies))
        else:
            self.logger.debug('cookies未能调用')

    def process_response(self, request, response, spider):
        # 判断cookies失效，封号等情况
        if response.status in [300, 301, 302, 303]:
            try:
                redirect_url = response.headers['location']
                if 'passport' in redirect_url:
                    self.logger.warning('cookies失效，正在更换cookies...')
                elif 'security' in redirect_url:
                    self.logger.warning('帐号失效，正在更换帐号...')
                # 替换cookies
                request.cookies = random.choice()
                return request
            except:
                raise IgnoreRequest
        elif response.status in [414]:
            return request
        else:
            return response
