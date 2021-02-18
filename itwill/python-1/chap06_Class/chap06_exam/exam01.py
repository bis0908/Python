'''
 문1) 다음 처리조건에 맞게 Rectangle 클래스를 정의하시오.
 <처리조건>
 1. 멤버 변수 : 가로(w), 세로(h)
 2. 생성자 : 가로(w), 세로(h) 멤버 변수 초기화
 3. 멤버 메서드(area_calc) : 사각형의 넓이를 구하는 메서드
          사각형 넓이 = 가로 * 세로
 4. 멤버 메서드(circum_calc) : 사각형의 둘레를 구하는 메서드
          사각형 둘레 = (가로 + 세로) * 2
 5. 기타 출력 예시 참조

       << 출력 예시 >>
    사각형의 넓이와 둘레를 계산합니다.
    사각형의 가로 입력 : 10
    사각형의 세로 입력 : 5
    ----------------------------------------
    사각형의 넓이 : 50
    사각형의 둘레 : 30
    ----------------------------------------
'''
print("사각형의 넓이와 둘레를 계산합니다.")
width = int(input('사각형의 가로 입력 : '))
height = int(input('사각형의 세로 입력 : '))


class Rectangle:
    w = 0
    h = 0

    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area_calc(self):
        area = self.w  * self.h
        return area

    def circum_calc(self):
        circum = (self.w  + self.h) * 2
        return circum

calc = Rectangle(width, height)


print('-' * 50)
print('사각형의 넓이: ', calc.area_calc())
print('사각형의 둘레: ', calc.circum_calc())
print('-' * 50)

calc.w


