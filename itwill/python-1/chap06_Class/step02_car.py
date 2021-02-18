# -*- coding: utf-8 -*-
"""
step02_car

1. self 인수: 멤버(속성, 메서드)를 호출하는 객체
self.속성
self.메서드()

2. 동적 속성(변수)
 - 생성자나 메서드에서 동적으로 만들어지는 속성


@author: wonseok
"""

class Car:
    # 1. 속성: data 저장
    name = None
    cc  = 0
    door = 0

    # 2. 생성자: 객체 생성 + 속성 초기화
    def __init__(self, name, cc, door):
        self.name = name
        self.cc = cc
        self.door = door

    # 3. 메서드(함수) : data 처리
    def carType(self):
        if self.cc >= 3000:
            self.kind = '대형'
        else:
            self.kind = '준중형'

    def carInfo(self):
        print('{} is {} cc{}, door is {} ea'.format(self.name, self.cc, self.kind, self.door))

car1 = Car('Malibu', 2000, 4)
car1.name
car1.cc
car1.door
car1.carType()
car1.carInfo()
