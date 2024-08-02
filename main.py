import requests
from bs4 import BeautifulSoup
import urllib
url = "https://supersimple.dev/exercises/youtube"
r = requests.get(url)
bs = BeautifulSoup(r.content,'html.parser')
urls = bs.find_all('img', class_='thumbnail')
for Url in urls:
    print(url + str(Url['src']))
