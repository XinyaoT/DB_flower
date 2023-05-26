#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2023/5/11 23:47
# @Author  : Smalltown
# @FileName: test.py
# @Software: PyCharm
import uuid

# cart_id = str(uuid.uuid4())
# print(cart_id)

import shortuuid

# custom_uuid ="c"+ shortuuid.ShortUUID(alphabet='0123456789').random(length=7)
# print(custom_uuid)


import pymssql
import flowershop_2module.shopping.shoppingcart_func as shoppingFun
import flowershop_2module.shopping.shoppingcart_utils as shopping
import shortuuid
import flowershop_2module.order.order_utils as order
# ###############################连接###########################################
conn=pymssql.connect(host="LAPTOP-D2INVD39",database='flower_shop_3',user='sa',password='123',charset='cp936')
str = "连接失败！"
if conn:
    str='连接成功！'
    # db.close() # 关闭连接，释放内存
print(str) # 如果结果为连接成功即表示已经成功连接。
# host 为服务器名称
# database 表示你需要连接的数据库
# user及password 表示你SQL Server身份验证的登录名和密码
cursor = conn.cursor()
# ###############################连接###########################################
flower_id='f0001'
sql = "SELECT flower_name FROM flower where flower_id= %s "
cursor.execute(sql, flower_id)
flower=cursor.fetchone()[0]
print(flower)
print(len(['or144158']))
