# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class MaoyanmoviePipeline:
    # def process_item(self, item, spider):
    #     return item
   def process_item(self, item, spider):
        file_name = item['file_name']
        film_type = item['film_type']
        release_time = item['release_time']
        output = f'|{file_name}|\t|{film_type}|\t|{release_time}|\n\n'
        with open('./maoyanmovie.txt', 'a+', encoding='utf-8') as article:
            article.write(output)
        return item