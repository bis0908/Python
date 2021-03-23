# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 22:26:27 2021

@author: wonseok
"""
import csv
import re
# import urllib.request
from bs4 import BeautifulSoup
import pandas as pd
# import os
import requests


# path: 다운 받은 경로를 지정한다.
code_path = 'E:/Code/Python/itwill/project/dataset/Market analysis/Actual_Transaction_Code/'
# 공공데이타터 포털에서 신청한 개인 Open API 값이 담긴 txt 파일 경로 지정(사용자가 직접 txt 파일을 만듭니다)
key_path = 'E:/Code/Python/itwill/project/'

def code_finder(gu_name):
    with open(code_path + 'region_code5_seoul.csv', encoding = 'euc-kr', mode = 'r') as region_code:
        code = csv.reader(region_code)
        next(code)
        try:
            for line in code:
                dong, lawd_cd = line
                if  gu_name == ''.join(re.findall(gu_name, dong)):
                    return lawd_cd

        except Exception as e:
            print('예외발생 : ', e)
        finally :
            region_code.close()

# column 선언
amount = []
area = []
building_mainPurpose = []
const_year = []
year = []
landArea = []
dong = []
gu = []
purArea = []
month = []
type_ = []
day = []
regCode = []
ocDate = []
relStat = []
global rest_info_for_cmcl_use
rest_info_for_cmcl_use = {}
global url


def get_last_page(url):
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "xml")
    last_page = soup.find('totalCount').string
    # return int(last_page)
    # last_page = 2
    return int(last_page)


def extract_info(xml):
    n_amount = xml.find_all("거래금액")
    for a in n_amount:
        amount.append(a.text)

    n_area = xml.find_all("건물면적")
    for b in n_area:
        area.append(b.text)

    n_building_mainPurpose = xml.find_all("건물주용도")
    for c in n_building_mainPurpose:
        building_mainPurpose.append(c.text)

    n_const_year = xml.find_all("건축년도")
    for d in n_const_year:
        const_year.append(d.text)

    n_year = xml.find_all("년")
    for e in n_year:
        year.append(e.text)

    n_landArea = xml.find_all("대지면적")
    for f in n_landArea:
        landArea.append(f.text)

    n_dong = xml.find_all("법정동")
    for g in n_dong:
        dong.append(g.text)

    n_gu = xml.find_all("시군구")
    for h in n_gu:
        gu.append(h.text)

    n_purArea = xml.find_all("용도지역")
    for i in n_purArea:
        purArea.append(i.text)

    n_month = xml.find_all("월")
    for j in n_month:
        month.append(j.text)

    n_type = xml.find_all("유형")
    for k in n_type:
        type_.append(k.text)

    n_day = xml.find_all("일")
    for l in n_day:
        day.append(l.text)

    n_regCode = xml.find_all("지역코드")
    for m in n_regCode:
        regCode.append(m.text)

    n_ocDate = xml.find_all("해제사유발생일")
    for n in n_ocDate:
        ocDate.append(n.text)

    n_relStat = xml.find_all("해제여부")
    for o in n_relStat:
        relStat.append(o.text)

    dataset = {'거래금액': amount,
            '건물면적': area,
            '건축주용도': building_mainPurpose,
            '건축년도': const_year,
            '년': year,
            '대지면적': landArea,
            '법정동': dong,
            '시군구': gu,
            '용도지역': purArea,
            '월': month,
            '유형': type_,
            '일': day,
            '지역코드': regCode,
             '해제사유발생일': ocDate,
             '해제여부': relStat
            }

    return dataset

def dataFrame_maker(dataset):
    global rest_info_for_cmcl_use
    rest_info_for_cmcl_use['거래금액'] = amount
    rest_info_for_cmcl_use['건물면적'] = area
    rest_info_for_cmcl_use['건축주용도'] = building_mainPurpose
    rest_info_for_cmcl_use['건축년도'] = const_year
    rest_info_for_cmcl_use['년'] = year
    rest_info_for_cmcl_use['대지면적'] = landArea
    rest_info_for_cmcl_use['법정동'] = dong
    rest_info_for_cmcl_use['시군구'] = gu
    rest_info_for_cmcl_use['용도지역'] = purArea
    rest_info_for_cmcl_use['월'] = month
    rest_info_for_cmcl_use['유형'] = type_
    rest_info_for_cmcl_use['일'] = day
    rest_info_for_cmcl_use['지역코드'] = regCode
    rest_info_for_cmcl_use['해제사유발생일'] = ocDate
    rest_info_for_cmcl_use['해제여부'] = relStat
    df = pd.DataFrame(rest_info_for_cmcl_use)
    df = df[['거래금액', '건물면적', '건축주용도', '건축년도', '년', '대지면적', '법정동', '시군구', '용도지역', '월', '유형', '일', '지역코드', '해제사유발생일', '해제여부']]
    return df

def extract_infos(last_page, url):
    global rest_info_for_cmcl_use
    for page in range(last_page):
        print(f'Open API: 국토부 상업업무용 부동산 매매 신고 자료 수집 중... page: {page+1}/', last_page)
        result = requests.get(f'{url}&pageNo={page+1}')
        soup = BeautifulSoup(result.text, 'xml')
        for result in soup:
            data = extract_info(result)
            data = dataFrame_maker(data)

    return data

def get_data(gu_name, ymd): #사용자가 입력한 word + url을 만든다.
    lawd_cd = code_finder(gu_name)
    serviceKey  = open(key_path + 'serviceKey(datagokr).txt', mode = 'r')
    serviceKey = serviceKey.read()
    url = f'http://openapi.molit.go.kr/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcNrgTrade?LAWD_CD={lawd_cd}&DEAL_YMD={ymd}&serviceKey={serviceKey}'
    last_page = get_last_page(url) #그 url의 마지막 페이지를 구한다.
    infos = extract_infos(last_page, url) #이를 통해 데이터를 추출한다.
    return infos


gu_name = str(input('검색할 구 입력: '))
ymd = int(input('검색할 기간 입력(ex. 202103): '))

datasets = get_data(gu_name, ymd)
datasets.to_csv('국토교통부_상업업무용 부동산 매매 신고정보({}).csv'.format(gu_name), encoding = 'utf-8-sig', index = False)
