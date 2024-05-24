import scrapy
from articlescraper.items import ArticleItem

class NbcnewsSpiderSpider(scrapy.Spider):
    name = "nbcnews_spider"
    allowed_domains = ["www.nbcnews.com"]
    start_urls = ["https://www.nbcnews.com/"]
    processed_urls = set()

    section_parsers = {
        'us-news': 'parse_us_news',
        'politics': 'parse_politics',
        'world': 'parse_world',
        'local': 'parse_local',
        'business': 'parse_business',
        'sports': 'parse_sports',
        'paris-2024-olympics': 'parse_paris_2024_olympics',
        'investigations': 'parse_investigations',
        'culture-&-trends': 'parse_culture_and_trends',
        'health': 'parse_health',
        'science': 'parse_science',
        'tech-&-media': 'parse_tech_and_media',
        'weather': 'parse_weather',
        # 'video-features': 'parse_video_features',
        'photos': 'parse_photos',
        'nbc-select': 'parse_nbc_select',
        'nbc-asian-american': 'parse_nbc_asian_america',
        'nbc-blk': 'parse_nbc_blk',
        'nbc-latino': 'parse_nbc_latino',
        'nbc-out': 'parse_nbc_out',
    }

    def parse(self, response):
        section_container = response.css(".menu-section.menu-section-sections.menu-section-main")
        section_list = section_container.css(".menu-list .menu-list-item")
        
        for url in section_list:
            section_url = url.css("a").attrib["href"]
            section_name = url.css("span::text").get()

            yield response.follow(section_url, self.parse_section, meta={'section_name': section_name})

    def parse_section(self, response):
        section_name = response.meta["section_name"]
        
        if section_name != "parse_video_features":
            parse_method_name = self.section_parsers.get(section_name, "parse_generic")
            parse_method = getattr(self, parse_method_name)
        
            yield from parse_method(response)

    def parse_us_news(self, response):
        article_list = response.css('.multi-up__article')
        
        for article in article_list:
            url = article.css("a.tease-card__picture-link").attrib['href']
            
            if url and url not in self.processed_urls:
                self.processed_urls.add(url)
                full_url = response.urljoin(url)

                yield response.follow(full_url, self.parse_article, meta={"url": full_url})

    def parse_generic(self, response):
        articles = response.css('.multi-up__article')
        
        for article in articles:
            url = article.css("a.tease-card__picture-link").attrib['href']
            full_url = response.urljoin(url)
            yield response.follow(full_url, self.parse_article, meta={"url": full_url})

    def parse_article(self, response):
        container = response.css(".article-hero__container")
        article_body = response.css(".article-body")
        article_item = ArticleItem()

        article_item["title"] = container.css("h1::text").get()
        article_item["url"] = response.meta["url"]
        article_item["author"] = article_body.css(".byline-name a::text").get()
        article_item["publishedDate"] = response.css("time[data-testid='timestamp__datePublished']::attr(datetime)").get()

        yield article_item