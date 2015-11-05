#encoding:utf-8

from db import DB
__author__ = 'xt'

db = DB()
datas = db.get_media_info()
source_id = {}
for data in datas:
    source_id[str(data[0])] = int(data[1])

