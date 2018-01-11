from enum import Enum
from AccountHandler import *

class Menus(Enum):
    MAKE=1
    DEPOSIT=2
    WITHDRAW=3
    INQUIRE=4
    EXIT=5

accHandler=AccountHandler()
while True:
    menu=accHandler.showAndInputMenu()
    if menu==Menus.MAKE.value:
        accHandler.makeAccount()
    elif menu==Menus.DEPOSIT.value:
        accHandler.depositMoney()
    elif menu==Menus.WITHDRAW.value:
        accHandler.withdrawMoney()
    elif menu==Menus.INQUIRE.value:
        accHandler.showAllAccInfo()
    elif menu==Menus.EXIT.value:
        print("프로그램을 종료합니다.")
        break
