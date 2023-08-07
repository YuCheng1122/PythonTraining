# _doc_ 列印文件字串
def getMax(x,y):

    if int(x) > int(y):
        return x
    else: 
        return y
print(getMax.__doc__)

#_str_()方法, _repr_() --> 協助返回易讀取的字串，在沒有定義__str__()是不會獲得易讀取的結果，因為powershell視窗讀取類別變數a系統是呼叫_repr_()所以需要定義這個方法。
class Name:
    def __init__(self, name) -> None:
        self.name = name
    def __str__(self) -> str:
        return f'{self.name}'
    __repr__ =__str__

#__iter__() 迭代物件，類似於list 或 tuple，提供給for....in 循環內使用，這時類別需要next()方法取得下一個值。
class Fib():
    def __init__(self,max) -> None:
        self.max=max
    def __iter__(self):
        self.a = 0
        self.b = 1
        return self
    def __next__(self):
        fib = self.a
        if fib > self.max:
            raise StopIteration
        self.a , self.b = self.b, self.a + self.b
        return fib
for i in Fib(100):
    print(i)
# __eq__() Method __eq__() == equals
class City():
    def __init__(self, name) -> None:
        self.name = name
    def equals(self, city2):
        return self.name.upper() == city2.name.upper()
    def __eq__(self, city2):
        return self.name.upper() == city2.name.upper()
    