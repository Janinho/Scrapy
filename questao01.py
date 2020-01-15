import scrapy
from scrapy.shell import inspect_response
import re



class UolSpider(scrapy.Spider):
    name = "Uol"

    start_urls = {
        'https://www.uol.com.br'
    }

    def parse (self, response):
       	elementos = response.css(".HU_currency__item:nth-child(1)")

        for elemento in elementos:
            #    open_in_browser(response)
                
                 print('A COTAÇÃO DOLAR É ' + elemento.css("span::text")[1].extract())
                    
               