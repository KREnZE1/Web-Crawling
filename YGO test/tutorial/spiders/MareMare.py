import scrapy



class MareMareSpider(scrapy.Spider):
    name = "MareMare"
    start_urls = [
        'https://yugioh.fandom.com/wiki/Dark_Magician',
    ]

    def parse(self, response):
        # method('Attribute', response)
        # method('Status', response)
        yield  {
            'attribute' : response.css('a::text').getall(),
        }
            
            
def method(target, response):
    attr = "test"
    data = response.css('a::attr(title)').getall()
    done = False
    for word in data:
        if done:
            attr = word
            break
        if word == target:
            done = True
            
    f = open('data.txt', 'r+')
    content = f.read()
    f.write(content+'\n'+attr)

# (data[354])[6:]
# 'name' : (response.css('h1::text').get())[6:-4],
# 'attribute' : (response.css('a::attr(href)').getall())[354][6:],
# 'attribute' : response.css('a::text').getall(),

# 'name' : response.css('title::text').getall(),