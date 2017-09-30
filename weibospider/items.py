import datetime
import scrapy
from weibospider.settings import SQL_DATETIME_FORMAT

class InformationItem(scrapy.Item):
    id_name = scrapy.Field()
    identitys = scrapy.Field()
    sex = scrapy.Field()
    living_place = scrapy.Field()
    intro = scrapy.Field()
    fans_num = scrapy.Field()
    birth_date = scrapy.Field()
    ID = scrapy.Field()
    image_urls = scrapy.Field()
    images = scrapy.Field()

    def get_insert_sql(self):
        insert_sql = '''
            insert into weibo_influentials(ID,id_name,sex,identitys,fans_num,intro,living_place,birth_date,
            image_urls,crawl_time
              )
            VALUE (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            ON DUPLICATE KEY UPDATE fans_num=VALUES(fans_num),
            intro=VALUES(intro),image_urls=VALUES(image_urls)
        '''
        ID = self['ID']
        id_name = self['id_name']
        sex = self['sex']
        identitys = self['identitys']
        fans_num = self['fans_num']
        intro = self['intro']
        living_place = self['living_place']
        birth_date = self['birth_date']
        image_urls = str(self['image_urls'])
        crawl_time = datetime.datetime.now().strftime(SQL_DATETIME_FORMAT)

        params = (ID,id_name,sex,identitys,fans_num,intro,living_place,birth_date,
            image_urls,crawl_time)

        return insert_sql, params


