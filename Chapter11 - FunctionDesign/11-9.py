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