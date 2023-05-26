#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2023/5/5 19:28
# @Author  : Smalltown
# @FileName: shorpingcart.py
# @Software: PyCharm
import pymssql

conn=pymssql.connect(host="LAPTOP-D2INVD39",database='test_shop',user='sa',password='123')
str = "连接失败！"
if conn:
    str='连接成功！'
    # db.close() # 关闭连接，释放内存
print(str) # 如果结果为连接成功即表示已经成功连接。
# host 为服务器名称
# database 表示你需要连接的数据库
# user及password 表示你SQL Server身份验证的登录名和密码
cursor = conn.cursor()

'''
                        创建表
'''
def CreateUser():
    cursor.execute("drop table if exists Yonghu ")  # 先判断是否存在这个表，如果存在删除
    sql = """
    create table Yonghu(
        User_id varchar(10) primary key,
        User_password varchar(10) not null ,
        User_sex CHAR(1) not null ,
        User_name varchar(10) not null,
        User_phone varchar(15) not null ,
        User_add varchar(50) not null )

    """
    # try:
    cursor.execute(sql)
    print("建表成功")
    # except:
    #     print("建表失败")
    # finally:
    #     conn.close()
    conn.commit()
    # cursor.close()
    # conn.close()


def CreateAdmin():
    cursor.execute("drop table if exists Guanliyuan ")  # 先判断是否存在这个表，如果存在删除
    sql = """
    create table Guanliyuan(
        Admin_id varchar(10) primary key,
        Admin_password varchar(10) not null,
        Admin_sex CHAR(1) not null,
        Admin_name varchar(10) not null)
       
    """
    # try:
    cursor.execute(sql)
    print("建表成功")
    # except:
    #     print("建表失败")
    # finally:
    #     conn.close()
    conn.commit()
    # cursor.close()
    # conn.close()

def CreateFlower():
    cursor.execute("drop table if exists Flower ")  # 先判断是否存在这个表，如果存在删除
    sql = """
    create table Flower(
        Flower_id varchar(10) primary key,
        Flower_name varchar(10) not null,
        Flower_mean varchar(25),
        Flower_importprice varchar(10),
        Flower_exportprice varchar(10)
        )

    """
    # try:
    cursor.execute(sql)
    print("建表成功")
    # except:
    #     print("建表失败")
    # finally:
    #     conn.close()
    conn.commit()
    # cursor.close()
    # conn.close()

def CreateClassify():
    cursor.execute("drop table if exists Classify ")  # 先判断是否存在这个表，如果存在删除
    sql = """
    create table Classify(
        Classify_id varchar(10) primary key,
        Classify_name varchar(10) not null
         )

    """
    # try:
    cursor.execute(sql)
    print("建表成功")
    # except:
    #     print("建表失败")
    # finally:
    #     conn.close()
    conn.commit()
    # cursor.close()
    # conn.close()

def CreateStorage():
    cursor.execute("drop table if exists Storage ")  # 先判断是否存在这个表，如果存在删除
    sql = """
    create table Storage(
        F_remain_id varchar(10) primary key,
        F_remain_num varchar(20) not null
         )

    """
    # try:
    cursor.execute(sql)
    print("建表成功")
    # except:
    #     print("建表失败")
    # finally:
    #     conn.close()
    conn.commit()
    # cursor.close()
    # conn.close()

def CreateNotice():
    cursor.execute("drop table if exists Notice ")  # 先判断是否存在这个表，如果存在删除
    sql = """
    create table Notice(
        Notice_id varchar(10) primary key,
        Notice_title varchar(20) not null ,
        Notice_content varchar(100) not null ,
        Notice_time DATE not null )

    """
    # try:
    cursor.execute(sql)
    print("建表成功")
    # except:
    #     print("建表失败")
    # finally:
    #     conn.close()
    conn.commit()
    # cursor.close()
    # conn.close()

def Createshoppingcart():
    cursor.execute("drop table if exists Cart ")  # 先判断是否存在这个表，如果存在删除
    sql = """
    create table Cart(
        Cart_id varchar(10) primary key,
        User_id varchar(10) not null ,
        totalPrice varchar(10),
        Flower_id varchar(10),
        Flower_name varchar(10),
        Flower_num int default 0    
         )

    """
    # try:
    cursor.execute(sql)
    print("建表成功")
    # except:
    #     print("建表失败")
    # finally:
    #     conn.close()
    conn.commit()
    # cursor.close()
    # conn.close()
# 订单明细
def CreateOrders():
    cursor.execute("drop table if exists Orders ")  # 先判断是否存在这个表，如果存在删除
    sql = """
    create table Orders(
        OrderInfo_id varchar(10) primary key,

        User_Id int NULL DEFAULT NULL ,
        Order_status int NOT NULL ,
        createTime datetime NOT NULL ,
        postage decimal(11, 0) NOT NULL ,
        updateTime datetime NOT NULL ,
        sendTime datetime NULL DEFAULT NULL,
        payment decimal(10, 0) NULL DEFAULT NULL ,
        orderType int NOT NULL ,
        address varchar(255) NOT NULL  )

    """
    # try:
    cursor.execute(sql)
    print("建order表成功")
    # except:
    #     print("建表失败")
    # finally:
    #     conn.close()
    conn.commit()
    # cursor.close()
    # conn.close()

#     订单索引
def CreateOrderInfo():
    cursor.execute("drop table if exists OrderInfo ")  # 先判断是否存在这个表，如果存在删除
    sql = """
   CREATE TABLE OrderInfo  (
  OrderInfo_Id int NOT NULL,
  Flower_Id int NOT NULL,
  Order_Id int NOT NULL ,
  Flower_num int NULL DEFAULT NULL,
  totalPrice decimal(10, 2) NULL DEFAULT NULL,
  PRIMARY KEY (OrderInfo_Id) 
) 
    """
    # try:
    cursor.execute(sql)
    print("建order表成功")
    # except:
    #     print("建表失败")
    # finally:
    #     conn.close()
    conn.commit()
    # cursor.close()
    # conn.close()

def CreateBBs_artical():
    cursor.execute("drop table if exists BBs_artical ")  # 先判断是否存在这个表，如果存在删除
    sql = """
   CREATE TABLE BBs_artical  (
   artical_Id varchar(10) primary key,
  User_Id varchar(10) not null ,
  User_name varchar(10) not null ,
  
  artical_title varchar (20),
  artical_content varchar(8000)
  
  
) 
    """
    # try:
    cursor.execute(sql)
    print("建order表成功")
    # except:
    #     print("建表失败")
    # finally:
    #     conn.close()
    conn.commit()
    cursor.close()
    conn.close()