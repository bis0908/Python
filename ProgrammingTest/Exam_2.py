class Calculator:
    num = 0
    def add(self, num):
        self.num += num
        return self

    def subtract(self, num):
        self.num -= num
        return self

calc = Calculator()
result = calc.add(4).add(5).subtract(3)
print(result.num)