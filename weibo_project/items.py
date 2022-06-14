# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WeiboProjectItem(scrapy.Item):
    name = scrapy.Field()       # 微博热搜的名字
    hot_order = scrapy.Field()  # 该微博的热搜排名
    username = scrapy.Field()   # 该微博的作者
    weibo_id = scrapy.Field()   # 某条微博的ID
    detail_url = scrapy.Field() # 该微博的细节url

class CommentItem(scrapy.Item):
    hot_point_name = scrapy.Field()
    hot_point_auth_name = scrapy.Field()
    hot_point_order = scrapy.Field()
    hot_point_weibo_id = scrapy.Field()
    hot_point_detail_url = scrapy.Field()
    comment_user_name = scrapy.Field()
    comment_user_id = scrapy.Field()
    comment_user_location = scrapy.Field()
    comment_user_content = scrapy.Field()
