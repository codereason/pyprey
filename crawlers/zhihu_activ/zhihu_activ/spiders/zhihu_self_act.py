import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import json
from items import ZhihuItem

class ZhihuSelfActSpider(CrawlSpider):
    ''' zhihu my own page activity'''
    name = 'zhihu_self_act'
    allowed_domains = ['zhihu.com']
    start_urls = ['http://zhihu.com/people/lian-shang-tian-kong-lan']

    rules = (
        Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    )
    def googlebot_header(self):

        headers = {"User-agent":"Googlebot"}
        return headers

    def start_requests(self):
        yield scrapy.http.Request(url, headers=googlebot_header())

    def parse_item(self, response):
        item = {}
        from bs4 import BeautifulSoup as bfs
        soup = bfs(response.text,"lxml")
        j = soup.findAll('script',{"type":"text/json"})[1].string
        jj = json.loads(j)
        for in 
            item = ZhihuItem()

            yield item
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        return item

