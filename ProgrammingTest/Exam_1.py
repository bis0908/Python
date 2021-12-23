# 미완성 코드입니다.

from abc import ABCMeta, abstractmethod
from itertools import cycle

class BakingMachine(metaclass=ABCMeta):
    def __init__(self):
        self.recipe = {}

    @abstractmethod
    def recipe(self):
        pass

# 빵마다 레시피가 있고 각 recipe 마다 material 3개씩 들어간다

class Cream(BakingMachine):
    def recipe(self):
        self.recipe = {'flour': 100, 'water': 100, 'cream': 200}

class Sugar(BakingMachine):
    def recipe(self):
        self.recipe = {'flour': 100, 'water': 50, 'sugar': 200}

class Butter(BakingMachine):
    def recipe(self):
        self.recipe = {'flour': 100, 'water': 100, 'butter': 50}

# cycle 함수를 이용하여 recipe length 만큼 반복 순환 처리
class Bread(object):
    def bread_property(self, bread_type):
        eval(bread_type)().recipe()
        recipe_cycle = cycle(self.recipe)
        print("recipe")
        for i in range(len(self.recipe)):
            dickey = next(recipe_cycle)
            print(dickey, self.recipe[dickey])

if __name__ == '__main__':
    prpty = Bread()
    brd = str(input("breadType: "))
    prpty.bread_property(brd)