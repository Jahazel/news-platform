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
        try:
            logging.info(f"Processing item: {item}")
            self.collection.insert_one(dict(item))
            logging.info("Item inserted into articles collection.")
        except Exception as e:
            logging.error(f"Error inserting item: {item}, error: {e}")
        return item