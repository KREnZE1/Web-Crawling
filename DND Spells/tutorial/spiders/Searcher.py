import scrapy

class SearchSpider(scrapy.Spider):
    name = "searcher"
    start_urls = [
        'http://dnd5e.wikidot.com/spells',
    ]

    def parse(self, response):
        if response.request.url != 'http://dnd5e.wikidot.com/spells':
            yield {
                'name': response.css('span::text').getall()[-1],
                'sourcebook': unify(response),
                'level': choose(response),
                'casttime': response.css('p::text').getall()[1], #Decompose (und andere Twitterzauber) funktionieren nicht
                'range': response.css('p::text').getall()[3][1:],
                'components': response.css('p::text').getall()[5][1:],
                'duration': response.css('p::text').getall()[7],
                'spell list': classcheck(response)
            }
        else:
            for data in response.css('a::text').getall()[31:597]: #31 ist der erste, 597 der letzte Zauber
                if (data[-5:] == ' (UA)') or (data[-5:] == ' (HB)'):
                    continue
                data = castLow(data)
                currUrl = response.request.url
                yield scrapy.Request(currUrl[:-1]+':'+data, callback=self.parse)
                       
                       
def classcheck(response):
    index = 31
    result = ''
    while response.css('a::text').getall()[index][0].isupper():
        result+= response.css('a::text').getall()[index]+', '
        index+=1
    return result[:-2]
        
def unify(response):
    unified = response.css('p::text').get()[8:]
    if unified[-1] == '(':
        unified = unified[:-2]
    return unified    
            
def choose(response):
    level = response.css('em::text').get()
    if level[:1].isnumeric():
        return level[:1]
    else:
        return 'Cantrip'

def castLow(word):
    name = ""
    for letter in word:
        if ord(letter) == 39: letter = ""
        elif (ord(letter)<65 or (ord(letter)>90 and ord(letter)<97) or ord(letter)>122):
            letter = '-'
                
        name+=letter
            
    return name.lower()