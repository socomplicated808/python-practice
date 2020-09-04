from selenium import webdriver
import urllib.request
import pytesseract
from PIL import Image
import time

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

filename = 'capcha.png'

site = webdriver.Firefox()

site.get("https://www.phpcaptcha.org/try-securimage/")

capcha = site.find_element_by_id('captcha_one')
capcha_url = capcha.get_attribute('src')

urllib.request.urlretrieve(capcha_url,filename)

img = Image.open(filename)
text = pytesseract.image_to_string(img,config='--psm 8 --oem 3')
print(text)

site.close()
