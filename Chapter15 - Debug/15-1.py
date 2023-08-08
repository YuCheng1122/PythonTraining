def division(x,y):
    try:
        return x/y
    except ZeroDivisionError:
        print('除數不可為零')
print(division(10,2))
print(division(5,0))