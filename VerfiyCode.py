#-*-coding:utf-8 -*-
try:
    import pytesseract
    from PIL import Image

except ImportError:
    print '模块导入错误，请使用pip安装'
    raise SystemExit

image = Image.open('sample5.jpg')
code =pytesseract.image_to_string(image)
print code