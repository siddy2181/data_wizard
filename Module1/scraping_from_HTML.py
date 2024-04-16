from urllib.request import urlopen
from bs4 import BeautifulSoup

# Exercise 1: Scrape wikipedia The world's billionaires

# Step 2
wiki_link= "https://en.wikipedia.org/wiki/The_World%27s_Billionaires"
html_page= urlopen(wiki_link)
soup=BeautifulSoup(html_page)

# Step 3
billionaires= soup.find("table", class_="wikitable sortable")
t_body=billionaires.find("tbody")
print(t_body)

# Step 4
data_table = list()
tr_tags=t_body.find_all("tr")
count = 0

for row in tr_tags:
    if count == 0:
        cols = row.find_all("th")
        count+=1
        
    else:
        cols = row.find_all("td")

    cols= [elem.text.strip() for elem in cols]
    print(cols)
    data_table.append([elem for elem in cols if elem])
    print(data_table)