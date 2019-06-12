# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
from twisted.enterprise import adbapi

# class JdallPipeline(object):
#     def process_item(self, item, spider):
#         return item


class MysqlTwistedPipline(object):

    def __init__(self, dbpool):
        self.dbpool = dbpool

    @classmethod
    def from_settings(cls, settings):
        dbparms = dict(
            host=settings["MYSQL_HOST"],
            db=settings["MYSQL_DBNAME"],
            user=settings["MYSQL_USER"],
            passwd=settings["MYSQL_PASSWORD"],
            charset='utf8',
            # 指定 curosr 类型 指定字典类型
            cursorclass=pymysql.cursors.DictCursor,
            use_unicode=True,
        )
        # 这就可以让adbapi来使用多个连接
        # 指定操作数据库的模块名和数据库参数
        dbpool = adbapi.ConnectionPool("pymysql", **dbparms)
        return cls(dbpool)

    def process_item(self, item, spider):
        # item 是要传入到self.do_insert的 会从dbpool取出cursor
        # runInteraction可以将传入的函数变成异步的
        query = self.dbpool.runInteraction(self.do_insert, item)
        # 指定异常处理方法
        query.addErrback(self.handle_error, item, spider)
        # 返回item
        return item

    def handle_error(self, failure, item, spider):
        print(failure)

    def do_insert(self, cursor, item):
        # 会从dbpool取出cursor
        print("写入数据库")
        # 执行具体的插入
        insert_sql, params = item.get_insert_sql()
        cursor.execute(insert_sql, params)
