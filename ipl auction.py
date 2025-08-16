import requests
from bs4 import BeautifulSoup 
import re
import pandas as pd
url = "https://www.iplt20.com/auction/2024"
r = requests.get(url=url)
soup = BeautifulSoup(markup=r.content,features='lxml')
ind = 1
headers = soup.find_all(name='tr',class_='ih-pt-tbl')[ind]
table_headers = []
for i in headers:
    table_headers.append(i.string)
table_headers = list(filter(lambda x: x if x != '\n' else False,table_headers))
body:BeautifulSoup = soup.find_all(name='tbody',id='pointsdata')[ind]
rows = body.find_all(name='tr')
table_rows = []
for i in rows:
    a = []
    # a.append(i.find('h2').text)
    for j in i.find_all('td'):
        a.append(str(j.text).replace("\n",''))   
    table_rows.append(a)
df = pd.DataFrame(columns=table_headers)
for i in range(len(table_rows)):
    df.loc[i] = table_rows[i]
print(df)
df.to_excel(r"Z:\\web scraping.xlsx",index=False)