'''
step05 문제

 문3) 다음 movie 객체를 대상으로 평점 8이상인 영화 제목과 전체 누적관객수를 출력하시오.

 <출력 결과>
 영화제목 : 광해, 관상
 누적 관객수 =  2,100
'''

movie = {'광해' : [9.24, 1200], '공작' : [7.86, 500], '관상' : [8.01, 900]}

tot = 0
print('영화 제목:', end = ' ')
for t, d in movie.items():
    if d[0] >= 8.0:
        print(t, end = ' ')
        tot += d[1]

print('\n 누적 관객수:', format(tot, '3,d'))