#coding=utf-8
from __future__ import absolute_import
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import json

from zhihu_activ.items import ZhihuItem
import logging


class ZhihuSelfActSpider(CrawlSpider):
    ''' zhihu my own page activity'''
    name = 'zhihu_self_act'
    allowed_domains = ['zhihu.com']
    start_urls = ['http://zhihu.com/people/lian-shang-tian-kong-lan']

    rules = (
        Rule(LinkExtractor(allow=r'Items/'),
             callback='parse_item', follow=True),
    )

    def googlebot_header(self):
        headers = {"User-agent": "Googlebot"}
        return headers

    def start_requests(self):
        print("starting req")



        yield scrapy.http.Request("https://www.zhihu.com/people/lian-shang-tian-kong-lan/", headers=self.googlebot_header(),
                                  callback=self.parse_first_page_item)

    def parse_first_page_item(self, response):
        # print(response.status_code)
        ''' main page crawling'''
        print("2")
        from bs4 import BeautifulSoup as bfs
        print(response.text)
        soup = bfs(response.text, "lxml")
        j = soup.findAll('script', {"type": "text/json"})[1].string
        jj = json.loads(j)
        entities = jj['initialState']['entities']
        answers = entities['answers']
        articles = entities['articles']

        def get_articles_fields(articles):
            res = []

            for key in list(articles.keys()):
                tmp = {}
                tmp['article'] = key
                tmp['updated'] = articles[key].get('updated')
                tmp['author_name'] = articles[key].get('author')['name']
                tmp['title'] = articles[key].get('title')
                tmp["created"] = articles[key].get('created')
                res.append(tmp)
            return res

        def get_id_and_action(act):
            res = []
            for key in act:
                article_id = str(act[key].get("target")["id"])
                action = act[key]['actionText']
                createdTime = act[key]['createdTime']
                res.append({"article_id": article_id,
                            "action": action, "createdTime": createdTime})
            return res

        details = get_articles_fields(articles)
        res = get_id_and_action(entities["activities"])
        joined = []
        for i in range(len(details)):
            for j in range(len(res)):
                # print(details[i].get("article"),res[j].get("article_id"))
                if details[i].get("article") == res[j].get("article_id"):
                    # print(i,j)
                    tmp = {
                        "article_id": details[i].get("article"),
                        "action": res[j].get("action"),
                        "createdTime": res[j].get("createdTime"),
                        "updatedTime": details[i].get("updated"),
                        "author_name": details[i].get("author_name"),
                        "title": details[i].get("title"),

                    }
                    joined.append(tmp)
        joined = sorted(joined, key=lambda x: x.get(
            'createdTime'), reverse=True)
        for i in range(len(joined)):
            item = ZhihuItem()
            #             id = scrapy.Field()
            # url = scrapy.Field()
            # name = scrapy.Field()
            # action = scrapy.Field()
            # writer = scrapy.Field()
            # title = scrapy.Field()
            # question = scrapy.Field()
            # content = scrapy.Field()
            # flag = scrapy.Field()
            # time = scrapy.Field()

            #     [{'article_id': '334325756',
            #   'action': '赞同了文章',
            #   'createdTime': 1607394299,
            #   'updatedTime': 1607391682,
            #   'author_name': 'Zilliz',
            #   'title': 'Milvus 实战 | 基于 Milvus 的图像查重系统'},
            item['id'] = joined[i].get('article_id')
            item['action'] = joined[i].get('action')
            item['time'] = joined[i].get('createdTime')
            item['content'] = joined[i].get('title')
            item['writer'] = joined[i].get('author_name')
            # item[''] = joined[i].get()
            print(item)

            yield item

        self.json_url = []


        def parse_jsons_item(self, response):
            '''parse jsons after parsing first page json'''
            self.json_url = url.get('paging') or None

            yield item

            if self.json_url:
                yield scrapy.http.Request(self.json_url, headers=self.googlebot_header(),
                                  callback=self.parse_jsons_item)