import scrapy
from scrapy.spiders import CrawlSpider, Rule, Spider
from scrapy.linkextractors import LinkExtractor
from ..items import LagouCompany, LagouPosition
from scrapy_splash import SplashRequest
import json


class LagouBaseSpider(Spider):
    """
    Lagou Basic Spider
    """
    name = 'lagou'
    allow_domains = [
        'www.lagou.com',
        'm.lagou.com'
    ]
    start_urls = [
        # 'https://m.lagou.com/search.json?city=%E6%88%90%E9%83%BD&positionName=Java&pageNo=1&pageSize=15'
        # 'https://m.lagou.com/search.html'
        'https://m.lagou.com/'
        # 'https://m.lagou.com/jobs/7303334.html'
    ]

    # use splash to handler request
    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url=url, callback=self.parse_start_url, endpoint='render.html')

    def parse_start_url(self, response):
        for p_id in response.css('ul.list li::attr(data-positionid)').extract():
            p_url = f'https://m.lagou.com/jobs/{p_id}.html'
            yield SplashRequest(p_url, callback=self.parse, args={
                'wait': 0.5
            })

    def parse(self, response, **kwargs):
        def extract(selector):
            output = response.xpath(selector).extract()
            return output[0].strip() if output is not None and len(output) > 0 else None

        item = LagouPosition()
        item['id'] = response.url.split('/')[-1][:-5]
        item['name'] = extract('//div[@class="postitle"]//h2[@class="title"]/text()')
        item['company'] = extract('//div[@class="dleft"]//h2[@class="title"]/text()')
        item['salary'] = extract('//span[@class="item salary"]//span/text()')
        item['location'] = extract('//span[@class="item workaddress"]//span/text()')
        item['job_nature'] = extract('//span[@class="item jobnature"]//span/text()')
        item['work_year'] = extract('//span[@class="item workyear"]//span/text()')
        item['education'] = extract('//span[@class="item education"]//span/text()')
        item['temptation'] = extract('//div[@class="temptation"]/text()')
        item['jd'] = extract('//div[@class="content"]/text()')

        if item['jd'] is None:
            with open('error.html', 'wb') as f:
                f.write(response.body)

        yield item


class LagouCrawlSpider(CrawlSpider):
    name = 'lagou-crawl'
    allow_domains = [
        'www.lagou.com',
        'm.lagou.com'
    ]
    start_urls = [
        # 'https://m.lagou.com/search.json?city=%E6%88%90%E9%83%BD&positionName=Java&pageNo=1&pageSize=15'
        # 'https://m.lagou.com/search.html'
        'https://m.lagou.com/'
        # 'https://m.lagou.com/jobs/7303334.html'
    ]
    rules = [
        Rule(LinkExtractor, )
    ]

    # use splash to handler request
    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url=url, callback=self.parse, endpoint='render.html', args={
                'wait': 0.5
            })

    def parse_item(self, response):
        pass
