from Account.NormalAccount import *

class HighCreditAccount(NormalAccount):
    def __init__(self, accID, balance, cusName, interRate, specialRate):
        NormalAccount.__init__(self, accID, balance, cusName, interRate)
        self.specialRate=specialRate
    def deposit(self, money):
        NormalAccount.deposit(self, money)
        if self.specialRate=='A' or self.specialRate=='a':
            spRate=0.07
        elif self.specialRate=='B' or self.specialRate=='b':
            spRate=0.04
        elif self.specialRate=='C' or self.specialRate=='c':
            spRate=0.02
        Account.deposit(self, money*spRate)
    def showAccInfo(self):
        NormalAccount.showAccInfo(self)
        print("신용등급 : %c" % self.specialRate)
