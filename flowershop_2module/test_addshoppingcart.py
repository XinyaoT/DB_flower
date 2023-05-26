#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2023/5/9 0:04
# @Author  : Smalltown
# @FileName: test_addshoppingchart.py
# @Software: PyCharm


import pymssql

import flowershop_2module.shopping.shoppingcart_utils as shopping
import shortuuid
import flowershop_2module.shopping.shoppingcart_func as shoppingFun
# ###############################连接###########################################
conn=pymssql.connect(host="LAPTOP-D2INVD39",database='flower_shop_5',user='sa',password='123')
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


'''插入一条用户数据'''
# data1 = ("u0001", "123","F", "11111", "jake")
# shopping.addUser(conn=conn, cursor=cursor, data=data1)

'''测试查询语句，并返回结果，返回的是元组，用数组方式取出对应的值'''
# sql = "SELECT User_id FROM Yonghu where User_id='u0001';"
# cursor.execute(sql)
# row = cursor.fetchone()
# print(row[0])


# 进入购物车选购商品模块，加入商品到购物车
while True:
    ################################数据输入##########################################################
    print("现在你已经可以开始选购你喜欢的花朵了！\n")
    flower_name = input("please chose one flower you like(玫瑰，茉莉，满天星):")

    '''前端接收用户传入的购物车数据，插入cart Info的表中,
        用户选择一种花就应该有一个购物车id，
        现在假设用户已经选择好了一种花，加入购物车'''

    user_id = input("Enter value for userid（请给我你的用户编号）: ")
    cart_id = "c"+shortuuid.ShortUUID(alphabet='0123456789').random(length=7)  #自动分配cartID

    '''点击+ 确认，'''
    add_flower_num = input("Enter value for add_flower_num（你需要买多少朵花）: ")  #这条消息应该是前端计算出传给后端的
    wholemoney = input("Enter value for wholemoney（前端告诉我你所购买的这种花的总价为）: ")  #这条消息应该是前端计算出传给后端的
    #########################数据输入##########################################################################################

    '''判断是否能加入购物车'''
    flag = shoppingFun.fun_can_add_or_not(cursor, flower_name, add_flower_num)

    # 不可以加入
    if flag == 1:
        print("库存不足，请重新设置购买数量")
    #可以加入
    else:
    #更新shoppingcart flower表 contain表，对于flower表的sale应该在订单处更新
        shoppingFun.fun_addshoppingcart(cart_id=cart_id, user_id=user_id, flower_name=flower_name, wholemoney=wholemoney, add_flower_num=add_flower_num,cursor=cursor, conn=conn)
        print("现在你已经成功将此花加入你的购物车了！\n")
        break



