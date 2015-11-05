# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import logging
import config
from scrapy.exceptions import DropItem


class LewenPipeline(object):

    def __init__(self):
        self.db = config.db
        self.log = logging.getLogger(__name__)

    def open_spider(self, spider):
        sql = 'delete from article_info where source = %d' % (config.source_id[spider.name])
        self.db.delete_article(sql, spider.name)

    def process_item(self, item, spider):
        item['source'] = config.source_id[item['source']]

        if item['title']:
            self.db.insert_article(item, spider.name)
        else:
            self.log.error("Spider %s title is None, url: %s" % (spider.name, item['article_url']))

        return item
