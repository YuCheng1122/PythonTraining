#QR Code 邊框區: 非資料區，至少需要4個模塊，主要是避免QR Code 周遭的圖影響辨識， 定位標記: 有三個定位點幫助掃描定位， 校正圖塊: 校正辨識， 容錯修功能: QR Code 面積越大容錯能力就越強大
import qrcode
import pytesseract
from PIL import Image

code = 'https://google.com'
img = qrcode.make(code)
print('filetype:', type(img))
img.save('Chapter17 - Image/ qrcode.png')

qr = qrcode.QRCode(version= 1,
                   error_correction= qrcode.constants.ERROR_CORRECT_M,
                   box_size=10,
                   border=4)
qr.add_data('Google')
img = qr.make_image(file_color='blue', back_color='yellow')
img.save('Chapter17 - Image/qrcode2.png')


# 使用絕對路徑
image_path = 'E:\\Python王者歸來\\Chapter17 - Image\\4484405.jpg'

text = pytesseract.image_to_string(Image.open(image_path))
print(type(text), ' ', text)

image_path2= 'E:\Python王者歸來\Chapter17 - Image\Screenshot 2023-07-19 162915.png'
text2 = pytesseract.image_to_string(Image.open(image_path2), lang='chi_tra')
print(text2)
with open('E:\\Python王者歸來\\Chapter17 - Image\\result.txt','w') as fn:
    fn.write(text2)