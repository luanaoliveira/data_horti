# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DataHortiItem(scrapy.Item):
    product = scrapy.Field()
    market = scrapy.Field()
    update = scrapy.Field()
    value = scrapy.Field()

