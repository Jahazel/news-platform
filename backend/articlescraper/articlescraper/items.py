import scrapy

class CnnTechArticle(scrapy.Item):
    # The title of the article
    title = scrapy.Field()
    
    # The author of the article
    author = scrapy.Field()
    
    # A brief summary of the article
    summary = scrapy.Field()
    
    # The URL to the full article
    url = scrapy.Field()
