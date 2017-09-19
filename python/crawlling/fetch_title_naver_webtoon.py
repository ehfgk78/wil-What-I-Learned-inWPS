
from bs4 import BeautifulSoup as bs

try:
    f = open("./naverwebtoon.txt", 'rt')
        spoon = f.read()
except FileNotFoundError(e):
    print(e)
finally:
    f.close()

soup = bs(spoon, 'lxml')

#soup.select("td.title > a")

bslist = soup.find_all('td', 'title')
for item in bslist:
    print(item.a.get_text())
