# -*- coding: utf-8 -*-
import scrapy
from ..items import ScrapyItem
from os import path
from os import mkdir

class WikiSpider(scrapy.Spider):
    name = 'wiki'
    allowed_domains = ['wikipedia.com']
    localPath = "../assets/wiki/"
    standardUrl = "https://pt.wikipedia.org/wiki/   "
    #start_urls = ['http://wikipedia.com/']

    def __init__(self, name):
        self.start_urls = [name]    

    def parse(self, response):  
        test = ScrapyItem()
        firstImage = response.xpath('//table[@class = "infobox_v2"]//tr//td/a/img/@src').extract_first()
        test["image_urls"] = ["https:" + firstImage]
        return test
        first_heading = response.xpath('//h1[@id = "firstHeading"]')
        
        
        first_heading_text = first_heading.xpath("./text()").extract_first()

        if(not self.createStructure(first_heading_text) ):
            pass
        self.localPath += first_heading_text + "/"
        wholeArticle = response.xpath('//div[@class = "mw-parser-output"]')

        wholeStructure = wholeArticle.xpath("./p | ./h2 | ./h3")
        output = open(self.localPath + first_heading_text + ".html", "w")

        output.write(first_heading.extract_first())
        for x in wholeStructure.extract():
            output.write(x)
        output.close()

    def createStructure(self, title):
        if ( not path.exists(self.localPath + title) ):
            mkdir(self.localPath + title)
            return True
        else:
            return False

    def url_join(self, urls):
        joined_urls = []
        for url in urls:
            joined_urls.append(self.standardUrl + url)

        return joined_urls