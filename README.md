### Install and start a tutorial project ###
1. Install: `pip install scrapy`
2. start a tutorial project: `scrapy startproject tutorial`


### Executing JavaScript in Scrapy with Splash ###
1. Run a instance of splash locally with docker: `docker run -p 8050:8050 scrapinghub/splash`
2. Change `settings.py` of the project:  
   ```python
   SPLASH_URL = 'http://localhost:8050'

   
   DOWNLOADER_MIDDLEWARES = {
       'scrapy_splash.SplashCookiesMiddleware': 723,
       'scrapy_splash.SplashMiddleware': 725,
       'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
   }
   
   
   SPIDER_MIDDLEWARES = {
       'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,
   }
    
    
   DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'
   HTTPCACHE_STORAGE = 'scrapy_splash.SplashAwareFSCacheStorage'
   ```
3. Use `SplashRequest`
   ```python
   from scrapy_splash import SplashRequest

   def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url=url, callback=self.parse, endpoint='render.html', args={
                'wait': 0.5
            })
   ```

### MongoDB in docker ###
1. create a volume for data: `docker volume create mongo-vol`
2. pull image from docker repo: `docker pull mongo`
3. start the MongoDB container:  
   `docker run --name scrapy-mongo -v mongo-vol:/data/db -p 27017:27017 -d mongo`


### Reference ###

1. [Scrapy 2.4 documentation](https://docs.scrapy.org/en/latest)
2. [Python 网络爬虫教程](https://www.bookstack.cn/read/piaosanlang-spiders/c41d7333f0fc34db.md)
3. [How to execute JavaScript with Scrapy?](https://www.scrapingbee.com/blog/scrapy-javascript/)
4. [Docker:mongo](https://hub.docker.com/_/mongo)
5. [Crawling with Scrapy – Javascript Generated Content](http://scrapingauthority.com/scrapy-javascript)
6. [XPath 教程](https://www.w3school.com.cn/xpath/index.asp)
7. [github:scrapy-splash](https://github.com/scrapy-plugins/scrapy-splash)
8. [PyMongo 3.11.1 Documentation](https://pymongo.readthedocs.io/en/stable/index.html)