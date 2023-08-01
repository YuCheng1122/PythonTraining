# zip function 
a = [1,2,3]
b = [4,5,6]
a, b = zip(*zip(a,b))
zipped = zip(a,b)
print(zipped)
print(list(zipped))
print(a,b) #tuple

mydict = dict(zip('abcde',range(5)))
print(mydict)
mydict2 = dict(zip(['a','b','c'], range(3)))# list
print(mydict2)
