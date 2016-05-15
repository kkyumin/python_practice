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
    start_urls = ['http://m.kobus.co.kr/web/m/reservation/sel_seat.jsp']

    def parse(self, response):
        a = response.css("body").extract()

        print repr(a).decode('raw_unicode_escape')


process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})

process.crawl(MyCrawler)
process.start()