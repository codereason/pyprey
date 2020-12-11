# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhihuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    id = scrapy.Field()
    url = scrapy.Field()
    name = scrapy.Field()
    action = scrapy.Field()
    writer = scrapy.Field()
    title = scrapy.Field()
    question = scrapy.Field()
    content = scrapy.Field()
    flag = scrapy.Field()
    time = scrapy.Field()
    source_flag = scrapy.Field()
    pass


class CsdnBlogItem(scrapy.Item):
    pass

class JianshuBlogItem(scrapy.Item):
    pass

class JianshuBlogItem(scrapy.Item):
    pass