import os

BOT_NAME = 'weibospider'

SPIDER_MODULES = ['weibospider.spiders']
NEWSPIDER_MODULE = 'weibospider.spiders'

ROBOTSTXT_OBEY = False
DOWNLOAD_DELAY = 2
DOWNLOAD_TIMEOUT = 10
COOKIES_ENABLED = True
# COOKIES_POOL_URL = 'http://127.0.0.1:5000/weibo/random'
COOKIES_POOL_URL = []

# TELNETCONSOLE_ENABLED = False

DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
    'Connection': 'keep-alive',
    'Host': 'weibo.cn',
    'Referer': 'https://weibo.cn/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
}
# SPIDER_MIDDLEWARES = {
#    'weibospider.middlewares.WeibospiderSpiderMiddleware': 543,
# }

DOWNLOADER_MIDDLEWARES = {
    'weibospider.middlewares.CookiesMiddlewares': 543,
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'scrapy_fake_useragent.middleware.RandomUserAgentMiddleware': 400,
}
ITEM_PIPELINES = {
    # 'scrapy.pipelines.images.ImagesPipeline': 1,
    #  'weibospider.pipelines.MyImagesPipeline': 200,
    'weibospider.pipelines.MysqlTwistedPipeline': 300,
}

# IMAGES_STORE = os.path.dirname(os.path.abspath(__file__))
# IMAGES_STORE = 'C:\\PythonProjects\\weibospider\\pics'

MYSQL_HOST = 'localhost'
MYSQL_DBNAME = 'weibo'
MYSQL_USER = 'root'
MYSQL_PASSWORD = '1234566'

SQL_DATETIME_FORMAT = '%Y-%m-%d %H:%M:%S'
SQL_DATE_FORMAT = '%Y-%m-%d'

'''scrapy-redis配置'''
# # 启用Redis调度存储请求队列
SCHEDULER = "scrapy_redis.scheduler.Scheduler"

# # 确保所有的爬虫通过Redis去重
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
#
# # 不清除Redis队列、这样可以暂停/恢复 爬取
SCHEDULER_PERSIST = True

# # 指定连接到redis时使用的端口和地址（可选）
REDIS_HOST = 'localhost'
REDIS_PORT = 6379

