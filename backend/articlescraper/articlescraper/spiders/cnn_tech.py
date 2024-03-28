import scrapy

class CnnTechSpider(scrapy.Spider):
    name = 'cnn_tech'  # Spider name used in the 'scrapy crawl' command
    allowed_domains = ['cnn.com']  # Limits the crawl to the CNN domain
    start_urls = ['https://www.cnn.com/business/tech']  # Starting point for the crawl

    # Sets to track seen URLs and headlines for deduplication
    seen_urls = set()
    seen_headlines = set()

    def parse(self, response):
        # Loop through each article found on the page
        for article in response.css('div[data-uri]'):
            # Construct the full URL from the relative path found in the href attribute
            article_url = response.urljoin(article.css('a::attr(href)').get())
            # Extract the article's headline
            headline = article.css('.container__headline-text::text').get()

            # Skip articles without headlines and ensure uniqueness
            if headline and article_url not in self.seen_urls and headline not in self.seen_headlines:
                self.seen_urls.add(article_url)
                self.seen_headlines.add(headline)

                yield {
                    'headline': headline,
                    'article_url': article_url,
                }
