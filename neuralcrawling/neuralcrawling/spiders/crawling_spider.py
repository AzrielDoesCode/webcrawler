from scrapy.spiders import CrawlSpider, Rule #Base class and Rules
from scrapy.linkextractors import LinkExtractor #Extractor for links


class CrawlingSpider(CrawlSpider):  #inheritance form CrawlSpider base class
    name = "spideyone"
    allowed_domains = ["toscrape.com"]
    start_urls = ["http://books.toscrape.com/"]

    rules = (
        Rule(LinkExtractor(allow="catalogue/category")),  #if only one rule, then use this commma 
        #because now itll be recognised as a tuple, if u want to add more u can remove the comma but otherwise the comma
        
    )