# coding=utf-8

__author__ = 'xt'

import scrapy
import time
from scrapy.http import Request
from scrapy.selector import Selector
from lewen.items import LewenItem

class SinaSpider(scrapy.Spider):
    name = 'sina'
    allowed_domains = ['news.sina.com.cn']
    start_urls = ['http://news.sina.com.cn/']

    def parse(self, response):
        sel = Selector(response)
        article_list = sel.xpath('//div[@class="blk_04"]//a')
        for article in article_list:
            url = article.xpath('./@href').extract()[0]
            yield Request(url=url, callback=self.parse_detail)

    def parse_detail(self, response):
        sel = Selector(response)
        item = LewenItem()
        item['source'] = 'sina'
        item['article_url'] = response.url
        item['update_time'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 
        item['create_time'] = sel.xpath('//span[@class="time-source"]/text()').extract()[0]
        item['author'] = sel.xpath('//span[@data-sudaclick="media_name"]/a/text()').extract()[0]
        item['title'] = sel.xpath('//h1[@id="artibodyTitle"]/text()').extract()[0]
        contents = sel.xpath('//div[@id="artibody"]//p').extract()
        item['content'] = ''
        for content in contents:
            item['content'] += content
        return item

