from Account.Account import *

class NormalAccount(Account):
    def __init__(self, accID, balance, cusName, interRate):
        Account.__init__(self, accID, balance, cusName)
        self.interRate=interRate

    def deposit(self, money):
        Account.deposit(self, money)
        Account.deposit(self, money*(self.interRate/100))
    def showAccInfo(self):
        Account.showAccInfo(self)
        print("이자율 : %d" % self.interRate)
