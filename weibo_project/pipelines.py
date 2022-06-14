# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import psycopg2

class WeiboProjectPipeline:
    
    def open_spider(self,spider):
        hostname = 'localhost'
        username = 'postgres'
        password = 'mrdl7824'
        database = 'weiboComments'
        self.connection = psycopg2.connect(host=hostname,user=username,password=password,dbname=database,port="5432")
        self.cur = self.connection.cursor()
        
    def close_spider(self,spider):
        self.cur.close()
        self.connection.close()
        
    def process_item(self, item, spider):
        self.cur.execute("INSERT INTO public.comments(hot_point_name ,hot_point_auth_name ,hot_point_order ,hot_point_weibo_id ,hot_point_detail_url ,comment_user_name ,comment_user_id ,comment_user_location ,comment_user_content) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s);",
        (item['hot_point_name'],item['hot_point_auth_name'],item['hot_point_order'],item['hot_point_weibo_id'],item['hot_point_detail_url'],item['comment_user_name'],item['comment_user_id'],item['comment_user_location'],item['comment_user_content']))
        self.connection.commit()
        return item
