import scrapy
import logging
from articlescraper.items import ArticleItem

class NbcnewsSpiderSpider(scrapy.Spider):
    name = "nbcnews_spider"
    allowed_domains = ["www.nbcnews.com"]
    start_urls = ["https://www.nbcnews.com/"]
    
    def __init__(self):
        self.processed_urls = set()

    section_parsers = {
        'U.S News': 'parse_us_news',
        'Politics': 'parse_politics',
        'World': 'parse_world',
        'Local': 'parse_local',
        'Business': 'parse_business',
        'Sports': 'parse_sports',
        'Paris-2024-olympics': 'parse_paris_2024_olympics',
        'Investigations': 'parse_investigations',
        'Culture & trends': 'parse_culture_and_trends',
        'Health': 'parse_health',
        'Science': 'parse_science',
        'Tech & Media': 'parse_tech_and_media',
        'Weather': 'parse_weather',
        # 'video-features': 'parse_video_features',
        'Photos': 'parse_photos',
        'NBC Select': 'parse_nbc_select',
        'NBC Asian America': 'parse_nbc_asian_america',
        'NBC-BLK': 'parse_nbc_blk',
        'NBC-Latino': 'parse_nbc_latino',
        'NBC-OUT': 'parse_nbc_out',
    }

    def parse(self, response):
        logging.debug("Parsing main page")
        section_container = response.css(".menu-section.menu-section-sections.menu-section-main")
        section_list = section_container.css(".menu-list .menu-list-item")
        logging.debug("Parsing main page")

        for url in section_list:
            section_url = url.css("a").attrib["href"]
            section_name = url.css("span::text").get()
            logging.debug(f"Found section: {section_name}, URL: {section_url}")

            if section_name in self.section_parsers:
                yield response.follow(section_url, self.parse_section, meta={'section_name': section_name})

    def parse_section(self, response):
        section_name = response.meta.get("section_name")
        logging.debug(f"Parsing section: {section_name}")
        
        if section_name and section_name != "parse_video_features":
            parse_method_name = self.section_parsers.get(section_name)  
            if parse_method_name and isinstance(parse_method_name, str):
                parse_method = getattr(self, parse_method_name, None)
                if parse_method:
                    yield from parse_method(response)
                else:
                    logging.warning(f"Method {parse_method_name} not found for section: {section_name}")
            else:
                logging.warning(f"No parse method defined for section: {section_name}")

    def parse_us_news(self, response):
        logging.debug("Parsing US news section")
        container = response.css(".package-grid")
        article_list = container.css(".styles_item__sANtw")
        
        for article in article_list:
            url = article.css("a::attr(href)").get()
            
            if url and url not in self.processed_urls:
                self.processed_urls.add(url)
                full_url = response.urljoin(url)
                logging.debug(f"Following article URL: {full_url}")

                yield response.follow(full_url, self.parse_article, meta={"url": full_url})

    # def parse_photos(self, response):
    #     logging.debug("Parsing photos news section")
    #     article_list = response.css(
    #     ".pkg.standardLead, .multi-up__article, .multi-up__tease-card--two-up, .multi-up__tease-card--three-up-main, .multi-up__tease-card--three-up, .multi-up__tease-card--four-up"
    # )

    def parse_politics(self, response):
        logging.debug("Parsing politics news section")
        article_list = response.css('.multi-up__article')
        
        for article in article_list:
            url = article.css("a::attr(href)").get()
            
            if url and url not in self.processed_urls:
                self.processed_urls.add(url)
                full_url = response.urljoin(url)
                logging.debug(f"Following article URL: {full_url}")

                yield response.follow(full_url, self.parse_article, meta={"url": full_url})

    def parse_world(self, response):
        logging.debug("Parsing world news section")
        article_list = response.css('.multi-up__article')
        
        for article in article_list:
            url = article.css("a::attr(href)").get()
            
            if url and url not in self.processed_urls:
                self.processed_urls.add(url)
                full_url = response.urljoin(url)
                logging.debug(f"Following article URL: {full_url}")

                yield response.follow(full_url, self.parse_article, meta={"url": full_url})

    def parse_local(self, response):
        logging.debug("Parsing local news section")
        article_list = response.css('.multi-up__article')
        
        for article in article_list:
            url = article.css("a::attr(href)").get()
            
            if url and url not in self.processed_urls:
                self.processed_urls.add(url)
                full_url = response.urljoin(url)
                logging.debug(f"Following article URL: {full_url}")

                yield response.follow(full_url, self.parse_article, meta={"url": full_url})     

    def parse_business(self, response):
        logging.debug("Parsing business news section")
        article_list = response.css('.multi-up__article')
        
        for article in article_list:
            url = article.css("a::attr(href)").get()
            
            if url and url not in self.processed_urls:
                self.processed_urls.add(url)
                full_url = response.urljoin(url)
                logging.debug(f"Following article URL: {full_url}")

                yield response.follow(full_url, self.parse_article, meta={"url": full_url})

    def parse_sports(self, response):
        logging.debug("Parsing sports news section")
        article_list = response.css('.multi-up__article')
        
        for article in article_list:
            url = article.css("a::attr(href)").get()
            
            if url and url not in self.processed_urls:
                self.processed_urls.add(url)
                full_url = response.urljoin(url)
                logging.debug(f"Following article URL: {full_url}")

                yield response.follow(full_url, self.parse_article, meta={"url": full_url})

    def parse_paris_2024_olympics(self, response):
        logging.debug("Parsing paris 2024 olympics news section")
        article_list = response.css('.multi-up__article')
        
        for article in article_list:
            url = article.css("a::attr(href)").get()
            
            if url and url not in self.processed_urls:
                self.processed_urls.add(url)
                full_url = response.urljoin(url)
                logging.debug(f"Following article URL: {full_url}")

                yield response.follow(full_url, self.parse_article, meta={"url": full_url})

    def parse_investigation(self, response):
        logging.debug("Parsing investigation news section")
        article_list = response.css('.multi-up__article')
        
        for article in article_list:
            url = article.css("a::attr(href)").get()
            
            if url and url not in self.processed_urls:
                self.processed_urls.add(url)
                full_url = response.urljoin(url)
                logging.debug(f"Following article URL: {full_url}")

                yield response.follow(full_url, self.parse_article, meta={"url": full_url})

    def parse_culture_and_trends(self, response):
        logging.debug("Parsing culture and trends news section")
        article_list = response.css('.multi-up__article')
        
        for article in article_list:
            url = article.css("a::attr(href)").get()
            
            if url and url not in self.processed_urls:
                self.processed_urls.add(url)
                full_url = response.urljoin(url)
                logging.debug(f"Following article URL: {full_url}")

                yield response.follow(full_url, self.parse_article, meta={"url": full_url})    

    def parse_health(self, response):
        logging.debug("Parsing health news section")
        article_list = response.css('.multi-up__article')
        
        for article in article_list:
            url = article.css("a::attr(href)").get()
            
            if url and url not in self.processed_urls:
                self.processed_urls.add(url)
                full_url = response.urljoin(url)
                logging.debug(f"Following article URL: {full_url}")

                yield response.follow(full_url, self.parse_article, meta={"url": full_url})    

    def parse_science(self, response):
        logging.debug("Parsing science news section")
        article_list = response.css('.multi-up__article')
        
        for article in article_list:
            url = article.css("a::attr(href)").get()
            
            if url and url not in self.processed_urls:
                self.processed_urls.add(url)
                full_url = response.urljoin(url)
                logging.debug(f"Following article URL: {full_url}")

                yield response.follow(full_url, self.parse_article, meta={"url": full_url})   

    def parse_tech_and_media(self, response):
        logging.debug("Parsing tech and media news section")
        article_list = response.css('.multi-up__article')
        
        for article in article_list:
            url = article.css("a::attr(href)").get()
            
            if url and url not in self.processed_urls:
                self.processed_urls.add(url)
                full_url = response.urljoin(url)
                logging.debug(f"Following article URL: {full_url}")

                yield response.follow(full_url, self.parse_article, meta={"url": full_url})   

    def parse_weather(self, response):
        logging.debug("Parsing weather news section")
        article_list = response.css('.multi-up__article')
        
        for article in article_list:
            url = article.css("a::attr(href)").get()
            
            if url and url not in self.processed_urls:
                self.processed_urls.add(url)
                full_url = response.urljoin(url)
                logging.debug(f"Following article URL: {full_url}")

                yield response.follow(full_url, self.parse_article, meta={"url": full_url})   

    def parse_photos(self, response):
        logging.debug("Parsing photos news section")
        article_list = response.css(
        ".pkg.standardLead, .multi-up__article, .multi-up__tease-card--two-up, .multi-up__tease-card--three-up-main, .multi-up__tease-card--three-up, .multi-up__tease-card--four-up"
    )
        
        for article in article_list:
            url = article.css("a::attr(href)").get()
            
            if url and url not in self.processed_urls:  
                self.processed_urls.add(url)
                full_url = response.urljoin(url)
                logging.debug(f"Following article URL: {full_url}")

                yield response.follow(full_url, self.parse_article, meta={"url": full_url})

    def parse_nbc_select(self, response):
        logging.debug("Parsing nbc select news section")
        article_list = response.css('.multi-up__article')
        
        for article in article_list:
            url = article.css("a::attr(href)").get()
            
            if url and url not in self.processed_urls:
                self.processed_urls.add(url)
                full_url = response.urljoin(url)
                logging.debug(f"Following article URL: {full_url}")

                yield response.follow(full_url, self.parse_article, meta={"url": full_url})

    def parse_nbc_asian_america(self, response):
        logging.debug("Parsing nbc asian america news section")
        article_list = response.css('.multi-up__article')
        
        for article in article_list:
            url = article.css("a::attr(href)").get()
            
            if url and url not in self.processed_urls:
                self.processed_urls.add(url)
                full_url = response.urljoin(url)
                logging.debug(f"Following article URL: {full_url}")

                yield response.follow(full_url, self.parse_article, meta={"url": full_url})

    def parse_nbc_blk(self, response):
        logging.debug("Parsing nbc blk news section")
        article_list = response.css('.multi-up__article')
        
        for article in article_list:
            url = article.css("a::attr(href)").get()
            
            if url and url not in self.processed_urls:
                self.processed_urls.add(url)
                full_url = response.urljoin(url)
                logging.debug(f"Following article URL: {full_url}")

                yield response.follow(full_url, self.parse_article, meta={"url": full_url})

    def parse_nbc_latino(self, response):
        logging.debug("Parsing nbc latino news section")
        article_list = response.css('.multi-up__article')
        
        for article in article_list:
            url = article.css("a::attr(href)").get()
            
            if url and url not in self.processed_urls:
                self.processed_urls.add(url)
                full_url = response.urljoin(url)
                logging.debug(f"Following article URL: {full_url}")

                yield response.follow(full_url, self.parse_article, meta={"url": full_url})

    def parse_nbc_out(self, response):
        logging.debug("Parsing nbc out news section")
        article_list = response.css('.multi-up__article')
        
        for article in article_list:
            url = article.css("a::attr(href)").get()
            
            if url and url not in self.processed_urls:
                self.processed_urls.add(url)
                full_url = response.urljoin(url)
                logging.debug(f"Following article URL: {full_url}")

                yield response.follow(full_url, self.parse_article, meta={"url": full_url})

    def parse_article(self, response):
        logging.debug(f"Parsing article: {response.url}")
        container = response.css(".article-hero__container")
        article_body = response.css(".article-body")
        article_item = ArticleItem()

        article_item["title"] = container.css("h1::text").get()
        article_item["url"] = response.meta["url"]
        article_item["author"] = article_body.css(".byline-name a::text").get()
        article_item["publishedDate"] = response.css("time[data-testid='timestamp__datePublished']::attr(datetime)").get()
        logging.debug(f"Scraped article: {article_item}")

        yield article_item