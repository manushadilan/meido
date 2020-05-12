# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MeidoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    subject=scrapy.Field()
    link= scrapy.Field()
    startedBy= scrapy.Field()
    replies= scrapy.Field()
    views=scrapy.Field()
    lastPostDate= scrapy.Field()
    lastPostBy=scrapy.Field()
