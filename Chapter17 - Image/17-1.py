#認識Pillow 模組的RGBA
#getrgb()

from PIL import ImageColor, Image


print(ImageColor.getrgb('#0000ff'))

#Box Tuple (left, top, right, bottom), 解析度(resolution)

#影像大小屬性

rushMore = Image.open('E:\Python王者歸來\Chapter17 - Image\Screenshot 2023-07-19 162915.png')
print('列出物件型態', type(rushMore))
width, height = rushMore.size
print('Width', width)
print('Height', height)
print('FileName', rushMore.filename)
print('FileSubName', rushMore.format)
print('Description of Object', rushMore.format_description)

#Display Image 
#rushMore.show()

#resize(), resize(width, heigh), Image.BILINEAR

#NewPic = rushMore.resize((width*5, height*2)).save('test.png')

#rotate()
#rushMore.rotate(90).save('test2.png')

#crop()
#test3 = rushMore.crop((80, 30, 150, 100))
#test3.save('./test3.png')
