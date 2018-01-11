class InvalidMenuException(Exception):
    def __str__(self):
        return "존재하지 않는 메뉴를 입력하셨습니다."
