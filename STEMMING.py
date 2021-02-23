import urllib.request
response=urllib.request.urlopen("https://en.wikipedia.org/wiki/SpaceX")
html=response.read()

from bs4 import BeautifulSoup
soup=BeautifulSoup(html,'html5lib')
text=soup.get_text(strip=True)

from nltk.stem import PorterStemmer

porter = PorterStemmer()

word_list=text
for w in word_list:
    print(porter.stem(w))