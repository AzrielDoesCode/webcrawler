from scrapy.spiders import CrawlSpider, Rule #Base class and Rules
from scrapy.linkextractors import LinkExtractor #Extractor for links


class CrawlingSpider(CrawlSpider):  #inheritance form CrawlSpider base class
    name = "spideyone"
    allowed_domains = ["toscrape.com"]
    start_urls = ["http://books.toscrape.com/"]

    rules = (
        Rule(LinkExtractor(allow="catalogue/category")),  #if only one rule, then use this commma 
        #because now itll be recognised as a tuple, if u want to add more u can remove the comma but otherwise the comma
        
        Rule(LinkExtractor(allow="catalogue/book" , deny="category"), callback="parse_item") #callback is a function that will be called for each item"parse_item


    )

    def parse_item(self, response):
        yield {
            "title": response.xpath('//h1/text()').get(),
            "price": response.xpath('//p[@class="price_color"]/text()').get(),
            "stock": response.xpath('//p[@class="instock availability"]/text()').get(),
            "description": response.xpath('//article/p/text()').get(),