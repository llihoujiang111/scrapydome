# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JdallItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 商品信息
    shop_id = scrapy.Field()
    url = scrapy.Field()
    title = scrapy.Field()
    brand = scrapy.Field()
    brand_url = scrapy.Field()
    price = scrapy.Field()
    comment_num = scrapy.Field()
    good_comment_rate = scrapy.Field()
    good_comment = scrapy.Field()
    general_count = scrapy.Field()
    poor_count = scrapy.Field()
    hot_comment_dict = scrapy.Field()
    default_comment_num = scrapy.Field()
    # 主键 评论ID
    comment_id = scrapy.Field()
    comment_context = scrapy.Field()
    comnent_time = scrapy.Field()
    # 用户评分
    comment_score = scrapy.Field()
    # 来源
    comment_source = scrapy.Field()
    # 型号
    produce_size = scrapy.Field()
    # 颜色
    produce_color = scrapy.Field()
    # 用户级别
    user_level = scrapy.Field()
    # 用户京享值
    user_exp = scrapy.Field()
    # 评价点赞数
    comment_thumpup = scrapy.Field()
    # 商家回复
    comment_reply_content = scrapy.Field()
    comment_reply_time = scrapy.Field()
    append_comment = scrapy.Field()
    append_comment_time = scrapy.Field()
    
    # 这个方法会在pipelines里面使用
    def get_insert_sql(self):
        shop_id = self["shop_id"]
        url = self["url"]
        title = self["title"]
        brand = self["brand"]
        brand_url = self["brand_url"]
        price = self["price"]
        comment_num = self["comment_num"]
        good_comment_rate = self["good_comment_rate"]
        good_comment = self["good_comment"]
        general_count = self["general_count"]
        poor_count = self["poor_count"]
        hot_comment_dict = self["hot_comment_dict"]
        default_comment_num = self["default_comment_num"]
        comment_id = self["comment_id"]
        comment_context = self["comment_context"]
        comnent_time = self["comnent_time"]
        comment_score = self["comment_score"]
        comment_source = self["comment_source"]
        produce_size = self["produce_size"]
        produce_color = self["produce_color"]
        user_level = self["user_level"]
        user_exp = self["user_exp"]
        comment_thumpup = self["comment_thumpup"]
        comment_reply_content = self["comment_reply_content"]
        comment_reply_time = self["comment_reply_time"]
        append_comment = self["append_comment"]
        append_comment_time = self["append_comment_time"]

        insert_sql = """
                       insert into JDAll(shop_id,url,title,brand,brand_url,price,comment_num,good_comment_rate,good_comment,general_count,poor_count,hot_comment_dict,default_comment_num,comment_id,comment_context,comnent_time,comment_score,comment_source,produce_size,produce_color,user_level,user_exp,comment_thumpup,comment_reply_content,comment_reply_time,append_comment,append_comment_time)  VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                     """
        params = (
            shop_id, url, title, brand, brand_url, price, comment_num, good_comment_rate, good_comment, general_count,
            poor_count, hot_comment_dict, default_comment_num, comment_id, comment_context, comnent_time, comment_score,
            comment_source, produce_size, produce_color, user_level, user_exp, comment_thumpup, comment_reply_content,
            comment_reply_time, append_comment, append_comment_time)
        print("return SQL 语句")
        return insert_sql, params

