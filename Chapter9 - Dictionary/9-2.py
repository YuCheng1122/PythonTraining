# items 
players = {'Stephen Curry':'GoldenState Warriors',
           'Stephen Curry1':'GoldenState Warriors',
           'Stephen Curry':'GoldenState Warriors',
           'Stephen Curry':'GoldenState Warriors',
           'Stephen Curry':'GoldenState Warriors',
           'Stephen Curry':'GoldenState Warriors'}
for name, team in players.items(): #tuple
    print("\nName: ", name)
    print("Team: ", team)

# fromkeys()
seq1 = ['name', 'city']
list_dict1 = dict.fromkeys(seq1)
print(f'dict1 {list_dict1}') #Replace value
list_dict2 = dict.fromkeys(seq1,'Chicago')
print(f'dict2 {list_dict2}')

#Big Dictionary
asia = ('Beijing', 'Hongkong')
world = {'Asia':asia}
print(world)

#Formatted String 
text = '%d %.2f %s' % (1, 99.3, 'Justin')
# 1 99.30 Justin

#Sorted
thing = {'iWatch':(15000,0.1),
         'Asus': (35000, 0.7)}
th = sorted(thing.items(), key=lambda item:item[1][0])
print('\nSorted by the price')
print('------------------------------')
for i in range(len(th)):
    print(f'{th[i][0]:8s}{th[i][1][0]:10d}{th[i][1][1]:10.2f}')

