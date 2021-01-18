# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class GaobanjiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    month_5_7_last = scrapy.Field()
    month_6_8_last = scrapy.Field()
