#!/usr/bin/python3

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",  # 数据库主机地址
    user="drivema",  # 数据库用户名
    passwd="RRSjFoexoV5pHrBv"  # 数据库密码
#    user="root",  # 数据库用户名
#    passwd=""  # 数据库密码
)

print(mydb)

mycursor = mydb.cursor()

#mycursor.execute("CREATE DATABASE mydatabase")

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)