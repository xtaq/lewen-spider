# coding=utf-8

import scrapy
import time
import urlparse
from scrapy.http import Request
from scrapy.selector import Selector
from lewen.items import LewenItem

__author__ = 'xt'


class S6krSpider(scrapy.Spider):
    name = '36kr'
    allowed_domains = ['36kr.com']
    start_urls = ['http://36kr.com/']

    def parse(self, response):
        sel = Selector(response)
        article_list = sel.xpath('//div[@class="head-images J_headImages"]//a '
                                 '| //div[@class="article-list"]//article//a[@target="_blank"]')
        for article in article_list:
            url = article.xpath('./@href').extract()[0]
            url = urlparse.urljoin(response.url, url)
            yield Request(url=url, callback=self.parse_detail)

    def parse_detail(self, response):
        sel = Selector(response)
        item = LewenItem()
        item['source'] = '36kr'
        item['article_url'] = response.url
        item['update_time'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        item['create_time'] = sel.xpath('//time[@class="timeago"]/attribute::title').extract()[0]
        item['author'] = sel.xpath('//span[@class="name"]/text()').extract()[0]
        item['title'] = sel.xpath('//h1[@class="single-post__title"]/text()').extract()[0]
        item['content'] = sel.xpath('//section[@class="article"]').extract()[0]
        return item

