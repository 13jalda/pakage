import inflection
import requests
from  bs4 import BeautifulSoup
page = requests.get('https://www.dailysmarty.com/topics/python')
soup = BeautifulSoup(page.text, 'html.parser')

titles = []
l_titles = []
for link in soup.find_all('h2'):
    for link2 in link.find_all('a'):
        titles.append(link2.get('href'))

for tit in titles:
    l_titles.append(inflection.titleize(tit[7:]))

print(l_titles)