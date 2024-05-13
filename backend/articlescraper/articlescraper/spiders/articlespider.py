import scrapy

class ArticlespiderSpider(scrapy.Spider):
    name = "articlespider"
    allowed_domains = ["techcrunch.com"]
    start_urls = ["https://techcrunch.com/"]

    def parse(self, response):
        latest_container = response.css(".wp-block-group.is-layout-flow.wp-block-group-is-layout-flow")
        articles = latest_container.css(".wp-block-tc23-post-picker")
        
        for article in articles:
            url =  article.css("h2 a").attrib['href']
            yield response.follow(url, self.parse_article, meta={'article_url': url})

    def parse_article(self, response):
        container = response.css(".wp-block-group")
        
        yield{
            "title": container.css("h1::text").get(),
            "url": response.meta['article_url'],
            "author": container.css(".wp-block-tc23-author-card-name a::text").get(),
            "publishedDate": container.xpath(".//div[contains(@class, 'wp-block-post-date')]/time/@datetime").get()
        }