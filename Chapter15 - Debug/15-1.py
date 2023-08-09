def division(x,y):
    try:
        return x/y
    except ZeroDivisionError:
        print('除數不可為零')
print(division(10,2))
print(division(5,0))

def passWord(pwd):
    pwdlen = len(pwd)
    if pwdlen < 5:
        raise Exception('Too short')
    if pwdlen > 8:
        raise Exception('Too Long')
    print('Right')
for pwd in ('aaaaabbbb', 'aaa', 'aaabbb'):
    try :
        passWord(pwd)
    except Exception as err:
        print('Error', str(err))

#Traceback 指出程式設計錯誤的原因
import traceback


def passWord(pwd):
    pwdlen = len(pwd)
    if pwdlen < 5:
        raise Exception('Too short')
    if pwdlen > 8:
        raise Exception('Too Long')
    print('Right')
for pwd in ('aaaaabbbb', 'aaa', 'aaabbb'):
    try :
        passWord(pwd)
    except Exception as err:
        errlog = open('error.txt', 'a',encoding='utf-8') #UnicodeEncodeError 指定編碼
        errlog.write(traceback.format_exc())
        errlog.close()
        print('Error', str(err))

#Finally 主要用在 Python 程式與資料庫連接
def division(x, y): 
    try:
        return x/y
    except:
        print('Error')
    finally:
        print('complete')
    
#Assert  斷言 -O 可以終止斷言
class Banks():
    bankname = 'Taipei Bank'
    def __init__(self,username,money) -> None:
        self.username = username
        self.money = money
    def save_money(self,money):
        assert money > 0 , 'Money should more than 0'
        self.money += money
        print('Deposit', money, 'Success')
    def withdraw_money(self,money,balance):
        assert money > 0 , 'Should be more than 0'
        assert money <= self.money, 'balance not enough'
        self.money -= money
        print('Withdraw', money, 'Success')
    def get_balance(self):
        print(self.name.title(),'Balance:', self.balance)
Tommy = Banks('Tommy', 100)
Tommy.save_money(-300)

#Logging 共有五個等級， DEBUG: 顯示程式日誌， INFO: 記錄一般發生的事件，WARNING: 雖然不會影響程式的執行但未來可能會導致問題發生
import logging

logging.basicConfig(level=logging.debug)
