# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 10:39:40 2021

@author: wonseok
"""

import pymysql

config = {
    'host': '127.0.0.1',
    'user': 'scott',
    'password': 'tiger',
    'database': 'work',
    'port': 3307,
    'charset': 'utf8',
    'use_unicode': True}

try:
    # db 연동 객체
    conn = pymysql.connect(**config)
    # sql문 실행 객체
    cursor = conn.cursor()
    sql = "select * from goods"
    cursor.execute(sql)
    dataset = cursor.fetchall()
    for row in dataset:
        print(row)

except Exception as e:
    print('db error :', e)
    conn.rollback()

finally:
    cursor.close()
    conn.close()
