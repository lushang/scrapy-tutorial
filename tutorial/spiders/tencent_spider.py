import scrapy


class TencentSpider(scrapy.spiders.Spider):
    name = 'tencent'
    allowed_domains = ['careers.tencent.com']
    start_urls = [
        # 'https://careers.tencent.com/jobdesc.html?postId=1288374893766778880',
        'https://www.lagou.com/jobs/7878216.html?show=d401b508236f447c9b1e046bbf1fb7c4'
    ]

    def parse(self, response):
        print(f"Existing settings: {self.settings.attributes.get('MONGO_URI')}")
        # with open('tencent-recruiting.txt', 'wb') as f:
        #     f.write(response.body)
