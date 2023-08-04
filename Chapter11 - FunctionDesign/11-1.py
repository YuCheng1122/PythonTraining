# function 其實就是一系列指令敘述所組成，目的有兩個。
# 1. 分割成小功能。除了簡單化，除錯也會比較方便，大型專案分成每個人一小塊可以縮短程式開發時間
# 2. 減少不必要的重複書寫過程

# Recursive Function
import sys
import time


def recur(i):
    if i < 1:
        return 0
    else:
        recur(i-1)
    print(i, end='\t')


recur(2)


def sum(n):
    if n <= 1:
        return 1
    else:
        return n+sum(n-1)


print(f'\nTotal:{sum(5)}')


def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)


print(f'Factorial {factorial(5)}')

# Factorial Time Limitation
print(sys.getrecursionlimit())

# Lamda: 匿名函數，是一個沒有名稱的函數，適合使用在程式中只存在一小段時間的情況，def用於定義一般函數，lamda用於匿名函數


def square(x): return x**2


print(square(2))
# 匿名函數一般用在不需要函數名稱的場合，例如，一些高階函數的部分參數是函數，這時就很適合使用匿名函數，同時可以讓城市變得簡潔。


def mycar(cars, func):
    for car in cars:
        print(func(car))


dreamcars = ['porsche', 'rolls royce', 'maserati']
mycar(dreamcars, lambda carbrand: "My dream car is" + carbrand.title())

#匿名函數使用與filter(func, iterable: 可以重複執行，例如字串(String)、串列(List)或元組(tuple)的元素(item)放入func(item)內，
#然後將func()函數執行結果是True的元素(item)組成新的篩選物件(filter object)回傳)

def oddfn(x):
    return x if (x%2==1) else None
mylist=[5,10,20]
filter_object= filter(oddfn,mylist)

print('Odd list:',[item for item in filter_object])

oddlist = list(filter(lambda x:(x%2==1),mylist))
print('oddlist',oddlist)

#map(func,iterable)將會對iterable 進行重複執行
squarelist = list(map(lambda x: x**2,mylist))
print(type(squarelist))
print('squarelist',squarelist)

#實作字串轉整數
#reduce(func,iterable) iterable
from functools import reduce
def strToInt(s):
    def func(x,y):
        print(x)
        print(y)
        return 10*x+y
    def charToNum(s):
        print('s=',type(s),s)
        mydict = {'5':5,'4':4,'8':8,'7':7}
        n=mydict[s]
        print('n=',type(n),n)
        return n
    return reduce(func,map(charToNum,s))
string = '5487'
x=strToInt(string)+10
print(x)

#Lamda 簡化的版本
def strToInt(s):
    def charToNum(s):
        return {'5':5,'4':4,'8':8,'7':7}[s]
    return reduce(lambda x,y:x*10+y, map(charToNum,s))
x=strToInt(string)+10
print(x)

#x.sort(key=None, reverse=False)
str_len=lambda x:len(x)
strs=['abc','abcd']
print(type(str_len(e) for e in strs))
print([str_len(e)for e in strs])



