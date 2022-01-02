# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 11:28:23 2021

@author: wonseok
"""

from flask import Flask, render_template, request, redirect
from Table_maker import table_Info # User_Function


app = Flask(__name__) # Flask 생성자 -> application 생성

@app.route('/') # 시작 페이지 url 호출 (http://127.0.0.1:5000/)
def index():
    return render_template('index.html') # home의 html 파일

@app.route('/report')
def report():
    word = request.args.get('word')

    if word:
        sales_img, density_img, trans_sales, trans_den = table_Info(word)
    else:
        return redirect('/') # word를 입력하지 않으면 리다이렉트 (home으로)

    return render_template('report.html',
                           word = str(word),
                           sales_dict = trans_sales,
                           den_dict = trans_den,
                           graph1 = sales_img,
                           graph2 = density_img)

# 프로그램 시작점
if __name__ == '__main__':
    app.run(debug = True) # 애플리케이션 실행