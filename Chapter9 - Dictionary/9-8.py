# Dict Generator
word = 'deepmind'
alphabetCount = {alphabet: word.count(alphabet) for alphabet in word}
print(alphabetCount)

#Zodiac Sign
season = {'Sagittarius':'11/23-12/21',
          'Capricon':'12/22-1/20'}
wd = input('Search Zodiac?')
if wd in season:
    print(wd,'Period',season[wd])
else:
    print('None')