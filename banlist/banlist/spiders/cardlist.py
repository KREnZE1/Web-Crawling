import scrapy


class PediaSpider(scrapy.Spider):
    name = 'cards'
    start_urls = ['https://yugioh.fandom.com/wiki/Category:TCG_cards']

    def parse(self, response):
        rows = response.css('li.category-page__member')
        for row in rows:
            nextPage = row.css('a.category-page__member-link::attr(href)').get()
            if nextPage is not None:
                yield scrapy.Request('https://yugioh.fandom.com'+nextPage, callback = self.parseDecide)
                
        # nextPage = response.css('div.category-page__pagination a.category-page__pagination-next.wds-button.wds-is-secondary::attr(href)').get()
        # if nextPage is not None:
        #     yield scrapy.Request(nextPage, callback = self.parse)
        
    def parseCard(self, response):
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
    
    def parseDecide(self, response):
        rows = response.css('tr.cardtablerow')
        for row in rows:
            if row.css('a::attr(title)').get() == 'Card type' and row.css('td.cardtablerowdata a::attr(title)').get().strip() == 'Monster':
                url = response.request.url
                yield scrapy.Request(url, callback = self.parseMon)
    
    def parseMon(self, response):
        rows = response.css('tr.cardtablerow')
        for row in rows:
            pass
            
    
    
# Monster, Spells, Traps in einzelne Datein speichern, 
# indem in der 2. Methode nach dem Kartentyp gefiltert wird, 
# wenn es ein Monster (/Spell/Trap) ist weitermachen und speichern
