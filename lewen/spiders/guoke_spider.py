# coding=utf-8

__author__ = 'xt'

import scrapy
import time
from scrapy.http import Request
from scrapy.selector import Selector
from lewen.items import LewenItem

class GuokeSpider(scrapy.Spider):
    name = 'guoke'
    allowed_domains = ['guokr.com']
    start_urls = ['http://www.guokr.com/']

    def parse(self, response):
        sel = Selector(response)
        article_list = sel.xpath('//div[@class="focus-explain"]//a')
        for article in article_list:
            url = article.xpath('./@href').extract()[0]
            yield Request(url=url, callback=self.parse_detail)

    def parse_detail(self, response):
        sel = Selector(response)
        item = LewenItem()
        item['source'] = 'guoke'
        item['article_url'] = response.url
        item['update_time'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        create_time = sel.xpath('//div[@class="content-th-info"]/span/text()').extract()[0]
        item['create_time'] = create_time
        item['author'] = sel.xpath('//div[@class="content-th-info"]/a/text()').extract()[0]
        item['title'] = sel.xpath('//h1[@id="articleTitle"]/text()').extract()[0]
        item['content'] = sel.xpath('//div[@class="document"]/div').extract()[0]
        return item

