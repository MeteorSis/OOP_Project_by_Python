from Exceptions.InsuffException import *
from Exceptions.MinusException import *

class Account:
    def __init__(self, accID, balance, cusName):
        self.accID=accID
        self.balance=balance
        self.cusName=cusName
    def deposit(self, money):
        if money<0:
            raise MinusException(money)
        self.balance+=money
    def withdraw(self, money):
        if money<0:
            raise MinusException(money)
        if self.balance<money:
            raise InsuffException(self.balance)
        self.balance-=money
    def showAccInfo(self):
        print()
        print("""계좌ID : %d
이 름 : %s
잔 액 : %d""" % (self.accID, self.cusName, self.balance))
