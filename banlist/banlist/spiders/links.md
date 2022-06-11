# CSS

Name: response.css('h1.page-header__title::text').get().strip()
Card Type:
All rows: response.css('tr.cardtablerow')
Text of a single row header: response.css('th.cardtablerowheader::text').get()
Text of a single row item: response.css('td.cardtablerowdata::text').get().strip()

<https://yugipedia.com/wiki/Forbidden>
All oddnumbered Rows = response.css('tr.row-odd')
All evennumbered Rows = response.css('tr.row-even')

Alle Karten:
Rows: response.css('li.category-page__member')
Nächster Link: response.css('a.category-page__member-link::attr(href)').get()
Name: response.css('a.category-page__member-link::text').get().strip()
