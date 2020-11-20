# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo
from datetime import datetime


class MongoPipeline(object):
    collection_name = 'lagou_items'
    err_name = 'error_ids'

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DATABASE', 'items')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]
        self.collection = self.db[self.collection_name]
        self.err_cl = self.db[self.err_name]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        item_dict = dict(item)
        c_id = item_dict.get('id')
        if item_dict.get('name') is None:
            self.err_cl.replace_one(
                {'id': c_id},
                {'id': c_id, 'time': datetime.now()},
                upsert=True
            )
        else:
            self.err_cl.delete_one({'id': c_id})
            if self.collection.find_one({'id': c_id}) is None:
                self.collection.insert_one(item_dict)
        return item
