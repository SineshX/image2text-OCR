import sys
# import urllib.request
import pytesseract
from PIL import Image, ImageEnhance, ImageFilter

# IMAGE_PATH = sys.argv[1]
IMAGE_PATH = 'image.jpg'

# open image
im = Image.open(IMAGE_PATH)
# im = Image.open(urllib.request.urlopen('https://lh5.googleusercontent.com/ah3RSKmtKnfwxeNCvJhbyUFLa8IDixLAqhXZGQSKM7qydUYipjmOtWwhjdjd2CLFk8mTUo-_DOBKjCnMNNM480-2ivV_CDZp_WTjNAyyfOxsDWNLnan44JuPxVhhy_c_Cw=w740')).convert('RGB')
# worked
# im = Image.open(urllib.request.urlopen('https://lh5.googleusercontent.com/ah3RSKmtKnfwxeNCvJhbyUFLa8IDixLAqhXZGQSKM7qydUYipjmOtWwhjdjd2CLFk8mTUo-_DOBKjCnMNNM480-2ivV_CDZp_WTjNAyyfOxsDWNLnan44JuPxVhhy_c_Cw=w740'))

# preprocessing
# im = im.convert('L')                             # grayscale
# im = im.filter(ImageFilter.MedianFilter())       # a little blur
# im = im.point(lambda x: 0 if x < 140 else 255)   # threshold (binarize)

text = pytesseract.image_to_string(im)           # pass preprocessed image to tesseract
print('\n\n'+text)                                      # print 

# lesson : tesseract binary was not installed :) also path was not added