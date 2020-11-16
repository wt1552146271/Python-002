# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql

class MaoyanPipeline:
    # def process_item(self, item, spider):
    #     return item

    # def process_item(self, item, spider):
    #     movie_name = item['movie_name']
    #     movie_type = item['movie_type']
    #     release_time = item['release_time']
    #     output = f'|{movie_name}|\t|{movie_type}|\t|{release_time}|\n\n'
    #     with open('./maoyanmovie.txt', 'a+', encoding='utf-8') as article:
    #         article.write(output)
    #     return item

    def process_item(self, item, spider):
        conn = pymysql.connect(
            host='localhost',
            port=3306,
            user='root',
            passwd='',
            db='test_db',
            charset='utf8'
        )
        cursor = conn.cursor()
        movie_name = item['movie_name']
        movie_type = item['movie_type']
        release_time = item['release_time']
        insert_sql = 'INSERT INTO movies(movie_name, movie_type,release_time) VALUES (%s, %s,%s)'
        cursor.execute(insert_sql, (movie_name, movie_type,release_time))
        conn.commit()
        cursor.close()
        conn.close()

        return item
