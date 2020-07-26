import scrapy
from bs4 import BeautifulSoup
import time
from ..items import MaoyanmovieItem
import lxml.etree


class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3']

    def parse(self, response):
        bs_info = BeautifulSoup(response.text, "html.parser")
        movie_list = bs_info.find_all('div', attrs={'class': 'channel-detail movie-item-title'})
        for movie in movie_list:
            item = MaoyanmovieItem()
            link = "https://maoyan.com" + movie.find('a').get('href')
            item['link'] = link
            yield scrapy.Request(url=link, meta={'item': item}, callback=self.parse2)

    def parse2(self,response):
        item = response.meta['item']
        selector = lxml.etree.HTML(response.text)
        file_name = selector.xpath('//div[@class="movie-brief-container"]/h1/text()')
        film_type = selector.xpath('//a[contains(@href, "/films?catId=")]/text()')
        release_time = selector.xpath('//li[@class="ellipsis"][3]/text()')
        item["file_name"] = file_name
        item["film_type"] = film_type
        item["release_time"] = release_time
        yield item


