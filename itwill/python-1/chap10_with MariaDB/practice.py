# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 20:13:31 2021

@author: wonseok
"""
import os
import csv
import pymysql

config = {
    'host': '127.0.0.1',
    'user': 'scott',
    'password': 'tiger',
    'database': 'work',
    'port': 3307,
    'charset': 'utf8',
    'use_unicode': True}

os.chdir('E:\Code\Python\itwill\chap10_with MariaDB\data')
cnt = 1

try:
    conn = pymysql.connect(**config)
    cursor = conn.cursor()

    # 1. table 생성

    sql = '''
        create table shopping(
            collect_day char(10) not null,
            good_id int not null,
            pum_id char(7) not null,
            pum_name char(10) not null,
            good_name varchar(400) not null,
            sales_price int not null,
            discount_price int not null,
            benifit int not null
            ) '''

    cursor.execute(sql) # 쿼리문 날리기
    print('1. shopping table 생성 완료')

    with open('2021-01-01.csv', 'r', encoding='euc-kr') as file:
        file_data = csv.reader(file, delimiter=',')
        next(file_data)
        for row in file_data:
            print('데이터 적재중...', cnt)
            collect_day = row[0]
            good_id = row[1]
            pum_id = row[2]
            pum_name = row[3]
            good_name = row[4]
            sales_price = row[5]
            discount_price = row[6]
            benifit = row[7]
            sql = f'''insert into shopping values(
                        '{collect_day}', '{good_id}', '{pum_id}', '{pum_name}',
                        '{good_name}', '{sales_price}', '{discount_price}', '{benifit}' ) '''
            cursor.execute(sql)
            conn.commit()
            cnt += 1

    file.close()
    print('Record 추가 성공!')


except Exception as e:
    print('db error :', e)
    conn.rollback()

finally:
    cursor.close()
    conn.close()
