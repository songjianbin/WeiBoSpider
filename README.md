 WeiBoSpider/微博爬虫
 =============

> - 爬取新浪微博粉丝量大于100万的影响力账号
> - 使用redis队列管理和去重功能
> - mysql存储抓取信息
<br><br/>

### 运行环境

Win10<br>
Python3.6<br>
Scrapy 1.3.3<br>
redis (2.10.6)<br>
MySQL Server 5.7<br>
<br/>

## 安装
```python
pip install -r requirements.txt
```

## settings配置
- cookies设置（示例），建议50个以上
```python
COOKIES_POOL_URL = [{'M_WEIBOCN_PARAMS': 'uicode%3D20000174',
                'SUB': '_2A2506lRDeThGedG71IY9yvKyT6IHXVUQzcZrDV6PUJbkdBeLVXNkW2SDpIJOt5lAV72ldoRlrJ9phFg..',
                'SCF': 'Am4ftLOpzroObu-7obBroD-s0vLEOFmI9zS_1UpLrZGvzQefwBRqXdXx9GDp5G5iqV9RCQa-pReFi-xU.',
                'SUHB': '0bttx7lOFWKRI', 'SSOLoginState': '1250542009', '_T_WM': 'd3db121574b0b47ed4fdc91ddc0bc7'}]
```

- scrapy-redis设置
```python
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
SCHEDULER_PERSIST = True
```

- mysql设置
```python
MYSQL_HOST = 'localhost'
MYSQL_DBNAME = 'weibo'
MYSQL_USER = 'root'
MYSQL_PASSWORD = '1234566'
```

- 如果cookies数量较多，可以增加设置`CONCURRENT_REQUESTS_PER_DOMAIN`(默认为8)，并取消`DOWNLOAD_DELAY`
```python
CONCURRENT_REQUESTS_PER_DOMAIN = 16
#DOWNLOAD_DELAY = 2
```

## 运行
- 请选择适当数量的起始url，存入redis队列中
```python
redis-cli push xinhua:start_urls https://weibo.cn/xxxxxxx/follow
```
- 启动spider
```python
scrapy crawl weibo
```


### 运行效果
```
2017-09-15 22:05:15 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://weibo.cn/1705586121/info> (referer: https://weibo.cn/5683580776/follow)
2017-09-15 22:05:15 [scrapy.core.scraper] DEBUG: Scraped from <200 https://weibo.cn/1705586121/info>
{'ID': '1705586121',
 'birth_date': '1991-08-16',
 'fans_num': 23516858,
 'id_name': 'GEM鄧紫棋',
 'identitys': '香港歌手',
 'image_urls': 'http://tvax1.sinaimg.cn/crop.0.0.512.512.180/65a92dc9ly8ffymnv401sj20e80e83ze.jpg',
 'intro': '"羅馬書12:19「不要自己伸冤，寧可讓步，聽憑主怒。」<br/>标签:<a '
          'href="/search/?keyword=%E8%87%AA%E7%94%B1&amp;stag=1">自由</a>&nbsp;<a '
          'href="/search/?keyword=90%E5%90%8E&amp;stag=1">90后</a>&nbsp;<a '
          'href="/search/?keyword=%E9%9F%B3%E6%A8%82%E4%BA%BA&amp;stag=1">音樂人</a>&nbsp;<a '
          'href="/account/privacy/tags/?uid=1705586121&amp;st=817ed6">更多&gt;&gt;</a><br/></div><div '
          'class="tip">其他信息</div><div '
          'class="c">互联网:http://weibo.com/gemtang<br/>手机版:http://weibo.cn/gemtang"',
 'living_place': '香港 其他',
 'sex': '女'}
2017-09-15 22:05:15 [scrapy_redis.dupefilter] DEBUG: Filtered duplicate request <GET https://weibo.cn/1705586121/follow> - no more duplicates will be shown (see DUPEFILTER_DEBUG to show all duplicates)
2017-09-15 22:05:17 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://weibo.cn/1192329374/info> (referer: https://weibo.cn/5683580776/follow)
2017-09-15 22:05:17 [scrapy.core.scraper] DEBUG: Scraped from <200 https://weibo.cn/1192329374/info>
{'ID': '1192329374',
 'birth_date': '0001-00-00',
 'fans_num': 94121417,
 'id_name': '谢娜',
 'identitys': '知名女主持人',
 'image_urls': 'http://tva3.sinaimg.cn/crop.0.1.1242.1242.180/4711809ejw8f387zus4vpj20yi0ykjwd.jpg',
 'intro': '"太阳女神（也可称为喜神）的光芒照四方呀嘛照四方：）工作邮箱：w761324@qq.com（仅限工作）感谢！<br/>标签:<a '
          'href="/search/?keyword=%E7%A4%BE%E4%BC%9A%E9%97%B2%E6%9D%82%E4%BA%BA%E7%AD%89&amp;stag=1">社会闲杂人等</a>&nbsp;<a '
          'href="/search/?keyword=%E4%B8%BB%E6%8C%81%E4%BA%BA&amp;stag=1">主持人</a>&nbsp;<a '
          'href="/account/privacy/tags/?uid=1192329374&amp;st=817ed6">更多&gt;&gt;</a><br/></div><div '
          'class="tip">其他信息</div><div '
          'class="c">互联网:http://weibo.com/xiena<br/>手机版:http://weibo.cn/xiena"',
 'living_place': '北京 海淀区',
 'sex': '女'}
2017-09-15 22:05:20 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://weibo.cn/1749975705/info> (referer: https://weibo.cn/5683580776/follow)
2017-09-15 22:05:21 [scrapy.core.scraper] DEBUG: Scraped from <200 https://weibo.cn/1749975705/info>
{'ID': '1749975705',
 'birth_date': '未填写',
 'fans_num': 7178570,
 'id_name': '唯美式情感语录',
 'identitys': '微博知名情感帐号',
 'image_urls': 'http://tva4.sinaimg.cn/crop.0.0.180.180.180/684e8299jw1e8qgp5bmzyj2050050aa8.jpg',
 'intro': '"全球搜索唯美情感美句，让我们一起感受身临其中的唯美境界，每小时整点发一条微博，关注吧，每个时刻的精彩微博让你深有体会。合作QQ：2559277275<br/>标签:<a '
          'href="/search/?keyword=%E8%AF%97%E8%AF%8D&amp;stag=1">诗词</a>&nbsp;<a '
          'href="/search/?keyword=%E6%84%9F%E6%82%9F%E4%BA%BA%E7%94%9F&amp;stag=1">感悟人生</a>&nbsp;<a '
          'href="/search/?keyword=%E7%BB%8F%E5%85%B8%E8%AF%AD%E5%BD%95%E6%94%B6%E9%9B%86&amp;stag=1">经典语录收集</a>&nbsp;<a '
          'href="/account/privacy/tags/?uid=1749975705&amp;st=817ed6">更多&gt;&gt;</a><br/></div><div '
          'class="tip">其他信息</div><div '
          'class="c">互联网:http://weibo.com/u/1749975705<br/>手机版:http://weibo.cn/u/1749975705"',
 'living_place': '广东 广州',
 'sex': '女'}
```

### 数据展示
  ![](http://upload-images.jianshu.io/upload_images/6926359-ee037822b75664cf.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

### 注意事项
- 程序已设置适当延迟，请合理使用
