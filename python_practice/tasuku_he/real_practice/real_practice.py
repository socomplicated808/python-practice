from selenium import webdriver
import pandas as pd
import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

url = 'https://system.reins.jp/reins/ktgyoumu/KG001_001.do'
screenshot_filename = 'screenshot.png'
filename = 'results.csv'
username = '130334632665'
password = '080409'
titles = []
prices = []

reins = webdriver.Firefox()
reins.get(url)
#login_button = reins.find_element_by_xpath('/html/body/table[2]/tbody/tr/td/div[1]/a/img')
#login_button.click()
username_field = reins.find_element_by_name('usrId')
username_field.send_keys(username)
password_field = reins.find_element_by_name('inpswrd')
password_field.send_keys(password)
image = reins.find_element_by_xpath('/html/body/table/tbody/tr/td/form[1]/table[1]/tbody/tr/td/table/tbody/tr[3]/td[2]/img')
location = image.location
size = image.size
reins.get_screenshot_as_file(screenshot_filename)

captcha = Image.open(screenshot_filename)

captcha = captcha.crop((748,424,904,451))
captcha.save('captcha.png')

text = pytesseract.image_to_string(captcha,config='--psm 7 -c tessedit_char_whitelist=0123456789')

captcha_field = reins.find_element_by_xpath('/html/body/table/tbody/tr/td/form[1]/table[1]/tbody/tr/td/table/tbody/tr[4]/td[2]/input')


captcha_field.send_keys(text)

login_button = reins.find_element_by_xpath('/html/body/table/tbody/tr/td/form[1]/table[3]/tbody/tr/td[2]/input')
login_button.click()

#reins.close()
