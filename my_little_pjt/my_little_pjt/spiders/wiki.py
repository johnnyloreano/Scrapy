# -*- coding: utf-8 -*-
import scrapy
from os import path
from os import mkdir

class WikiSpider(scrapy.Spider):
    name = 'wiki'
    allowed_domains = ['wikipedia.com']
    path = "../assets/wiki/"
    #start_urls = ['http://wikipedia.com/']

    def __init__(self, name):
        self.start_urls = [name]    

    def parse(self, response):
        first_heading = response.xpath('//h1[@id = "firstHeading"]')
        
        first_heading_text = first_heading.xpath("./text()").extract_first()

        if(not self.createStructure(first_heading_text) ):
            pass
        self.path += first_heading_text + "/"
        wholeArticle = response.xpath('//div[@class = "mw-parser-output"]')

        wholeStructure = wholeArticle.xpath("./p | ./h2 | ./h3")
        output = open(self.path + first_heading_text + ".html", "w")

        output.write(first_heading.extract_first())
        for x in wholeStructure.extract():
            output.write(x)
        output.close()

    def createStructure(self, title):
        if ( not path.exists(self.path + title) ):
            mkdir(self.path + title)
            return True
        else:
            return False