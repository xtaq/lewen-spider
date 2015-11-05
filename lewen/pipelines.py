# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import logging
import MySQLdb
import config
from scrapy.exceptions import DropItem
from scrapy.http import Request


class LewenPipeline(object):

    def __init__(self):
        self.conn = MySQLdb.connect(host='localhost',
                                    port=3306,
                                    user="root",
                                    passwd="",
                                    db="test",
                                    charset="utf8")
        self.cursor = self.conn.cursor()
        self.log = logging.getLogger(__name__)

    def open_spider(self, spider):
        try:
            sql = 'delete from article_info where source = %d' % (config.source_id[spider.name])
            self.cursor.execute(sql)
            self.conn.commit()
        except MySQLdb.Error, e:
            self.log.error("Spider %s Delete Error %d: %s" % (spider.name, e.args[0], e.args[1]))
            self.conn.rollback()

    def process_item(self, item, spider):
        item['source'] = config.source_id[item['source']]

        try:
            if item['title']:
                self.cursor.execute("""INSERT INTO article_info (source, title, article_url,
                                create_time, update_time, content, author)
                                VALUES (%s, %s, %s, %s, %s, %s, %s)""",
                                (item['source'],
                                 item['title'],
                                 item['article_url'],
                                 item['create_time'],
                                 item['update_time'],
                                 item['content'],
                                 item['author']))
            else:
                self.log.error("Spider %s title is None, url: %s" % (spider.name, item['article_url']))

            self.conn.commit()
        except MySQLdb.Error, e:
            self.log.error("Spider %s Insert Error %d: %s" % (spider.name, e.args[0], e.args[1]))

        return item
