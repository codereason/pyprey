from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from config.config import Config
from items import ZhihuItem
import json

class ZhihuFollowedUsersSpider(CrawlSpider):
    name = 'zhihu_followed_users'
    allowed_domains = ['zhihu.com']
    start_urls = ['http://zhihu.com/']
    cf = Config("../../../../config/config.ini")
    confs = cf.get_configs()
    followed_users = confs.get('crawler')['followed_users']
    # headers = confs.get('crawler')['headers']
    users = followed_users.split(",") if "," in followed_users else [followed_users]
    rules = (
        Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    )

    def googlebot_header(self,url):
        headers.get("google_header")
        headers = {"User-agent":"Googlebot"}
        return headers

    def start_requests(self):
        for user in followed_users:
            url = "https://www.zhihu.com/people/{}".format(user)

            googlebot_header[''] = ''
            yield scrapy.http.JSONRequest(url, headers=googlebot_header)

    def parse_item(self, response):
        resp = json.loads(response)
        item = ZhihuItem()
        item['']
        item['']
        yield itme
        # item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        # item['name'] = response.xpath('//div[@id="name"]').get()
        # item['description'] = response.xpath('//div[@id="description"]').get()
        