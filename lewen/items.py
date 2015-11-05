# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class LewenItem(Item):
    title = Field()
    content = Field()
    source = Field()
    image_urls = Field()
    create_time = Field()
    author = Field()
    article_url = Field()
    update_time = Field()
