# create a crawler class
# create a scraper class

# customize the pipeline
import scrapy
import urllib
import os
import uuid

from scrapy.spiders import CrawlSpider


class CrawlRestaurant(CrawlSpider):
    name = "totalhappyhour.com"
    allowed_domains = ["totalhappyhour.com"]
    start_urls = ["https://www.totalhappyhour.com"]

    def parse(self, response):
        # select a city
        city_urls = response.xpath(
            "//div[@class='city-selector']/a/@href").extract()
        for url in city_urls:
            url = self.start_urls[0] + url
            yield scrapy.Request(url, callback=self.get_restaurant)

    def get_restaurant(self, response):
        restaurants_urls = response.xpath(
            "//div[@class='profiles']/div[contains(@class, 'profile')]/h2/a/@href").extract()
        for restaurant_url in restaurants_urls:
            restaurant_url = self.start_urls[0] + restaurant_url
            yield scrapy.Request(restaurant_url, callback=self.get_page)

    def get_page(self, response):
        filename = str(uuid.uuid4())
        urllib.urlretrieve(response.url, os.path.abspath(
            '../data/cache/{}').format(filename))


class ScrapeRestraurant(scrapy.Spider):
    pass
