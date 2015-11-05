# -*- coding: utf-8 -*-
from lewen.spiders.conf_spider import conf

# scrapy api
from twisted.internet import reactor, defer
from scrapy.crawler import CrawlerRunner
from scrapy.utils.project import get_project_settings
import logging

logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename='myapp.log',
                filemode='w')
logger = logging.getLogger(__name__)
runner = CrawlerRunner(get_project_settings())


@defer.inlineCallbacks
def crawl():
    spider_counter = 0
    for name, rule in conf.items():
        logger.info("Spider %s started" % name)
        spider_counter += 1
        yield runner.crawl('deep', rule)
        if spider_counter == len(conf):
            reactor.stop()

crawl()
# blocks process so always keep as the last statement
reactor.run()
