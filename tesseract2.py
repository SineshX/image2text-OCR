import requests
import sys
import webbrowser
from bs4 import BeautifulSoup
from PIL import Image, ImageEnhance, ImageFilter
import urllib.request
import pytesseract



response = requests.get("https://docs.google.com/forms/d/e/1FAIpQLSdhSVsVoPOMp4HNdzxuCGtcSFIj61JTSkMn8XyOhgdB5psfXg/viewform")

soup = BeautifulSoup(response.content, "html.parser")

# front=Image.open(urllib.request.urlopen('https://avatars.githubusercontent.com/u/48027382')).convert('RGB')
images=[]

for link in soup.find_all('img'):
    print(link.get('src'))
# simple print the links


# for link in soup.find_all('img'):
#     images.append(Image.open(urllib.request.urlopen(link.get('src'))).convert('L'))
#     # converted to greyscale for better processing

# text = pytesseract.image_to_string(im)           # pass preprocessed image to tesseract
# print(text) 

for link in soup.find_all('img'):
    try: 
        im = (Image.open(urllib.request.urlopen(link.get('src'))).convert('L'))
        im = im.filter(ImageFilter.MedianFilter())       # a little blur
        im = im.point(lambda x: 0 if x < 140 else 255)   # threshold (binarize)
        text = pytesseract.image_to_string(im)           # pass preprocessed image to tesseract
        print('\n\n'+text) 
    except:
        print('not correct image format')


    


# im = Image.open(urllib.request.urlopen('https://lh5.googleusercontent.com/ah3RSKmtKnfwxeNCvJhbyUFLa8IDixLAqhXZGQSKM7qydUYipjmOtWwhjdjd2CLFk8mTUo-_DOBKjCnMNNM480-2ivV_CDZp_WTjNAyyfOxsDWNLnan44JuPxVhhy_c_Cw=w740'))

# preprocessing
# im = im.convert('L')    
# for im in images:
#     print(pytesseract.image_to_string(im))
#     # will store later