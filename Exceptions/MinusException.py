class MinusException(Exception):
    def __init__(self, money):
        self.money=money
    def __str__(self):
        return """입력한 금액 : %d원은 음수입니다.
양수 값을 입력하셔야합니다.""" % self.money
