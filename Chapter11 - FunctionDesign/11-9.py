#sort()
sc = [['John',80],['Tom',90],['Kevin',75]]
sc.sort(key= lambda x:x[0])
print(sc)
sc.sort(key= lambda x:x[1])
print(sc)
#sorted()
#sorted = sorted(iterable,key=None,reverse=False)

#字典成績依照人名(鍵)與分數(值)排序
sc={'John':80, 'Tom':90, 'Kevin':75}
newsc1 = sorted(sc.items(), key= lambda x:x[0])
print(newsc1)
newsc2 = sorted(sc.items(), key= lambda x:x[1])
print(newsc2)

#big to small
thing = {'watch':500, 'iPhone':800}
price = sorted(thing.items(),key= lambda x : x[1], reverse=True)
print(price)

#建立與遍歷迭代器
#可迭代物件包括串列、元組、集合、字典，可以使用iter()函數為這些物件建立迭代器(iterator)
my_list = [1,3,5]
my_iterator = iter(my_list)
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))

#yield 和生成器函數，yield 會回傳值然後區域遍數值會被保留，同時生成器函數會暫停停止執行，直到透過迭代器要取得下一個值才會往下執行。

def iter_data():
    x = 10
    yield x
    x = x*x 
    yield x 
myiter = iter_data()
print(next(myiter))

#生成器與迭代器的優點，此例可以發現如果用串列儲存的話會需要5個元素空間，然而如果用迭代器的話只需要1個元素空間
def list_square(n):
    mylist = []
    for data in range(1, n+1):
        mylist.append(data**2)
    return mylist
print(list_square(5))

def iter(n):
    for data in range(1,n+1):
        yield data**2
myiter = iter(5)
for iter in myiter:
    print(iter)
    
#串列生成(list generator)
list_square = [n**2 for n in range(1,6)]
print(list_square)

#生成器與迭代生成
list_square = (n**2 for n in range(1,6))
for data in list_square:
    print(data)
    
#做一個Range() 函數
def myRange(start=0, end=100, step=1):
    n = start
    while n < end:
        yield n
        n += step
print(type(myRange))
for x in myRange(1,5):
    print(x)    
#做一個費波數
def fibonaci(n):
    a,b = 0,1
    count = 0
    while count < n:
        yield a
        a,b = b, a+b
        count +=1
fib = fibonaci(10)
for num in fib:
    print(num,end=' ')
 
#裝飾器(Decorator): 想在函數內增加一些功能，但是不想更改原本的函數，這時可以使用裝飾器。
def greeting(string):
    return string


def errcheck(func):
    def newFunc(*args):
        if args[1] != 0:
            result =func(*args)
        else: 
            result = '除數不可為0'
    return newFunc
@errcheck
def mydiv(x,y):
    return x/y
print(mydiv(6,2))

#函數重新設計記錄一篇文章每個單字出現次數
def modifySong(songStr):
    for ch in songStr:
        if ch in '.,?':
            songStr = songStr.replace(ch,'')
    return songStr

def wordCount(songCount):
    global mydict
    songList = songCount.split()
    print('down below is list')
    print(songList)
    mydict = {wd: songList.count(wd) for wd in set(songList)}
    
data = """ARE ARE ,,,, YOU YOU YOU,,, ???? HAPPY HAPPY"""

mydict = {}
print('chang to lower case')
song = modifySong(data.lower())
print(song)
wordCount(song)
print('result:')
print(mydict)

#Prime Number
def isPrime(num):
    """Test if num is prime"""
    for n in range(2,num):
        if num % n ==0:
            return False
    return True

