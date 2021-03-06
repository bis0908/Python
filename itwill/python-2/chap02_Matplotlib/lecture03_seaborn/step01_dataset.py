# -*- coding: utf-8 -*-
"""
Seaborn : Matplotlib 기반 다양한 배경 테마, 통계용 차트 제공
seaborn dataset
"""

import seaborn as sb # 별칭

# 1. 그래프 배경 스타일
sb.set_style(style='darkgrid')
'''
그래프 배경 스타일
style = “darkgrid”, “whitegrid”, “dark”, “white”, “ticks”
'''

# 2. seaborn dataset: 자체 제공 dataset
print(sb.get_dataset_names())
# ['anagrams', 'anscombe', 'attention', 'brain_networks', 'car_crashes', 'diamonds', 'dots', 'exercise', 'flights', 'fmri', 'gammas', 'geyser', 'iris', 'mpg', 'penguins', 'planets', 'tips', 'titanic']

iris = sb.load_dataset('iris')
print(iris.info())

tips = sb.load_dataset('tips')
print(tips.info())

titanic = sb.load_dataset('titanic')
print(titanic.info())

flights = sb.load_dataset('flights')
print(flights.info())

# 3.
