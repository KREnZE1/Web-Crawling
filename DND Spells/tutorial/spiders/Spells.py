from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from csv import reader
import scrapy



class SpellSpider(scrapy.Spider):
    name = "spells"
    start_urls = [
        'http://dnd5e.wikidot.com/spells',
    ]
    # base_url = 'http://dnd5e.wikidot.com/spell:'

    def parse(self, response):
        dataset = response.css('a::text').getall()[31:597] #[31:597]
        for data in dataset:
            name = ""
            for letter in data:
                if ord(letter)==32:
                    letter = '-'
                
                name+=letter
            
            if ((name[-5:] == '-(UA)') or (name[-5:] == '-(HB)')):
                name = name[:-5]
            
            yield {
                'name': name.lower()
            }
            
        # process = CrawlerProcess(get_project_settings())
        # with open('datei.csv', 'r') as read_obj:
        #     csv_reader = reader(read_obj)
        #     for row in csv_reader:
        #         process.crawl('searcher', domain = ('http://dnd5e.wikidot.com/spell:'+str(row)))
                

                    
        
# 'name': response.css('span::text').getall()[-1],
# 'sourcebook': response.css('p::text').get()[8:],
# 'level': response.css('em::text').get()[:1],
# 'casttime': response.css('p::text').getall()[1],
# 'range': response.css('p::text').getall()[3][1:],
# 'components': response.css('p::text').getall()[5][1:],