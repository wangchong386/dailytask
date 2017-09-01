# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ItemList(scrapy.Item):
    item_code = scrapy.Field()
    item_name = scrapy.Field()
    item_cate = scrapy.Field()
    url = scrapy.Field()
    current_page = scrapy.Field()
    rate_star = scrapy.Field()
    order_num = scrapy.Field()
    price = scrapy.Field()
    ori_price = scrapy.Field()
    store_url = scrapy.Field()
    store_feed_url = scrapy.Field()
    crawl_time = scrapy.Field()


class ItemFeedback(scrapy.Item):
    item_code = scrapy.Field()
    current_page = scrapy.Field()
    total_page = scrapy.Field()
    records = scrapy.Field()


class ItemStore(scrapy.Item):
    store_num = scrapy.Field()
    store_name = scrapy.Field()
    store_url = scrapy.Field()
    store_time = scrapy.Field()
    crawl_time = scrapy.Field()
