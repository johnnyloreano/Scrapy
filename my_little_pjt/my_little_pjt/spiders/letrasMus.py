# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request

class LetrasmusSpider(scrapy.Spider):
    name = 'letrasMus'
    allowed_domains = ['letras.mus.br/']

    def __init__(self,artist):
        self.start_urls = [artist]

    def parse(self, response):
        best_songs = response.xpath("//div[@class='artista-top g-sp g-pr']/ol/li/a/@href").extract()
        for song in best_songs:
            path = response.urljoin(song)
            yield Request(path, callback = self.parse_lyric, dont_filter=True)


    def parse_lyric(self, response):
        artist = response.xpath("//div[@class='cnt-head_title']/h2/a/text()").extract() 
        music = response.xpath("//div[@class='cnt-head_title']/h1/text()").extract() 
        lyric = response.xpath("//div[@class='cnt-letra p402_premium']/p/text()").extract()
        yield {
            'Artist' : artist,
            'Music' : music,
            'Lyric' : lyric
        }
