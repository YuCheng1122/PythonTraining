#正規表達式主要功能是執行模式的比對與搜尋，甚至文件也可以用正規表達式處理搜尋和取代功能。
def taiwanPhoneNum(string):
    if len(string) != 12:
        return False
    for i in range(0,4):
        if string[i].isdecimal() ==False: #isdecimal 數字位元
                return False
    if string[4] != '':
         return False
    for i in range(0,8):
         if string[i].isdecimal() == False:
              return False
    if string[8] != '-':
         return False
#正則表達式的基礎，建立搜尋字串模式pattern，這個方法使用\d表示0-9的數字字元。
#Regex 是 Regular Expression 的簡稱，search()可以執行字串搜尋

msg = 'Please call 0906-171-101'
msg1 = '0906171101'

import re
def parseString(string):
    pattern = r'\d\d\d\d-\d\d\d-\d\d\d'
    phoneNum = re.search(pattern, string)
    if phoneNum != None:
          print(f'Phone Number: {phoneNum.group()}')
    else:
         print(f'{string} string not contain phone number')
parseString(msg)
parseString(msg1)

#groups() 多重指定 
msg2 = 'My phone num is 02-22706160 '
pattern = r'(\d{2})-(\d{8})'
phoneNum = re.search(pattern, msg2)
areaNum, localNum = phoneNum.groups()
print(f'Area:{areaNum}')
print(f'Local:{localNum}')

#貪婪和非貪婪搜尋
def searchStr(pattern, msg):
    txt = re.search(pattern, msg)
    if txt == None:
          print('Search Failed', txt)
    else:
        print('Search Success', txt.group())
msg = 'son'
msg2 = 'sonsonsonsonson'
pattern = '(son){3,5}' #3,4,5都算找到但最後會輸出5，這個就稱為Greedy
searchStr(pattern, msg)
searchStr(pattern, msg2)

pattern2 = '(son){3,5}?' # Not Greedy
searchStr(pattern2,msg2)

#re.match(): 只會比對開頭而已
msg = 'John will attend my party tonight.'
pattern ='John'
txt = re.match(pattern, msg)
if txt != None:
     print('Yes')

#group(): 傳回搜尋到的字串， end(): 搜尋到字串的結束位置， start(): 搜尋到字串的起始位置

#sub(): 基礎用法 --> result = re.sub(pattern, newstr, msg) pattern為欲搜尋字串，成功後用newstr取代，

pattern = r"""
(\d{2})|\(d{2}\)?
(\s|-)?
\d{8}
(\s*(ext|ext.)\s*\d{2,4})?
)"""

phoneNum = re.findall(pattern, msg, re.VERBOSE)
for num in phoneNum:
     print(num[0])