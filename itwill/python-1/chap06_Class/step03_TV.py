# -*- coding: utf-8 -*-
"""
step03_TV

기본 생성자
 - 생성자를 생략하면 기본 생성자가 만들어진다.

@author: wonseok
"""

class default:

    def data(self, x, y):
        self.x = x
        self.y = y

    def mul(self):
        return self.x * self.y

obj = default()
obj.data(10, 20)
obj.mul() # 200

# class 설계

class tv:

    # 속성: 전원, 볼륨, 채널
    power = False
    volume = 7
    channel = 5

    # 메서드: 속성처리
    def changePower(self):
        self.power = not(self.power) # F <-> T

    def volumeUp(self):
        self.volume += 1

    def volumeDown(self):
        self.volume -= 1

    def channelUp(self):
        self.channel += 1

    def channelDown(self):
        self.channel -= 1

    def tvInfo(self):
        print(f'전원 상태: {self.power}, 채널 번호: {self.channel}, 볼륨: {self.volume}')


tv1 = tv()
tv1.changePower()
tv1.channelUp
tv1.volumeUp()
tv1.tvInfo()
