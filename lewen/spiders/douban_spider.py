__author__ = 'xt'

import scrapy
import time
from scrapy.http import Request
from scrapy.selector import Selector
from lewen.items import LewenItem

class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['douban.com']
    start_urls = ['http://www.douban.com/']

    def parse(self, response):

        sel = Selector(response)
        article_list = sel.xpath('//div[@class="notes"]//li//a')
        for article in article_list:
            url = article.xpath('./@href').extract()[0]
            yield Request(url=url, callback=self.parse_detail)

    def parse_detail(self, response):
        sel = Selector(response)
        item = LewenItem()
        item['source'] = 'douban'
        item['article_url'] = response.url
        item['update_time'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        item['create_time'] = sel.xpath("//div[@id='content']//div/span[@class='pl']/text()").extract()[0]
        item['author'] = sel.xpath('//div/a[@class="note-author"]/text()').extract()[0]
        title = sel.xpath('//div[contains(@class, "note-header")]/h1/text()').extract()[0]
        item['title'] = title
        item['content'] = sel.xpath("//div[@id='link-report']").extract()
        return item
