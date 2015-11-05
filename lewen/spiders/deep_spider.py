# coding=utf-8

import scrapy
import urlparse
import time
import logging
from scrapy.http import Request
from scrapy.selector import Selector
from lewen.items import LewenItem
from scrapy.spiders import CrawlSpider, Rule

__author__ = 'xt'


class DeepSpider(CrawlSpider):
    name = 'deep'

    def __init__(self, rule):
        self.rule = rule
        self.name = rule['name']
        self.allowed_domains = rule['allow_domains']
        self.start_urls = rule['start_urls']
        self.log = logging.getLogger(__name__)
        super(DeepSpider, self).__init__()

    def parse(self, response):
        sel = Selector(response)
        article_list = sel.xpath(self.rule['article'])
        for article in article_list:
            url = article.xpath('./@href').extract()[0]
            url = urlparse.urljoin(response.url, url)
            yield Request(url=url, callback=self.parse_detail, errback=self.on_err)

    def parse_detail(self, response):
        sel = Selector(response)
        item = LewenItem()
        item['source'] = self.name
        item['article_url'] = response.url
        item['update_time'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        create_time = sel.xpath(self.rule['create_time']['xpath']).extract()
        item['create_time'] = self._is_index('create_time', create_time)

        author = sel.xpath(self.rule['author']['xpath']).extract()
        item['author'] = self._is_index('author', author)

        title = sel.xpath(self.rule['title']['xpath']).extract()
        item['title'] = self._is_index('title', title)

        content = sel.xpath(self.rule['content']['xpath']).extract()
        item['content'] = self._is_index('content', content)
        if 'join' in self.rule['content']:
            item['content'] = ''.join(content)

        return item

    def _is_index(self, arg, content):
        if content:
            if 'index' in self.rule[arg]:
                return content[0].strip()
            else:
                return content
        else:
            self.log.error('spider %s %s fetch is none' % (self.name, arg))

    def on_err(self, reason):
        try:
            response = reason.value.response
            url = response.url
            msg = str.format('ON PROCESSING {1}, CODE: {0}', response.status, url)
            self.log.error(msg)
        except (TypeError, AttributeError):
            self.log.error(str.format('Error: {0}', reason))
