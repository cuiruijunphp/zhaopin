# -*- coding: utf-8 -*-
import scrapy


class SearchSpider(scrapy.Spider):
    name = "search"
    allowed_domains = ["zhipin.com"]
    start_urls = ['https://www.zhipin.com/boss/search/geeks.json?page=1&keywords=php&city=101280600']

    def start_requests(self):
        url = 'http://www.zhipin.com/captcha/randkey.json'
        yield scrapy.Request(url, method='POST',callback=self.parse)

    def parse(self, response):
        print(response.body)
