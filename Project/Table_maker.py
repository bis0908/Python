# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 10:43:06 2021

@author: wonseok
"""
from service_rec import similarity # 사용자 함수
import pandas as pd

# 그래프 그리기
import matplotlib.pyplot as plt
import seaborn as sb

# 이미지 저장을 위한 모듈
import os
import time


def table_info(word):
    # index.html에서 입력받은 도로명을 기반으로 similarity 함수를 통해 업종 매출, 밀집도 상위 데이터를 dict로 반환
    sales_dict, den_dict = similarity(word)

    # 기본 경로를 절대 경로로 지정
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    #  그래프 그리기
    plt.rcParams['font.family'] = 'Malgun Gothic'
    sales_rank = pd.DataFrame(sales_dict.items(), columns = ['업종명', '당월매출금액'])
    colors = sb.color_palette('hls', len(sales_rank['업종명']))
    sales_rank.plot(kind = 'bar', x = '업종명', y = '당월매출금액', color = colors, edgecolor='black', legend = False)
    plt.title('업종별 평균 매출 Top 5')
    plt.xticks(rotation = 0) # x 축에 표시되는 업종명이 세로로 90도 틀어져 표시되어 0도로 재조정

# =============================================================================
#     기존에 저장된 이미지가 있을 경우, 웹에서 old 이미지를 로드하는 문제 때문에
#     파일명에 시간을 추가하여 중복을 제거
# =============================================================================
    sales_img = "sales_rank_" + str(time.time()) + ".png"
    for filename in os.listdir('static/images'):
        if filename.startswith('sales_rank_'):  # not to remove other images
            os.remove('static/images/' + filename)

    plt.savefig(BASE_DIR + '/WebPage/static/images/' + sales_img)


    density_rank = pd.DataFrame(den_dict.items(), columns = ['업종명', '당월매출금액'])
    density_rank.plot(kind = 'bar', x = '업종명', y = '당월매출금액', color = colors, edgecolor='black', legend = False)
    plt.title('밀집도별 평균 매출 Top 5')
    plt.xticks(rotation = 0)

    density_img = "density_rank_" + str(time.time()) + ".png"
    for filename in os.listdir('static/images'):
        if filename.startswith('density_rank_'):  # not to remove other images
            os.remove('static/images/' + filename)

    plt.savefig(BASE_DIR + '/WebPage/static/images/' + density_img)


    trans_sales = {}
    trans_den = {}
    for key, val in sales_dict.items():
        val = format(val, ',')
        # c = dict(key, val)
        trans_sales[key] = val

    for key, val in den_dict.items():
        val = format(val, ',')
        # c = dict(key, val)
        trans_den[key] = val

    # 이미지 2장, dict 2개를 최종 반환 합니다.
    return sales_img, density_img, trans_sales, trans_den