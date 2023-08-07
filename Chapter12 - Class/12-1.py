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
#封裝Encapsulation : Attribute 可以讓外部引用稱為公有屬性 --> 私有屬性: 確保類別內的屬性安全

class BanksP():
    def __init__(self,username) -> None:
        self.__name = username
        self.__balance = 0
        self.__bankname = 'Taipei Bank'
    def save_money(self,money):
        self.__balance += money
        print('Deposit', money, 'Success')
    def withdraw_money(self,money):
        self.__balance -= money
        print('Withdraw', money, 'Success')
    def get_balance(self):
        print(self.__name.title(),'Balance:', self.__balance)
TommyBank=BanksP('Tommy')
TommyBank.save_money(100)

#Private Method
class BanksPM():
    def __init__(self,username) -> None:
        self.__name = username
        self.__balance = 0
        self.__bankname = 'Taipei Bank'
        self.__rate = 30
        self.__service_charge = 0.1
    def save_money(self,money):
        self.__balance += money
        print('Deposit', money, 'Success')
    def withdraw_money(self,money):
        self.__balance -= money
        print('Withdraw', money, 'Success')
    def get_balance(self):
        print(self.__name.title(),'Balance:', self.__balance)
    def US_to_NTD(self,USD):
        self.result=self.__cal_rate(USD)
        return self.result
    def __cal_rate(self,USD):
        return int(USD * self.__rate * (1-self.__service_charge))
    
TommyBank=BanksPM('Tommy')
print(f'10 can exchange {TommyBank.US_to_NTD(10)} NTD')

#Base Class and Derived Class
class Father():
    def hometown(self):
        print('I live in Taipei')
class Son(Father):
    pass
#Private Attribute 存取私有屬性可以透過return的方式進行
class Father():
    def hometown(self):
        self.__address= 'Taipei'
    def getAddress(self):
        return self.__address
class Son(Father):
    pass

#衍生類別引用基底類別的方法
class Animal():
    def __init__(self,animal_name,animal_age):
        self.name = animal_name
        self.age = animal_age
    def run(self):
        print(self.name.title(), 'is runnning')
class Dog(Animal):
    def __init__(self, animal_name, animal_age):
        super().__init__(animal_name, animal_age)

#衍伸類別有自己的方法
class Animal():
    def __init__(self,animal_name,animal_age):
        self.name = animal_name
        self.age = animal_age
    def run(self):
        print(self.name.title(), 'is runnning')
class Dog(Animal):
    def __init__(self, animal_name, animal_age):
        super().__init__(animal_name, animal_age)

#兄弟類別屬性取得
class Father():
    def __init__(self) -> None:
        self.fathermoney = 10000
class Tommy(Father):
    def __init__(self) -> None:
        super().__init__()
        self.TommyMoney = 10000000
class Tim(Father):
    def __init__(self) -> None:
        self.TimMoney = 100
        super().__init__()
    def getMoney(self):
        print(f'Father: {self.fathermoney}')
        print(f'\n Tommy Money: {self.TimMoney}')
i=Tim()
i.getMoney()

#Polymorphism
claslass Animals():
    def 