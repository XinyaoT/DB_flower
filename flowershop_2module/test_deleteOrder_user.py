#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2023/5/19 23:17
# @Author  : Smalltown
# @FileName: test_deleteOrder_user.py
# @Software: PyCharm

import pymssql
import pyodbc

import flowershop_2module.shopping.shoppingcart_func as shoppingFun
import flowershop_2module.shopping.shoppingcart_utils as shopping
import shortuuid
import flowershop_2module.order.order_utils as order
import flowershop_2module.order.order_func as orderFun
# ###############################连接###########################################
#
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

# 用户删除的是订单详情，而不是单一的订单



orderInfo_ids = []

num = 0 # 前端传入
while True:
    orderInfo_id = input("请选择好哪些订单详情信息是你想取消的（前端返回给我用户选择的的订单详情编号）：")
    num = num+1
    if orderInfo_id == 'q':
        break
    orderInfo_ids.append(orderInfo_id)
print(orderInfo_ids)
orderInfo = tuple(orderInfo_ids)
print(orderInfo)

client_id = input("前端请告诉我你的用户id：")

# 取消订单申请
orderFun.deleteOrderInfo_user(conn, cursor, orderInfo, num)

#     order_id = order.getOrderInfo_orderId(cursor=cursor, orderInfo_id=orderInfo[i])
#
#
#     flag = order.getIsOrderInfo_orderInfoId(cursor=cursor, order_id=order_id)
#
#     print(flag)
#     if flag ==1 :
#         print("你删除的是最后一条该",i,"订单的数据\n")
#
#         order.deleteOrderInfo(cursor=cursor, conn=conn, data=orderInfo[i])
#         order.deleteOrder(cursor=cursor, conn=conn, data=order_id)
#
#     else:
#         order.deleteOrderInfo(cursor=cursor, conn=conn, data=orderInfo[i])
#
# print("删除成功")