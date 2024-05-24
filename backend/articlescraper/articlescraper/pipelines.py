import pymongo
import logging

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class ArticlescraperPipeline(object):
    def __init__(self):
        self.conn = pymongo.MongoClient(
            "localhost",
            27017
        )
        db = self.conn["articleDB"]
        self.collection = db["articles"]
        logging.info("MongoDB connection opened and collection selected.")

    def process_item(self, item, spider):
        self.collection.update_one(
            {'url': item['url']},  # Assuming 'url' is unique
            {'$set': item},
            upsert = True
        )
        return item