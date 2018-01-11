from enum import Enum
from Account.HighCreditAccount import *
from Exceptions.InsuffException import *
from Exceptions.InvalidMenuException import *
from Exceptions.MinusException import *

class KindOfAccounts(Enum):
    NORMALACC=1
    HIGHCREDITACC=2

class AccountHandler:
    def __init__(self):
        self.accArr=[]

    def showAndInputMenu(self):
        while True:
            print()
            print("""-----Menu-----
1. 계좌개설
2. 입 금
3. 출 금
4. 계좌정보 전체 출력
5. 프로그램 종료""")
            try:
                choice=int(input("선택 : "))
                if choice<1 or choice>5:
                    raise InvalidMenuException()
                return choice
            except ValueError:
                print("""정수 값을 입력하셔야합니다.
다시 입력해주십시오""")
            except InvalidMenuException as e:
                print(e)
                print("다시 입력해주십시오")

    def makeAccount(self):
        while True:
            try:
                print()
                kindOfAcc=int(input("""[계좌종류선택]
1. 보통예금계좌 2. 신용신뢰계좌
선택 : """))
                if kindOfAcc != KindOfAccounts.NORMALACC.value \
                   and kindOfAcc!=KindOfAccounts.HIGHCREDITACC.value:
                    raise InvalidMenuException()
                break
            except ValueError:
                print("""정수 값을 입력하셔야합니다.
다시 입력해주십시오""")
            except InvalidMenuException as e:
                print(e)
                print("다시 입력해주십시오")

        if kindOfAcc==KindOfAccounts.NORMALACC.value:
            print()
            print("[보통예금계좌 개설]")
        elif kindOfAcc==KindOfAccounts.HIGHCREDITACC.value:
            print()
            print("[신용신뢰계좌 개설]")


        while True:
            try:
                accID=int(input("계좌ID : "))
                break
            except ValueError:
                print("""정수 값을 입력하셔야합니다.
다시 입력해주십시오""")
                print()

        cusName=input("이 름 : ")

        while True:
            try:
                balance=int(input("입금액 : "))
                if balance<0:
                    raise MinusException(balance)
                break
            except ValueError:
                print("""정수 값을 입력하셔야합니다.
다시 입력해주십시오""")
                print()
            except MinusException as e:
                print(e)
                print("다시 입력해주십시오")
                print()

        while True:
            try:
                interRate=int(input("이자율 : "))
                break
            except ValueError:
                print("""정수 값을 입력하셔야합니다.
다시 입력해주십시오""")
                print()
            
        if kindOfAcc==KindOfAccounts.NORMALACC.value:
            self.accArr.append(NormalAccount(accID, balance, cusName, interRate))
        elif kindOfAcc==KindOfAccounts.HIGHCREDITACC.value:
            while True:
                try:
                    specialRate=input("신용등급 (A, B, C) : ").upper()
                    if ord(specialRate)>=ord('A') and ord(specialRate)<=ord('C'):
                        break
                    raise TypeError
                except TypeError:
                    print("올바르지 않은 등급을 입력하셨습니다.")
                    print()
            self.accArr.append(HighCreditAccount(accID, balance, cusName, interRate, specialRate))

    def depositMoney(self):
        while True:
            try:
                print()
                id=int(input("""[입 금]
계좌ID : """))
                break
            except ValueError:
                print("""정수 값을 입력하셔야합니다.
다시 입력해주십시오""")
        searchedAcc=self.searchID(id)
        if searchedAcc==None:
            print("ID가 존재하지 않습니다.")
            return
        while True:
            try:
                money=int(input("입금액 : "))
                searchedAcc.deposit(money)
                break;
            except ValueError:
                print("""정수 값을 입력하셔야합니다.
다시 입력해주십시오""")
                print()
            except MinusException as e:
                print(e)
                print("다시 입력해주십시오.")
                print()

        print("입금완료")

    def withdrawMoney(self):
        while True:
            try:
                print()
                id=int(input("""[출 금]
계좌ID : """))
                break
            except ValueError:
                print("""정수 값을 입력하셔야합니다.
다시 입력해주십시오""")
        searchedAcc=self.searchID(id)
        if searchedAcc==None:
            print("ID가 존재하지 않습니다.")
            return
        while True:
            try:
                money=int(input("출금액 : "))
                searchedAcc.withdraw(money)
                break;
            except ValueError:
                print("""정수 값을 입력하셔야합니다.
다시 입력해주십시오""")
            except InsuffException as e:
                print(e)
                print("다시 입력해주십시오.")
                print()
            except MinusException as e:
                print(e)
                print("다시 입력해주십시오.")
                print()
                
        print("출금완료")

    def showAllAccInfo(self):
        if len(self.accArr)==0:
            print("고객이 존재하지 않습니다.")
            return
        print()
        print("[전체 계좌]")
        for acc in self.accArr:
            acc.showAccInfo()

    def searchID(self, id):
        for i in range(len(self.accArr)):
            if self.accArr[i].accID==id:
                return self.accArr[i]
        return None
