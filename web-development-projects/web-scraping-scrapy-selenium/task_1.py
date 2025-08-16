# Obligatory assignment 3

# Task 1

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from oblig321.items import VergeReview

class Crawling_and_Scraping(CrawlSpider):
    name = "spidy"
    allowed_domains = ["theverge.com"]
    start_urls = ["https://www.theverge.com/reviews"]

    rules = (
        Rule(LinkExtractor(allow=r"https://www.theverge.com/\d+/[^/]+$"), 
             callback="parse_item", follow=True),
        Rule(LinkExtractor(allow=r"https://www.theverge.com/[a-z\-]+/\d+/[^/]+$"),
            callback="parse_item", follow=True),
    )

    def parse_item(self, response):
        try:
            title = response.css("h1::text").extract_first()
            authorname = response.css("span[class^='_114qu8c2 _114qu8c'] a::text").get()
            
            if title and authorname:
                item = VergeReview()
                authorlink = response.css("span[class^='_114qu8c2 _114qu8c'] a::attr(href)").get()
                if authorlink:
                    item["authorlink"] = response.urljoin(authorlink)
                else:
                    item["authorlink"] = None
                item["authorname"] = authorname.strip()
                item["title"] = title.strip()
                item["url"] = response.url
                yield item
        except Exception as e:
            self.logger.error(f"URL that got the error {response.url}: {e}")