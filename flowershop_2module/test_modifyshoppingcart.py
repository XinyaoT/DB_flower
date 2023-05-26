#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2023/5/12 0:32
# @Author  : Smalltown
# @FileName: test_modifyshoppingcart.py
# @Software: PyCharm


import pymssql
import flowershop_2module.shopping.shoppingcart_func as shoppingFun
import flowershop_2module.shopping.shoppingcart_utils as shopping
import shortuuid

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

'''此模块描述当用户进入购物车的页面对于购物车的每一条信息进行  ++/--/删除'''
print("你现在进入*我的购物车*当中了，你可以选择对自己购物车中的每一条记录进行++或--或者删除")

lang = input("如果输入+，表示你想增加你选中的商品（你选中哪些是前端告诉我的）\n如果输入-，表示你想删减选中的商品（你选中哪些也是前端告诉我的）\n"
             "如果输入*删除*，那么你选中的这条记录会被删除\n:")

match lang:
    case "+":
        print("你可以开始增加商品选购数量了！\n")
        flower_name = input("请告诉我你选择的商品名字：")
        add_num = input("请告诉我，你增加后的数量：")  #这里的限制操作前端来做,,
        cart_wholeMoney = input("前端告诉我最后你提交的总价为：")
        cart_id = input("前端告诉我你这条信息的cart_id为：")
        dertaAdd = shoppingFun.fun_modifyAddShoppingcart(cursor=cursor,conn=conn, flower_name=flower_name, add_num=add_num, cart_wholeMoney=cart_wholeMoney, cart_id=cart_id)
        print("你现在已经成功添加了", dertaAdd, "个商品拉")

    case "-":

        print("你可以开始减少商品选购数量了！\n")
        flower_name = input("请告诉我你选择的商品名字：")
        dec_num = input("请告诉我，你减少后的数量：")  # 这里的限制操作前端来做,,
        if dec_num ==1:
            print("已经不能再减少了哟！\n")
        else:
            cart_wholeMoney = input("前端告诉我最后你提交的总价为：")
            cart_id = input("前端告诉我你这条信息的cart_id为：")
            dertaDec = shoppingFun.fun_modifyDecShoppingcart(cursor=cursor,conn=conn, flower_name=flower_name, dec_num=dec_num, cart_wholeMoney=cart_wholeMoney, cart_id=cart_id)
            print("你现在已经成功减少了", dertaDec, "个商品拉")

    case "删除":

        print("你可以开始删除购物车信息拉！\n")
        flower_name = input("请告诉我你选择的商品名字：")
        cart_id = input("前端告诉我你这条信息的cart_id为：")
        shoppingFun.fun_modifyDeleShoppingcart(cursor=cursor, conn=conn, cart_id=cart_id,flower_name=flower_name)
        print("你删除了编号为",cart_id,"的购物信息")

