import scrapy


class ZhihuActivSelfSpider(scrapy.Spider):
    name = 'zhihu_activ_self'
    allowed_domains = ['zhihu.com']
    start_urls = ['http://zhihu.com/']

    def parse(self, response):

        pass
