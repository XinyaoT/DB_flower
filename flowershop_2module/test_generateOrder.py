#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2023/5/13 1:26
# @Author  : Smalltown
# @FileName: test_generateOrder.py
# @Software: PyCharm


import pymssql
import pyodbc as pyodbc

import flowershop_2module.shopping.shoppingcart_func as shoppingFun
import flowershop_2module.shopping.shoppingcart_utils as shopping
import shortuuid
import flowershop_2module.order.order_utils as order
import flowershop_2module.order.order_func as orderFun
# ###############################连接###########################################
# conn=pyodbc.connect(host="LAPTOP-D2INVD39",database='flower_shop_5',user='sa',password='123',charset="cp936")
conn = pyodbc.connect('DRIVER={SQL Server};SERVER=LAPTOP-D2INVD39;DATABASE=flower_shop_5;UID=sa;PWD=123')
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

# 获取用户的购物车id信息
print("好了，你现在可以选择让购物车生成订单了\n")
cart_ids = []
orderInfo_uuid = []

num = 0 # 前端传入
while True:
    cart_id = input("请选择好哪些购物车信息是你决定要生成的订单（前端返回给我用户选择的的购物车编号）：")
    num = num+1
    if cart_id == 'q':
        break
    cart_ids.append(cart_id)
print(cart_ids)
cart_info = tuple(cart_ids)
print(cart_info)

'''一条购物车信息生成一条订单详情，同一时间生成的这些订单详情生成一条购物车信息'''

# 可利用ajax请求获取时间戳存入当前数据库，假设已经获取成功
client_id = input("前端告诉我你的用户id为：")
order_time = input("前端告诉我你生成该订单的时间是：")
order_price = input("前端向我传输你所选择的购物车的总价为：")
order_addr = input("获取地址表的信息：")
# 是否选择合订成束
order_bunched = input("时候合订成束（1/0）")

# 生成1条订单信息
order_uuid = orderFun.addOrder_user(cursor,conn, client_id, order_price, order_time)

#         针对地址的设置：
# flag = input("请问你是否选择使用默认地址？（1表示使用默认，0表示选择其他地址信息）：")
# if(flag == 1):

# 在has_c_a中拿到address_id

# 通过addressid检索这一行是否是default
# 如果是，取出地址信息







# 同时生成多条订单详情信息，一条购物车详情对应一个，上面总共统计出有num个

orderFun.addOrderInfo_user(cursor, conn, orderInfo_uuid,order_addr,order_bunched, cart_info, order_uuid, order_time,client_id,num)

# 通过上述选择的购物车详情生成对应的订单详情信息



