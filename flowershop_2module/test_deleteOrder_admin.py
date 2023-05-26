#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2023/5/20 0:36
# @Author  : Smalltown
# @FileName: test_deleteOrder_admin.py
# @Software: PyCharm
import pymssql
import flowershop_2module.shopping.shoppingcart_func as shoppingFun
import flowershop_2module.shopping.shoppingcart_utils as shopping
import shortuuid
import flowershop_2module.order.order_utils as order
# ###############################连接###########################################
conn=pymssql.connect(host="LAPTOP-D2INVD39",database='flower_shop_5',user='sa',password='123',charset='cp936')
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

 # order_id = order.getOrderInfo_orderId(cursor=cursor, orderInfo_id=orderInfo[i])


    # flag = order.getIsOrderInfo_orderInfoId(cursor=cursor, order_id=order_id)

    # print(flag)
    # if flag ==1 :
    #     print("你删除的是最后一条该",i,"订单的数据\n")
    #
    #     order.deleteOrderInfo(cursor=cursor, conn=conn, data=orderInfo[i])
    #     order.deleteOrder(cursor=cursor, conn=conn, data=order_id)
    #
    # else:
    #     order.deleteOrderInfo(cursor=cursor, conn=conn, data=orderInfo[i])

# print("删除成功")