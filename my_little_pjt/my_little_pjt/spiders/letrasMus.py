# -*- coding: utf-8 -*-
import scrapy


class LetrasmusSpider(scrapy.Spider):
    name = 'letrasMus'
    allowed_domains = ['letras.mus.br/']
    start_urls = ['https://www.letras.mus.br/pineapple/sobre-nos-poesia-acustica-2/']

    def parse(self, response):
        return self.parse_lyric(response)


    def parse_lyric(self, response):
        artist = response.xpath("//div[@class='cnt-head_title']/h2/a/text()").extract() 
        music = response.xpath("//div[@class='cnt-head_title']/h1/text()").extract() 
        lyric = response.xpath("//div[@class='cnt-letra p402_premium']/p/text()").extract()
        yield {
            'Artist' : artist,
            'Music' : music,
            'Lyric' : lyric
        }
