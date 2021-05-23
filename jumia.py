import requests
from bs4 import BeautifulSoup
import pandas as pd

item = 'laptops'

r = requests.get(f'https://www.jumia.com.ng/{item}')
soup = BeautifulSoup(r.content, 'lxml')

all_products = []
products = soup.find_all('article', {'class', 'prd _fb col c-prd'})

for product in products:
    name = product.find("h3", {"class", "name"}).get_text()
    price = product.find("div", {"class", "prc"}).get_text()
    prod = {
        'Name': name,
        'Price': price
    }
    all_products.append(prod)

df = pd.DataFrame(all_products)
df.index += 1
df.to_excel(f"{item}.xlsx", index=False)
print("Done")
