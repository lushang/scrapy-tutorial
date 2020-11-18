# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class TencentItem(scrapy.Item):
    name = scrapy.Field()
    detailLink = scrapy.Field()
    catalog = scrapy.Field()
    recruitNumber = scrapy.Field()
    workLocation = scrapy.Field()
    publishTime = scrapy.Field()


class LagouCompany(scrapy.Item):
    name = scrapy.Field()
    industry = scrapy.Field()
    fin_stage = scrapy.Field()
    employee = scrapy.Field()
    website = scrapy.Field()
    logo = scrapy.Field()


class LagouPosition(scrapy.Item):
    company = scrapy.Field()
    id = scrapy.Field()
    name = scrapy.Field()
    salary = scrapy.Field()
    jd = scrapy.Field()
    location = scrapy.Field()
    temptation = scrapy.Field()
    job_nature = scrapy.Field()
    work_year = scrapy.Field()
    education = scrapy.Field()
    owner = scrapy.Field()
    pub_time = scrapy.Field()
