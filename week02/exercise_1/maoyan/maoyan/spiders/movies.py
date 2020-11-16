import scrapy
from bs4 import BeautifulSoup
import lxml.etree
from ..items import MaoyanItem
from scrapy.selector import Selector
#import scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware

class MoviesSpider(scrapy.Spider):
    name = 'movies'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3']

    # def parse(self, response):
    #     pass

    def start_requests(self):		# 固定的名字
        url = 'https://maoyan.com/films?showType=3'
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        try:
            movies = Selector(response=response).xpath('//div[@class="movie-hover-info"]')
            # for movie in movies:
            for i in range(10):
                item = MaoyanItem()
                movie_name = movies[i].xpath('./div/span/text()').extract_first()

                movie_type_rawlist = movies[i].xpath('./div[2]/text()').extract()
                movie_type = movie_type_rawlist[1].strip()

                movie_start_time_rawlist = movies[i].xpath('./div[4]/text()').extract()
                release_time = movie_start_time_rawlist[1].strip()

                item['movie_name'] = movie_name
                item['movie_type'] = movie_type
                item['release_time'] = release_time
                yield item
        except Exception as e:
            print(e)
