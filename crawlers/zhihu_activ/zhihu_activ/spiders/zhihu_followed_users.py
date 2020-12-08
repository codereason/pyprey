from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from config.config import Config


class ZhihuFollowedUsersSpider(CrawlSpider):
    name = 'zhihu_followed_users'
    allowed_domains = ['zhihu.com']
    start_urls = ['http://zhihu.com/']
    cf = Config("../../../../config/config.ini")
    confs = cf.get_configs()
    followed_users = confs.get('crawler')['followed_users']
    users = followed_users.split(",") if "," in followed_users else [followed_users]
    rules = (
        Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = {}
        # item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        # item['name'] = response.xpath('//div[@id="name"]').get()
        # item['description'] = response.xpath('//div[@id="description"]').get()
