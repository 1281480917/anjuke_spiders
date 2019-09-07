import scrapy
from anjuke.items import AnjukeItem


class DmozSpider(scrapy.Spider):
    name = "anju"
    start_urls = [
        "https://www.anjuke.com/chengdu/cm/#"
    ]

    def start_requests(self):
        yield scrapy.http.Request(self.start_urls[0],callback=self.start)

    def start(self, response):
        selector = scrapy.Selector(response)
        # comunity_url=selector.re("https://www.anjuke.com/deyang/cm707.*?/")
        comunity_url = selector.xpath(
            '//*[@id="content"]/ul[1]/li/em/a/@href').extract()
        print(comunity_url)
        for url in comunity_url:
            yield scrapy.http.Request(url, callback=self.info)
        next_url = selector.re(
            '<a href="(.+?)"><span class="nextpage"><ins>下一页</ins> ')[0]
        print(next_url)
        yield scrapy.http.Request(next_url, callback=self.start)

    def info(self, response):
        item = AnjukeItem()
        selector = scrapy.Selector(response)
        community = selector.xpath(
            '//*[@id="content"]/div[2]/div/div/h3/text()').extract()[0]
        average_price = selector.xpath(
            '//*[@id="content"]/div[2]/div/div/p/span/em/text()').extract()[0]
        item['community'] = community
        item['average_price'] = average_price
        print(item['community'], item['average_price'])
        print(type(item['community']))
        print(item)
        print(type(item))
        yield item

    def parse(self, response):
        pass
