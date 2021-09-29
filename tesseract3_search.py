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
mylist=[]
for link in soup.find_all('img'):
    try: 
        im = (Image.open(urllib.request.urlopen(link.get('src'))).convert('L'))
        im = im.filter(ImageFilter.MedianFilter())       # a little blur
        im = im.point(lambda x: 0 if x < 140 else 255) 
        text = pytesseract.image_to_string(im) #pass pre processed image
        print('\n'+text)
        mylist.append(text)
        images.append(im)
    except:
        print('\nnot correct image format')


# mylist = ['apple','google','microsoft']

for x in mylist:
    print(x)#x is the search Query stored in mylist
    webbrowser.open('https://google.com/search?q='+x)
    # this will search the Query in new tab of my browser

