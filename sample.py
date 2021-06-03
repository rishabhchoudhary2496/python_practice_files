from bs4 import BeautifulSoup
import requests;

import time
url = 'https://instagram.com/rishabh.2496'

r = requests.get(url)
rawText = r.text
soup = BeautifulSoup(rawText,'html.parser')
tags = (soup.find_all('body'))[0].find_all('script')
s=(str(tags[0])[52:-10])
print(s)











