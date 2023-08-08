import os
import glob

# os.walk()

for dirName, sub_dirName, fileNames in os.walk('oswalk'):
    print(dirName)
    print(sub_dirName)
    print(f'fileNames\n')
# os.path()
print(os.path.abspath('.'))
print(os.path.abspath('..'))
print(os.path.abspath('14-1.py'))

# glob
for file in glob.glob('D:\PythonTraining\Chapter14 - os Model\*.*'):
    print(f'{file}: {os.path.getsize(file)} bytes')
    
# 分析檔案、加密檔案
def modifySong(songStr):
    for ch in songStr:
        if ch in '.?,':
            songStr = songStr.replace(ch, '')
    return songStr

def wordCount(songCount): # 字串轉串列
    global mydict
    songList = songCount.split()
    print('以下是歌曲串列')
    print(songList)
    mydict = {wd: songList.count(wd) for wd in set(songList)}
    
fn = 'D:\PythonTraining\Chapter14 - os Model\data.txt'
with open(fn) as fileObj:
    data = fileObj.read()
    print('以下是所讀取的歌曲')
    print(data)

mydict = {}
print('大寫改小寫') 
song = modifySong(data.lower())
print(song)
wordCount(song)
print('Result')
print(mydict)   

#加密檔案
import string

def encrypt(text, encryDict):
    cipher = []
    for i in text:
        v = encryDict[i] #encrypt
        cipher.append(v) #encrypt result
    return '' .join(cipher)

abc = string.printable[:-3] #cancel unprintable string
subText = abc[-3:] + abc[:-3] #encrypt list
encry_dict = dict(zip(subText, abc))

with open(fn) as fileObj:
    msg = fileObj.read()
ciphertext = encrypt(msg, encry_dict)

print('Original String')
print(msg)
print('Encrypted String')
print(ciphertext)