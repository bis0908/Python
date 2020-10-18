class Car():
    # def start(knock):   #파이썬은 모든 함수를 하나의 arg와 함께 사용한다.
                        # #모든 Method의 첫번째 argument는 Method 그 자신이다.
        # print(knock.doors)
        # print("I started")

# porche = Car()
# porche.color = "Ruby Star"
# porche.start()

#print(dir(Car)) #class에 있는 모든 properties를 보여준다.

    def __init__(self, **kwargs):
            #print(kwargs.get)  #Dictionary 자료구조 
            self.wheels = 4
            self.doors = 4
            self.windows = 4
            self.seats = 4
            self.color = kwargs.get("color", "black")
            self.price = kwargs.get("price", "$20")

    def __str__(self): #기존의 함수를 재정의할 수 있음.
        return f"Car with {self.wheels} wheels"
        
    def take_off(self):
        return "taking off"

class Convertible(Car):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.time = kwargs.get("time", "15")
    
    def take_off(self):
        return "taking off"
        
    def __str__(self): #기존의 함수를 재정의할 수 있음.
        return f"Car with moving roof"


porche = Convertible(color = "Ruby Star", price = "$40")
print(porche.color, porche.price)

# Benz = Car()
# print(Benz.color, Benz.price)