import scrapy
from scrapy.shell import inspect_response
import re

class UOLpider(scrapy.Spider):
    name = "UOL"
   

    start_urls = {
        'file:///C:/Users/diego.silva/Downloads/Codigos-20190505T223057Z-001/Codigos/EXERCICIO_01/uol.html'
    }

    def parse(self, response):
        elementos = response.css(".HU_currency__item:nth-child(1)")
        for elemento in elementos:
              
                yield {
                    'A COTAÇÃO DOLAR É': elemento.css("span::text")[1].extract()
                    
                }
