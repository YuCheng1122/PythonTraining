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

#__iter__() 迭代物件
