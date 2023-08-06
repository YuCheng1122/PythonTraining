# 屬性: Attribute, 方法: Method
# 初始化整個類別，所謂的初始化類別是類別內建立一個初始化方法，當在程式內宣告這個類別的物件時將自動執行這個方法。

class Banks():
    bankname = 'Taipei Bank'
    def __init__(self,username,money) -> None:
        self.username = username
        self.money = money
    def save_money(self,money):
        self.balance += money
        print('Deposit', money, 'Success')
    def withdraw_money(self,money):
        self.balance -= money
        print('Withdraw', money, 'Success')
    def get_balance(self):
        print(self.name.title(),'Balance:', self.balance)
#封裝Encapsulation

