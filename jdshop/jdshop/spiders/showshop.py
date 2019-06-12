# -*- coding: utf-8 -*-
import time

import scrapy
from fake_useragent import UserAgent
import re
import json
from scrapy.linkextractors import LinkExtractor

headr = UserAgent()


class ShowshopSpider(scrapy.Spider):
    name = 'showshop'
    allowed_domains = ['jd.com']
    start_urls = ['https://dc.3.cn/category/get']
    custom_settings = {
        'LOG_LEVEL': 'DEBUG',
        'LOG_FILE': '5688_log_%s.txt' % time.time(),
        "DEFAULT_REQUEST_HEADERS": {'User-Agent': headr.random},
    }

    def parse(self, response):
        good_urla = json.loads(response.text)
        good_url = json.dumps(good_urla, ensure_ascii=False)
        # print(good_url)
        one_url = re.findall(pattern='{"n": "(.*?)", "s"', string=good_url)
        goodone_url = []
        for v in one_url:
            if 'list' in v and 'coll' not in v and 'rich' not in v:
                goodone_url.append(v)
        for url in goodone_url:
            a = f'https://{url}'
            yield scrapy.Request(url=a, callback=self.parse2)

    def parse2(self, response):
        urls = response.xpath('//*[@id="plist"]/ul/li/div/div[1]/a/@href').extract()
        next_url = response.xpath("//a[@class='pn-next']/@href").extract()
        for v in urls:
            urlv = f'https:{v}'
            print(urlv)
            yield scrapy.Request(url=urlv, callback=self.parse3)
        for x in next_url:
            next_urlx = f'https://list.jd.com/{x}'
            yield scrapy.Request(url=next_urlx, callback=self.parse2)

    def parse3(self, response):
        pass
