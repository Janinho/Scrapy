
#Importando o scrapy

import scrapy
from scrapy.utils.response import open_in_browser


# scrapy runspider -a produto=telefone questao02.py --nolog


class MercadoLivre(scrapy.Spider):
    #Nomeando a classe
    name = "MercadoLivre"

    def __init__(self, produto="", **kwargs):
        self.start_urls = {"https://lista.mercadolivre.com.br/%s" % produto}
        super().__init__(**kwargs)

    
    def parse(self, response):
        nomes_produtos = response.css(".main-title::text").extract()
        preco_produtos = []

        for item in response.css(".item__price"):
            preco = item.css(".price__fraction::text").extract_first()

            if item.css(".price__decimals::text").extract_first():
                preco += "," + item.css(".price__decimals::text").extract_first()

            preco_produtos.append(preco)

        for nome, preco in zip(nomes_produtos, preco_produtos):
            yield {
                "NOME_PRODUTO" : nome,
                "PRECO" : preco
            }
        pagination = response.xpath("//ul[@role]/li[last()]/a")