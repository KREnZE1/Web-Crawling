from asyncio.windows_events import NULL
from unittest import case
import scrapy


class BannedcardsSpider(scrapy.Spider):
    name = 'bannedcards'
    start_urls = ['https://yugioh.fandom.com/wiki/Forbidden']

    def parse(self, response):
        cards = response.css('td.smwtype_wpg')
        for card in cards:
            link = card.css('a::attr(href)').get()
            
            if link is not None:
                yield scrapy.Request('https://yugioh.fandom.com'+link, callback = self.parse_card)

    def parse_card(self, response):
        name = response.css('h1.page-header__title::text').get().strip()
        rows = response.css('tr.cardtablerow')
        cardType = ""
        attribute = ""
        
        for row in rows:
            if row.css('a::attr(title)').get() == 'Card type':
                cardType = row.css('td.cardtablerowdata a::attr(title)').get().strip()
            if row.css('a::attr(title)').get() == 'Attribute' or row.css('a::attr(title)').get() == 'Property':
                attribute = row.css('td.cardtablerowdata a::attr(title)').get().strip()
            if cardType == 'Monster Card':
                print()
             
             
        yield { 
            'Name': name,
            'Card Type': cardType,        
            'Attribute': attribute
        }
        
# https://yugioh.fandom.com/wiki/Amazoness_Archer
# https://yugioh.fandom.com /wiki/Amazoness_Archer
# https://db.ygoprodeck.com/banlist/