# 集合的基本概念是無序且每個元素是唯一的，其實也可以將集合看成是字典的鍵，每個鍵皆是唯一的，集合元素的內容是不可變的(Immutable)。
# 可變物件：該變數所指向記憶體中的值可以被改變
# 不可變物件：該變數所指向記憶體中的值不可以被改變，所以當變數指向的值改變時，等於將原來的值複製一份後存於一個新的地址，變數再指向這個新的地址
# 不可變物件：int, string, float, tuple, frozenset
# 可變物件：list, dict, set
# https://hackmd.io/@Kirin/rJAa3VF5s

Student = {'Peter', 'Tommy','Thomas','Alice'}
Math = {'Peter', 'Tommy'}
Physics = {'Thomas','Tommy'}

Union = Math | Physics
print('Have %d people will join Math or Physices'% len(Union),Union)
unAttend = Student - Union
print('Neither Math nor Physics have %d people'% len(unAttend),unAttend)

A = {n for n in range(1,100,2)}
print(type(A))
print(A)

A = {n for n in range(1,100) if n%11==0}
print(type(A))
print(A)

for n in range(1,100):
    if n%11 == 0:
        print(n)

word = 'deepmind'
alphabetCount = {alphabet: word.count(alphabet) for alphabet in set(word)}
print(alphabetCount)

#Cocktail Example
