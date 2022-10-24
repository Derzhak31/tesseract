import pytesseract         # INFO https://tesseract-ocr.github.io/tessdoc/
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

img = Image.open('russian.png')

file_name = img.filename
file_name = file_name.split('.')[0]

text = pytesseract.image_to_string(img, lang='rus')
print(text)

with open(f'{file_name}.txt', 'w') as txt:
    txt.write(text)
    