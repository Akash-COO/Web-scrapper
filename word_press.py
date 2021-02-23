import urllib.request
response=urllib.request.urlopen("https://en.wikipedia.org/wiki/SpaceX")
html=response.read()
word_no_punc=[]

from bs4 import BeautifulSoup
soup=BeautifulSoup(html,'html5lib')
text=soup.get_text(strip=True)

from wordcloud import WordCloud
import matplotlib.pyplot as plt

wordcloud=WordCloud().generate(text)

plt.figure(figsize=(12,12))
plt.imshow(wordcloud)

plt.axis("off")
plt.show()