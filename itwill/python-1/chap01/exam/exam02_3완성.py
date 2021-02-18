'''
step02 문제
'''

''' 
문3) 지방(fat), 탄수화물(carbohydrate), 단백질(protein)            
       칼로리의 합계를 계산하는 프로그램을 작성하시오.
    조건1> 지방, 탄수화물, 단백질의 그램을 키보드로 입력받음 
    조건2> dict에 저장된 3개 데이터 이용 총 칼로리 계산
               총 칼로리 = 지방 * 9 + 단백질 * 4 + 탄수화물 * 4              
    조건3> 총 칼로리 출력 : format()함수 이용
    
   <<화면출력 결과>>
  지방의 그램을 입력하세요 : 25
  탄수화물의 그램을 입력하세요 : 520
  단백질의 그램을 입력하세요 : 45
  총칼로리 : 2,485 cal
'''

fat = int(input('지방의 그램을 입력하세요 : ')) # 25
carbohydrate = int(input('탄수화물의 그램을 입력하세요 : ')) # 520
protein = int(input('단백질의 그램을 입력하세요 : ')) # 45

totCalorie = fat * 9 + carbohydrate * 4 + protein * 4 

# 문자열과 함께 출력
print('총 칼로리 : {0:3,d} cal'.format(totCalorie))
# 총 칼로리 :  2,485  cal

