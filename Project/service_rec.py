# -*- coding: utf-8 -*-
"""


"""
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# 상주_유동비율 데이터 로드
data_pop = pd.read_csv("E:/Code/Python/itwill/project/WebPage/merge_set_flo_prop2.csv")
# 매출 데이터 로드
data_sales = pd.read_csv("E:/Code/Python/itwill/project/WebPage/annual_sales_new.csv")
# 상권-업종 별 분기매출 평균
service_sales = pd.read_csv("E:/Code/Python/itwill/project/WebPage/point_service_sales.csv", encoding='utf-8', index_col=False)

def similarity(name):
    # '상권_코드_명'에 대응하는 '상권_코드'로 변경 (name -> code)
    code_table = pd.DataFrame(data_sales['상권_코드'].unique(),
                              index=data_sales['상권_코드_명'].unique(),
                              columns=['상권코드'])
    code = int(code_table.loc[name])

    # 1-1. 상주인구비율, 유동인구비율을 고려하여 선택한 상권과 비슷한 상권 50개 찾기
    # pivot table 작성
    data_pv = pd.pivot_table(data_pop,
                             index='상권_코드',
                             columns='class',
                             values='val')

    data_sim = cosine_similarity(data_pv)

    # 유사도 데이터프레임 변환
    data_sim2 = pd.DataFrame(data=data_sim, index=data_pv.index,
                             columns=data_pv.index)

    rec = data_sim2[code].sort_values(ascending=False)[:51]

    list_of_index = [item for item in data_pv.loc[rec.index].index]

    # 1-2. 1-1에서 찾은 50개 상권 중 업종별 매출액을 고려하여 선택한 상권과 비슷한 상권 5개 찾기
    # top50  list -> df
    list_df = pd.DataFrame(list_of_index, columns=['상권_코드'])

    # top50 df 와 매출 데이터 조인
    df_merge = pd.merge(data_sales, list_df, on='상권_코드')

    # 조인df -> 피벗테이블
    merge_pv = pd.pivot_table(df_merge,
                              index='상권_코드',
                              columns='서비스_업종_코드_명',
                              values='분기별매출평균')

    # 상권별 유사도
    merge_pv.fillna(0, inplace=True)  # Nan 값 0 처리

    data_sim = cosine_similarity(merge_pv)

    data_sim = pd.DataFrame(data=data_sim, index=merge_pv.index, columns=merge_pv.index)

    # 추천 함수
    recomm_top = data_sim[code].sort_values(ascending=False)[1:6]

    # 매출 데이터와 top 5 df 조인
    df_merge = pd.merge(data_sales, recomm_top, on='상권_코드')

    # 조인df -> 피벗테이블
    data_pv = pd.pivot_table(df_merge,
                             index='상권_코드',
                             columns='서비스_업종_코드_명',
                             values='분기별매출평균')

    data_pv.fillna(0, inplace=True)  # NaN 값 0 처리

    # 점수 기록을 위한 score DataFrame 생성
    score = pd.DataFrame(data_sales.서비스_업종_코드_명.unique(), columns=['서비스_업종_코드_명'])
    data_pv2 = pd.pivot_table(df_merge,
                              index='서비스_업종_코드_명',
                              values='분기별매출평균')
    # top5 상권의 업종별 매출액 순위에 따라 22점 만점의 점수를 부여
    # ex) 1등(22점), 2등(21점), 3등(20점), ...
    for i in [0, 1, 2, 3, 4]:
        # 매출액 순위에 따라 내림차순으로 정렬 후 매출액이 0보다 큰 업종에 차례대로 점수 부여
        data_sort = data_pv.iloc[i].sort_values(ascending=False)[data_pv.iloc[i] > 0]
        list_of_index = [item for item in data_pv2.loc[data_sort.index].index]
        list_df = pd.DataFrame(list_of_index, columns=['서비스_업종_코드_명'])
        score_series = pd.Series(
            range(22, 22 - len(data_pv.iloc[i].sort_values(ascending=False)[data_pv.iloc[i] > 0]), -1))
        score_df = pd.DataFrame(score_series)
        if i == 0:
            list_df['score1'] = score_df
            score = pd.merge(score, list_df, 'outer')
        elif i == 1:
            list_df['score2'] = score_df
            score = pd.merge(score, list_df, 'outer')
        elif i == 2:
            list_df['score3'] = score_df
            score = pd.merge(score, list_df, 'outer')
        elif i == 3:
            list_df['score4'] = score_df
            score = pd.merge(score, list_df, 'outer')
        else:
            list_df['score5'] = score_df
            score = pd.merge(score, list_df, 'outer')

    score.fillna(0, inplace=True)  # score 의 NaN은 0으로 대체

    # 각 상권의 업종별 점수를 합산하여 합산점수 상위 5개 업종을 선택
    score_sum = score['score1'] + score['score2'] + score['score3'] + score['score4'] + score['score5']
    score['score_sum'] = score_sum
    score.index = score.서비스_업종_코드_명
    score_sum_sort = score.score_sum.sort_values(ascending=False)[0:5]
    rec_sales = [item for item in data_pv2.loc[score_sum_sort.index].index]

    # 2. 업종별 밀집도를 비교하여 밀집도가 낮은 업종 추천
    # 피벗테이블 생성
    data_pv = pd.pivot_table(df_merge,
                             index='상권_코드',
                             columns='서비스_업종_코드_명',
                             values='점포수')
    data_pv2 = pd.pivot_table(df_merge,
                              index='서비스_업종_코드_명',
                              values='점포수')

    data_pv.fillna(0, inplace=True)  # NaN은 0으로 처리

    # 업종별 밀집도 점수 DataFrame 생성
    score_den = pd.DataFrame(data_sales.서비스_업종_코드_명.unique(), columns=['서비스_업종_코드_명'])

    # 5개 상권의 업종별 밀집도 계산(밀집도 = 해당 업종의 점포수 / 해당 상권 전체의 점포수)
    for i in [0, 1, 2, 3, 4]:
        score_den_reg = data_pv.iloc[i] / sum(data_pv.iloc[i])
        list_of_index = [item for item in data_pv2.loc[score_den_reg.index].index]
        list_df = pd.DataFrame(list_of_index, columns=['서비스_업종_코드_명'])
        if i == 0:
            list_df['den1'] = score_den_reg.values
            score_den = pd.merge(score_den, list_df, 'outer')
        elif i == 1:
            list_df['den2'] = score_den_reg.values
            score_den = pd.merge(score_den, list_df, 'outer')
        elif i == 2:
            list_df['den3'] = score_den_reg.values
            score_den = pd.merge(score_den, list_df, 'outer')
        elif i == 3:
            list_df['den4'] = score_den_reg.values
            score_den = pd.merge(score_den, list_df, 'outer')
        else:
            list_df['den5'] = score_den_reg.values
            score_den = pd.merge(score_den, list_df, 'outer')

    # 5개 상권의 업종별 밀집도 평균 계산
    score_den_mean = (score_den['den1'] + score_den['den2'] + score_den['den3']
                      + score_den['den4'] + score_den['den5']) / 5
    score_den['den_mean'] = score_den_mean.values
    score_den.index = score_den.서비스_업종_코드_명

    # 선택한 상권의 현재 업종별 밀집도 계산
    pv_store = pd.pivot_table(data_sales,
                              index='서비스_업종_코드_명',
                              columns='상권_코드',
                              values='점포수')

    pv_store.fillna(0, inplace=True)  # NaN은 0으로 처리

    score_select = pv_store[code]
    score_select_den = score_select / sum(score_select)

    # 환경이 비슷한 5개 상권의 업종별 밀집도와 선택한 상권의 업종별 밀집도 차이 계산
    score_diff = score_den['den_mean'] - score_select_den

    # 차이가 클수록 추천도 증가
    score_diff_sort = score_diff.sort_values(ascending=False)[0:5]
    rec_den = [item for item in pv_store.loc[score_diff_sort.index].index]

    sales = rec_sales[:5]  # ['반찬가게', '스포츠 강습', '한식음식점', '호프-간이주점', '슈퍼마켓']
    den = rec_den[:5]


    # 입력상권의 업종별 분기매출평균 df  --> 상권코드별로 존재하는 업종 종류 다름
    com = service_sales['상권_코드_명'] == name
    serv_sales = service_sales[com][['서비스_업종_코드_명', '분기별매출평균']]

    def merge_two_dicts(x, y):
        z = x.copy()
        z.update(y)
        return z

    sales_dict = {}  # 매출 top5 결과 dict
    for i in sales:
        serv = serv_sales['서비스_업종_코드_명'] == i
        sales = serv_sales[serv][['서비스_업종_코드_명', '분기별매출평균']]  # 업종 매출 df

        position_sales_dict = dict([(x, int(y)) for x, y in zip(sales['서비스_업종_코드_명'], sales['분기별매출평균'])])
        sales_dict = merge_two_dicts(sales_dict, position_sales_dict)
        # print(sales_dict)

    den_dict = {}  # 밀집도 top5 결과 dict
    for i in den:
        serv = serv_sales['서비스_업종_코드_명'] == i
        den = serv_sales[serv][['서비스_업종_코드_명', '분기별매출평균']]  # 업종 매출 df

        position_sales_dict = dict([(x, int(y)) for x, y in zip(den['서비스_업종_코드_명'], den['분기별매출평균'])])
        den_dict = merge_two_dicts(den_dict, position_sales_dict)

    return sales_dict, den_dict


