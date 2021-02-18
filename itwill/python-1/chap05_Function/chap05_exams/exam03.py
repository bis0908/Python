'''
 문3) tot 함수를 인수로 받아서 dataset 각 원소의 합을 계산하는 함수를 완성하시오.

  <출력 결과>
  tot = [12.5, 7, 22.3]
'''

def tot(x):
    return sum(x)

def my_func(tot, datas):
    re = [tot(x) for x in datas]
    return re


# dataset
dataset = [[2,4.5,6], [3,4], [5,8.3,9]]

my_func(tot, dataset)
