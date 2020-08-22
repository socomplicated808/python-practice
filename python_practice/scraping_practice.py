from bs4 import BeautifulSoup
import requests
import pandas as pd


titles = []
prices = []
i = 1
filename = "results.csv"

try:
    while i <= 5:
        url = "https://www.ebay.com/sch/i.html?_from=R40&_nkw=pokemon&_sacat=0&_pgn=" + str(i)
        print("getting data from " + url)

        contents = requests.get(url)

        soup = BeautifulSoup(contents.content,'html.parser')

        for item in  soup.find_all('h3',class_ = 's-item__title'):
            titles.append(item.get_text().replace("New Listing",""))

        for item in soup.find_all('span',class_='s-item__price'):
            prices.append(item.get_text())
        i += 1
except:
    print("Reached the last page")

print("Generating csv file")
results = pd.DataFrame(
        {
    'Title':titles,
    'Price':prices,
            }
        )

#print(results)


results.to_csv(filename)
print(filename + " was generated")
