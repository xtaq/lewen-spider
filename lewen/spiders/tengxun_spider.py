# coding=utf-8


import scrapy
import time
from scrapy.http import Request
from scrapy.selector import Selector
from lewen.items import LewenItem

__author__ = 'xt'


class TengxunSpider(scrapy.Spider):
    name = 'tengxun'
    allowed_domains = ['news.qq.com']
    start_urls = ['http://news.qq.com/']

    def parse(self, response):
        sel = Selector(response)
        article_list = sel.xpath('//div[@class="Q-tpList"]//a')
        for article in article_list:
            url = article.xpath('./@href').extract()[0]
            yield Request(url=url, callback=self.parse_detail)

    def parse_detail(self, response):
        sel = Selector(response)
        item = LewenItem()
        item['source'] = 'tengxun'
        item['article_url'] = response.url
        item['update_time'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        item['create_time'] = sel.xpath('//span[@class="article-time"]/text()').extract()[0]
        item['author'] = sel.xpath('//span[@bosszone="jgname"]/a/text()').extract()[0]
        item['title'] = sel.xpath('//div[@class="hd"]/h1/text()').extract()[0]
        item['content'] = sel.xpath('//div[@accesskey="3"]').extract()[0]
        return item

