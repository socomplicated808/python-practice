from selenium import webdriver
import pandas as pd

filename = 'results.csv'
titles = []
prices = []

ebay = webdriver.Firefox()
ebay.get ("https://www.ebay.com/")
search_bar = ebay.find_element_by_xpath('//input[@id="gh-ac"]')
search_bar.send_keys("pokemon")
search_button = ebay.find_element_by_xpath('//input[@id="gh-btn"]')
search_button.click()
url = ebay.current_url


titles_elements = ebay.find_elements_by_class_name("s-item__title")
prices_elements = ebay.find_elements_by_class_name("s-item__price")

for element in titles_elements:
    titles.append(element.text.encode('cp932','ignore'))

for element in prices_elements:
    prices.append(element.text)

#print(titles)
#print(prices)
results = pd.DataFrame({
    'Title':titles,
    'Price':prices,
    })

results.to_csv(filename)
print(filename + " was generated.")

ebay.close()
