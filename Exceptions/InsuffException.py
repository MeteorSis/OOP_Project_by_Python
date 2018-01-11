class InsuffException(Exception):
    def __init__(self, balance):
        self.balance=balance
    def __str__(self):
        return "잔액이 모자랍니다. : (잔액 : %d원)" % self.balance
