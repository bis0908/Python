# -*- coding: utf-8 -*-
"""
step04_account

@author: wonseok
"""

class Account:
    balance = 0

    def __init__(self, bal):
        self.balance = bal

    def getBalance(self):
        return self.balance

    def deposit(self, money):
        self.balance += money

    def withdraw(self, money):
        if self.balance < money:
            print('잔액 부족')
        else:
            self.balance -= money

acc1 = Account(1000)
print('현재 잔액: ', acc1.getBalance())

acc1.deposit(100000)
print('현재 잔액: ', acc1.getBalance())

acc1.withdraw(50000)
print('현재 잔액: ', acc1.getBalance())