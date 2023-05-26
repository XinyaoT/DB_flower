#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2023/5/15 19:23
# @Author  : Smalltown
# @FileName: order_func.py
# @Software: PyCharm


import flowershop_2module.shopping.shoppingcart_func as shoppingFun
import flowershop_2module.shopping.shoppingcart_utils as shopping
import shortuuid
import flowershop_2module.order.order_utils as order

def adminDeleteTheOrder():
 print("pass")

def deleteOrderInfo_user(conn, cursor, orderInfo, num):
    for i in range(0, num - 1):
       order.updateOderInfoStatus(conn=conn, cursor=cursor, orderInfo_id=orderInfo[i])

    print("取消订单的信息已同步给管理员")


def addOrder_user(cursor, conn, client_id, order_price, order_time):
   order_uuid = "or" + shortuuid.ShortUUID(alphabet='0123456789').random(length=6)
   print(order_uuid)
   data1 = (order_uuid, client_id, order_price, order_time)
   order.addOrder(conn=conn, cursor=cursor, data=data1)
   return order_uuid


def addOrderInfo_user(cursor, conn, orderInfo_uuid,order_addr,order_bunched, cart_info, order_uuid, order_time,client_id,num):
   for i in range(0, num - 1):
      orderInfo_uuid.append("oi" + shortuuid.ShortUUID(alphabet='0123456789').random(length=6))
      print(orderInfo_uuid)
      orderInfo_flower_id = order.getOrderInfo_flower_id(cursor=cursor, cart_id=cart_info[i])
      orderInfo_flower_name = order.getOrderInfo_flower_name(cursor=cursor, flower_id=orderInfo_flower_id)
      print(orderInfo_flower_name)
      orderInfo_flowerNum = int(order.getOrderInfo_flowerNum(cursor=cursor, cart_id=cart_info[i]))
      orderInfo_whole_money = order.getOrderInfo_wholeMoney(cursor=cursor, cart_id=cart_info[i])
      orderInfo_addr = order_addr
      orderInfo_bunched = order_bunched
      orderInfo_clientId = client_id

      data = (orderInfo_uuid[i], cart_info[i], order_uuid, order_time, orderInfo_flower_id, orderInfo_flower_name,
              orderInfo_flowerNum, orderInfo_whole_money, orderInfo_addr, orderInfo_bunched, orderInfo_clientId)
      print(data)
      order.addOrderInfo(conn=conn, cursor=cursor, data=data)
