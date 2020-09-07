from selenium import webdriver
from selenium.webdriver.support.ui import Select
import os
import pandas as pd
import pytesseract
from PIL import Image
import pyautogui
import time
import urllib.request


#####################################
#            How to Use             #
####################################
# 1. install the gecko driver from the following site 
#    https://github.com/mozilla/geckodriver/releases
# 2. put the .exe you downloaded from the above link into the same folder as the program is in
# 3. install tesseract ocr from the following link 
#    https://tesseract-ocr.github.io/tessdoc/Home.html
# 4. enter the following code leading to the .exe file 
#    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

url = 'https://system.reins.jp/reins/ktgyoumu/KG001_001.do'
screenshot_filename = 'screenshot.png'
filename = 'results.csv'
username = '130334632665'
password = '080409'

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

baibai_bukken_kensaku = reins.find_element_by_xpath('/html/body/table[2]/tbody/tr/td[1]/div[3]/div[1]/form/input[2]')
baibai_bukken_kensaku.click()


#######################################################
#                Defining Parameters                  #
#######################################################

with open('parameters') as file:
    content = file.readlines()
#print(content)
content = [parameter.rstrip('\n') for parameter in content if parameter[0] != '#']
#print(content) 

for parameter in content:
    if parameter == 'uretochi':
        select = reins.find_element_by_name('/html/body/table/tbody/tr/td/form[1]/table[3]/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr[2]/td[2]/select/option[2]')
        select.click()
    elif parameter == 'ureikkodate':
        select = reins.find_element_by_xpath('/html/body/table/tbody/tr/td/form[1]/table[3]/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr[2]/td[2]/select/option[3]')
        select.click()
    elif parameter == 'uremanshon':
        select = reins.find_element_by_xpath('/html/body/table/tbody/tr/td/form[1]/table[3]/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr[2]/td[2]/select/option[4]')
        select.click()
    elif parameter == 'uregaisen':
        select = reins.find_element_by_xpath('/html/body/table/tbody/tr/td/form[1]/table[3]/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr[2]/td[2]/select/option[5]')
        select.click()
    elif parameter == 'uresotoichi':
        select = reins.find_element_by_xpath('/html/body/table/tbody/tr/td/form[1]/table[3]/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr[2]/td[2]/select/option[6]')
        select.click()
    elif parameter == 'shinchikumanshon':
        select = reins.find_element_by_xpath('/html/body/table/tbody/tr/td/form[1]/table[3]/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr[2]/td[6]/select/option[2]')
        select.click() 
    elif parameter == 'chuukomanshon':
        select = reins.find_element_by_xpath('/html/body/table/tbody/tr/td/form[1]/table[3]/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr[2]/td[6]/select/option[3]')
        select.click() 
    elif parameter == 'shinchikutown':
        select = reins.find_element_by_xpath('/html/body/table/tbody/tr/td/form[1]/table[3]/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr[2]/td[6]/select/option[4]')
        select.click()
    elif parameter == 'chuukotown':
        select = reins.find_element_by_xpath('/html/body/table/tbody/tr/td/form[1]/table[3]/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr[2]/td[6]/select/option[5]')
        select.click()
    elif parameter == 'shinchikuresort':
        select = reins.find_element_by_xpath('/html/body/table/tbody/tr/td/form[1]/table[3]/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr[2]/td[6]/select/option[6]')
        select.click()
    elif parameter == 'chuukoresort':
        select = reins.find_element_by_xpath('/html/body/table/tbody/tr/td/form[1]/table[3]/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr[2]/td[6]/select/option[7]')
        select.click()
    elif parameter == 'others':
        select = reins.find_element_by_xpath('/html/body/table/tbody/tr/td/form[1]/table[3]/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr[2]/td[6]/select/option[8]')
        select.click()
    elif parameter == 'shiteinashi':
        select = reins.find_element_by_xpath('/html/body/table/tbody/tr/td/form[1]/table[3]/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr[5]/td[2]/input[1]')
        select.click()
    elif parameter == 'shoyuukennomi':
        select = reins.find_element_by_xpath('/html/body/table/tbody/tr/td/form[1]/table[3]/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr[5]/td[2]/input[2]')
        select.click()
    elif parameter == 'shakuchiken':
        select = reins.find_element_by_xpath('/html/body/table/tbody/tr/td/form[1]/table[3]/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr[5]/td[2]/input[3]')
        select.click()
    elif parameter == 'zumenarinomi':
        select = reins.find_element_by_xpath('/html/body/table/tbody/tr/td/form[1]/table[3]/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr[6]/td[2]/input[1]')
        select.click()
    elif parameter == 'bukkengazouarinomi':
        select = reins.find_element_by_xpath('/html/body/table/tbody/tr/td/form[1]/table[3]/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr[6]/td[2]/input[2]')
        select.click()
    elif parameter == 'zaimukyokubukkennomi':
        select = reins.find_element_by_xpath('/html/body/table/tbody/tr/td/form[1]/table[3]/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr[6]/td[2]/input[3]')
        select.click()
    elif parameter == 'ookushonnomi':
        select = reins.find_element_by_xpath('/html/body/table/tbody/tr/td/form[1]/table[3]/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr[6]/td[2]/input[4]')
        select.click()
    elif parameter == 'shinjukuku':
        select = reins.find_element_by_xpath('//*[@id="tdfkMi1"]')
        select.send_keys('東京都') 
        select = reins.find_element_by_xpath('//*[@id="shzicmi1_1"]')
        select.send_keys('新宿区')
        select = reins.find_element_by_xpath('//*[@id="shzicmi2_1"]')
        select.send_keys('大久保３丁目')
