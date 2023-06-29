#pip3 install pytesseract
#ocr need clean picture, no difficult chinese or special character
import os
import glob
from PIL import Image
import pytesseract

#pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
def get_grayscale_image(filepath):
    fp = Image.open(filepath)
    # 转为灰度图片
    imgry = fp.convert('L')
    # 二值化，采用阈值分割算法，threshold为分割点,根据图片质量调节
    threshold = 150
    table = []
    for j in range(256):
        if j < threshold:
            table.append(0)
        else:
            table.append(1)
    return imgry.point(table, '1')

def remove_blankline(srcfile,dstfile):
    with open(dstfile, 'a', encoding="utf-8") as f1:
        for line in open(srcfile, encoding="utf-8"):
            if line == '\n':
                line = line.strip("\n")
            f1.write(line)
    os.remove(srcfile)
    #open the result file
    os.system(dstfile)

imagepath = glob.glob(os.path.join(r'D:\temp\pic','*'))
res_origin = r'D:\temp\temp.txt'
res_noblank = r'D:\temp\res.txt'

for file in imagepath:
    img = get_grayscale_image(file)
    # OCR识别：lang指定中文,--psm 6 表示按行识别，有助于提升识别准确率
    text = pytesseract.image_to_string(img, lang='chi_sim+eng',config='--psm 6')
    
    with open(res_origin, 'a', encoding="utf-8") as f:
        f.write(text)

remove_blankline(res_origin,res_noblank)