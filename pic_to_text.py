#pip3 install pytesseract
import os
import glob
from PIL import Image
import pytesseract



#pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
path = r"D:\temp\pic"
imagelist = glob.glob(os.path.join(path,'*'))
#imagelist = [i for i in os.listdir(path)]

for file in imagelist:
    img = Image.open(file)
    text = pytesseract.image_to_string(img, lang='chi_sim+eng')
    with open(r'D:\temp\res.txt', 'a', encoding="utf-8") as f:
        f.write(text)

with open(r'D:\temp\res_noblankline.txt', 'a', encoding="utf-8") as f1:
    for line in open(r'D:\temp\res.txt', encoding="utf-8"):
        if line == '\n':
            line = line.strip("\n")
        f1.write(line)



#ocr problem:  need clean picture, no difficult chinese character or special character