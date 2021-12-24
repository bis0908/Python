
class BakingMachine(object):

    def create_bread(self, breadtype):
        if breadtype == 'cream':
            bread = Cream()
        elif breadtype == 'sugar':
            bread = Sugar()
        elif breadtype == 'butter':
            bread = Butter()
        else:
            print("잘못 입력하셨습니다.")
        return bread

# 빵마다 레시피가 있고 각 recipe 마다 material 3개씩 들어간다

class Cream():
    def recipe(self):
        material = {'flour': 100, 'water': 100, 'cream': 200}
        return material

class Sugar():
    def recipe(self):
        material = {'flour': 100, 'water': 50, 'sugar': 200}
        return material

class Butter():
    def recipe(self):
        material = {'flour': 100, 'water': 100, 'butter': 50}
        return material

baking_machine = BakingMachine()
bread = ['cream', 'sugar', 'butter']
for i in range(len(bread)):
    print("breadType: {}".format(bread[i]))
    baker = baking_machine.create_bread(bread[i])
    print("recipe")
    for key, value in baker.recipe().items():
        print("{}: {}".format(key, value))
    print()