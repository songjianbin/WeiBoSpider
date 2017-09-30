# -*- coding: utf-8 -*-
import re
from urllib import parse
import scrapy
import time
import json
import random
from weibospider.items import InformationItem
from scrapy_redis.spiders import RedisSpider

class WeiboSpider(RedisSpider):
    name = "weibo"
    redis_key = "weibo:start_urls"
    # start_urls = ['https://weibo.cn/2716896955/follow']

    def parse(self, response):
        # 爬取用户关注列表中粉丝数大于100万的账户ID
        results = response.css('table')
        for result in results:
            fans_num = int(result.re('.*?<br>粉丝(.*?)人.*')[0])
            ID = result.xpath('.//tr/td[2]/a[2]').re('.*?uid=(.*?)&.*')[0]
            if fans_num >= 1000000:
                yield scrapy.Request(url='https://weibo.cn/' + ID + '/info', callback=self.parse_info,
                                     meta={'fans_num': fans_num})
        next_page = response.css('#pagelist a::attr(href)').extract_first()
        if next_page:
            time.sleep(random.uniform(0.1, 1.1))
            yield scrapy.Request(url=parse.urljoin(response.url, next_page), callback=self.parse)

    def parse_info(self, response):
        # 爬取个人简单信息
        infoitem = InformationItem()
        ID = re.search('https://weibo.cn/(.*?)/info', response.url).group(1)
        infoitem['ID'] = ID
        infoitem['image_urls'] = response.css('.c img::attr(src)').extract_first()
        infoitem['id_name'] = re.search(".*?<title>(.*?)的资料.*", response.text).group(1)
        if '认证信息' in response.text:
            infoitem['identitys'] = re.search(".*?认证信息：(.*?)<br/>.*", response.text).group(1)
        else:
            infoitem['identitys'] = '未填写'
        if '性别' in response.text:
            infoitem['sex'] = re.search(".*?性别:(.*?)<br/>.*", response.text).group(1)
        else:
            infoitem['sex'] = '未填写'
        if '地区' in response.text:
            infoitem['living_place'] = re.search(".*?地区:(.*?)<br/>.*", response.text).group(1)
        else:
            infoitem['living_place'] = '未填写'
        if '生日' in response.text:
            infoitem['birth_date'] = re.search(".*?生日:(.*?)<br/>.*", response.text).group(1)
        else:
            infoitem['birth_date'] = '未填写'
        if '简介' in response.text:
            intro_json = json.dumps(re.search(".*?简介:(.*)<br/>.*", response.text).group(1)).replace('\\ud', '')
            infoitem['intro'] = intro_json.encode('latin-1').decode('unicode_escape')
        else:
            infoitem['intro'] = '未填写'
        try:
            infoitem['fans_num'] = response.meta['fans_num']
        except:
            infoitem['fans_num'] = 0
        yield infoitem
        yield scrapy.Request(url='https://weibo.cn/' + ID + '/follow', callback=self.parse)

