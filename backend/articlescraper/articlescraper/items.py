import scrapy

class CnnTechArticle(scrapy.Item):
    title = scrapy.Field()
    author = scrapy.Field()
    summary = scrapy.Field()
    url = scrapy.Field()
