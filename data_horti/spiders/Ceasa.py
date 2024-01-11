import scrapy
from data_horti.items import DataHortiItem


class CeasaSpider(scrapy.Spider):
    name = "Ceasa"
    allowed_domains = ["www.ceasa.gov.br"]
    start_urls = ["http://www.ceasa.gov.br/precos.php?TIP=1&P01=6&P02=1&P03=0&P04=0"]

    def parse(self, response):
        rows = response.css('.tab2Precos tr')
        header = rows[0].css('td')
        cotacao = []

        for row in rows:
            if row == rows[0]: continue
            columns = row.css('td::text')

            for i, column in enumerate(columns):
                if column == columns[0]: continue
                
                productName = columns[0].get()
                value = column.get()
                marketName = header[i].css('td ::text').get().replace(' ', '').replace(' )', ')').replace('( ', '(')
                update = header[i].css('td *::text').extract()[1]

                horti = DataHortiItem(product=productName, market=marketName, update=update, value=value)
                cotacao.append(horti)

        yield { 'cotacao': cotacao }
