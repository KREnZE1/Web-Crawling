import scrapy


class PediaSpider(scrapy.Spider):
    name = 'pedia'
    start_urls = ['https://yugipedia.com/wiki/Forbidden']

    def parse(self, response):
        pass
        
