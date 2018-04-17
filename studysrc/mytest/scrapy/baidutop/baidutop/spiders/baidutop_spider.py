# encoding: utf-8
# Author: LW

import scrapy
from baidutop.items import BaidutopItem


class BaiduTopSpider(scrapy.Spider):
    name = 'baidutop'
    allowed_domains = ['baidu.com']
    start_urls = [
        'http://top.baidu.com/buzz?b=7&fr=topbuzz_b62',
        'http://top.baidu.com/buzz?b=62&fr=topcategory_c16'
    ]

    def parse(self, response):

        sel = scrapy.selector.Selector(response)
        tr = sel.xpath('//table/tr')
        items = []
        for td in tr:
            item = BaidutopItem()
            item['name'] = td.xpath('td[@class="keyword"]/a[@class="list-title"]/text()').extract()
            item['link']  = td.xpath('td[@class="keyword"]/a[@class="list-title"]/@href').extract()
            item['rank']  = td.xpath('td[@class="first"]/span/text()').extract()
            items.append(item)
        return items