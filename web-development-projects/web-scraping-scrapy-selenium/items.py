# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class VergeReview(scrapy.Item):
    authorlink = scrapy.Field()
    authorname = scrapy.Field()
    title = scrapy.Field()
    url = scrapy.Field()