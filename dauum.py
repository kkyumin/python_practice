#-*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import scrapy
from scrapy.crawler import CrawlerProcess


def reprunicode(u):
    return repr(u).decode('raw_unicode_escape')

class MyCrawler(scrapy.Spider):
    name = 'NAME'
    start_urls = ['http://www.daum.net']

    def parse(self, response):
        a = response.css("ol#realTimeSearchWord>li>div>div[aria-hidden='true']>span.txt_issue>a::attr(href)").extract()
        b = []
        temp = "ol#realTimeSearchWord>li>div>div.realtime_item" + str(1) + "[aria-hidden='true']>span.txt_issue>a>strong::text"
        b.append(response.css(temp).extract())
        for i in range(2,11):
            temp = "ol#realTimeSearchWord>li>div>div.realtime_item"+str(i)+"[aria-hidden='true']>span.txt_issue>a::text"
            b.append(response.css(temp).extract())

        result = [(i, j) for i,j in zip(a,b)]

        for k in range(10):
            print repr(result[k]).decode('raw_unicode_escape')
        pass

process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})

process.crawl(MyCrawler)
process.start()