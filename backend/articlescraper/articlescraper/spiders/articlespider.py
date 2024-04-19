import scrapy


class ArticlespiderSpider(scrapy.Spider):
    name = "articlespider"
    allowed_domains = ["techcrunch.com"]
    start_urls = ["https://techcrunch.com/"]

    def parse(self, response):
        content = response.css(".content .river.river--homepage div")
        articles = content.css(".post-block.post-block--image.post-block--unread")

        for article in articles:
            yield{
                "name":article.css(".post-block__header .post-block__title a::text").get(),
                "author": article.css(".river-byline__authors a::text").get()
            }
