# -*- coding: utf-8 -*-
"""
step05_inheritance

@author: wonseok
"""

class superClass:
    name = None
    age = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f'name: {self.name}, age = {self.age}')



class subClass(superClass):
    gender = None

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def info(self):
        print(f'name: {self.name}, age = {self.age}, gender = {self.gender}')



sub = subClass('자식', 25, '여자')
dir(sub)
sub.info()