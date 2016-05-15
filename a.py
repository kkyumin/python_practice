import scrapy
from scrapy.crawler import CrawlerProcess


class Daum_Rank(scrapy.Spider):
    name = 'Daum_rank'
    start_urls = ['http://www.daum.net']

    def parse(self, response):

        titles = response.css('#realTimeSearchWord>li>div>div>span>a>strong::attr(text)').extract()
        urls = response.css('#realTimeSearchWord>li>div>div>span>a>strong::attr(href)').extract()

        print titles, urls

        titles = response.css('#realTimeSearchWord>li>div>div>span>a::attr(text)').extract()
        urls = response.css('#realTimeSearchWord>li>div>div>span>a::attr(href)').extract()

        results = zip(titles, urls)

        for titles, urls in results:
            print titles, urls


process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})

process.crawl(Daum_Rank)
process.start()