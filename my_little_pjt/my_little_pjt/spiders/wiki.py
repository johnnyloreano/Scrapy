# -*- coding: utf-8 -*-
import scrapy


class WikiSpider(scrapy.Spider):
    name = 'wiki'
    allowed_domains = ['wikipedia.com']
    #start_urls = ['http://wikipedia.com/']

    def __init__(self, name):
        self.start_urls = [name]

    def parse(self, response):
        first_heading = response.xpath('//h1[@id = "firstHeading"]') 
        wholeArticle = response.xpath('//div[@class = "mw-parser-output"]')

        wholeStructure = wholeArticle.xpath("./p | ./h2 | ./h3")
        output = open("yes.html", "w")
        for x in wholeStructure.extract():
            output.write(x)
        output.close()