kensaku = reins.find_element_by_xpath('/html/body/table/tbody/tr/td/form[1]/div[8]/input[1]')
kensaku.click()


def scrape(xpath):
    result = []
    i = 2
    while True:
        try:
            scrape = reins.find_element_by_xpath(xpath.format(i))
            result.append(scrape.text)
            i += 1
        except:
            break
    return result


number = scrape('/html/body/table/tbody/tr/td/form[1]/table[3]/tbody/tr/td/table/tbody/tr[{}]/td[3]')
torihikijoutai = scrape('/html/body/table/tbody/tr/td/form[1]/table[3]/tbody/tr/td/table/tbody/tr[{}]/td[4]')
kakaku_kanri = scrape('/html/body/table/tbody/tr/td/form[1]/table[3]/tbody/tr/td/table/tbody/tr[{}]/td[5]/div')
price_per_size = scrape('/html/body/table/tbody/tr/td/form[1]/table[3]/tbody/tr/td/table/tbody/tr[{}]/td[6]/div')
location_name_floor = scrape('/html/body/table/tbody/tr/td/form[1]/table[3]/tbody/tr/td/table/tbody/tr[{}]/td[7]')
train_line = scrape('/html/body/table/tbody/tr/td/form[1]/table[3]/tbody/tr/td/table/tbody/tr[{}]/td[8]')
walk_time = scrape('/html/body/table/tbody/tr/td/form[1]/table[3]/tbody/tr/td/table/tbody/tr[{}]/td[9]')
layout = scrape('/html/body/table/tbody/tr/td/form[1]/table[3]/tbody/tr/td/table/tbody/tr[{}]/td[10]')
year_made = scrape('/html/body/table/tbody/tr/td/form[1]/table[3]/tbody/tr/td/table/tbody/tr[{}]/td[11]/div')
company_phone_number = scrape('/html/body/table/tbody/tr/td/form[1]/table[3]/tbody/tr/td/table/tbody/tr[{}]/td[12]')

#print(number)
#print(torihikijoutai)
#print(kakaku_kanri)
#print(price_per_size)
#print(location_name_floor)
#print(train_line)
#print(walk_time)
#print(layout)
#print(year_made)
#print(company_phone_number)


checkbox = reins.find_elements_by_name('bkknId1')
#print(checkbox)

counter = 1

#for clickable in checkbox:
#    clickable.click()
#    button = reins.find_element_by_xpath('/html/body/table/tbody/tr/td/form[1]/div[7]/input')
#    button.click()
#    pyautogui.hotkey('alt','s')
#    pyautogui.press('enter')
#    clickable.click()
#    time.sleep(5)
#    path = 'C:\\Users\\socom\\Downloads\\'
#    files = os.listdir(path)
#    sorted_files = sorted(files,key=lambda x:os.path.getctime('C:\\Users\\socom\\Downloads\\{}'.format(x)))
#    pdf = sorted_files[-1]
#    extension = '.pdf'
#    time.sleep(1)
#    os.rename(path + pdf, str(counter) + extension)
#    counter += 1
reins.close()
#
results = pd.DataFrame({
    'number':number,
    'torihikijoutai':torihikijoutai,
    'kakaku kanri':kakaku_kanri,
    'price per size': price_per_size,
    'location name floor':location_name_floor,
    'train line':train_line,
    'walk time':walk_time,
    'layout':layout,
    'year made':year_made,
    'company phone number':company_phone_number
        })

results.to_csv(filename,encoding='utf-8-sig')
