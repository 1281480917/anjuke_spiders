# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy import signals
import json
import codecs
from anjuke.items import AnjukeItem
import csv
class CSVPipeline(object):

   def open_spider(self,spider):
      self.csvwriter = csv.writer(open('anju.csv', 'w'), delimiter=',')
      self.csvwriter.writerow(['community','average_price123'])

   def process_item(self, item, spider):
        #self.csvwriter = csv.writer(open('anju.csv', 'w'), delimiter=',')
        rows=[]
        rows.append(item['community'])
        rows.append(item['average_price'])
        self.csvwriter.writerow(rows)
        return item

   def close_spider(self, spider):
       self.csvwriter.close()


class JsonWithEncodingCnblogsPipeline(object):

    def open_spider(self,spider):
        self.file = codecs.open('anju.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line)
        return item

    def close_spider(self, spider):
        self.file.close()

if __name__ == '__main__':
    CSVPipeline().open_spider('')