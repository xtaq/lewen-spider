#encoding:utf-8

import MySQLdb
import logging

__author__ = 'xt'


class DB:

    def __init__(self):
        self.conn = MySQLdb.connect(host='localhost',
                                    port=3306,
                                    user="root",
                                    passwd="",
                                    db="test",
                                    charset="utf8")
        self.log = logging.getLogger(__name__)

    def __del__(self):
        self.conn.close()

    #获取操作游标
    # def cursor(self):
    #     try:
    #         return self.conn.cursor()
    #     except (AttributeError, MySQLdb.OperationalError):
    #         self.connect()
    #         return self.conn.cursor()

    # def commit(self):
    #     return self.conn.commit()

    '''
    获取爬取媒体名字和ID对应信息
    '''
    def get_media_info(self):
        sql = 'select media_name, media_id from media_info'
        cur = self.conn.cursor()
        cur.execute(sql)
        return cur.fetchall()

    def delete_article(self, sql, name):
        cur = self.conn.cursor()
        try:
            cur.execute(sql)
            self.conn.commit()
        except MySQLdb.Error, e:
            self.log.error("Spider %s Delete Error %d: %s" % (name, e.args[0], e.args[1]))
            self.conn.rollback()

    def insert_article(self, item, name):
        cur = self.conn.cursor()
        try:
            cur.execute("""INSERT INTO article_info (source, title, article_url,
                            create_time, update_time, content, author)
                            VALUES (%s, %s, %s, %s, %s, %s, %s)""",
                            (item['source'],
                             item['title'],
                             item['article_url'],
                             item['create_time'],
                             item['update_time'],
                             item['content'],
                             item['author']))
            self.conn.commit()
        except MySQLdb.Error, e:
            self.log.error("Spider %s Insert Error %d: %s" % (name, e.args[0], e.args[1]))


if __name__ == '__main__':
    db = DB()
