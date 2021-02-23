import urllib.request
response=urllib.request.urlopen("https://en.wikipedia.org/wiki/SpaceX")
html=response.read()
word_no_punc=[]

#print(html)

from bs4 import BeautifulSoup
soup=BeautifulSoup(html,'html5lib')
text=soup.get_text(strip=True)
#print(text)
from nltk import sent_tokenize,word_tokenize
sent_text=sent_tokenize(text)
word_text=word_tokenize(text)
print(len(sent_text))
#print(sent_text)
#print(len(word_text))
#print(word_text)
from nltk import FreqDist
#finding common words
#fdist=FreqDist(word_text)
#print(fdist)
#print(fdist.most_common(10))
#removing punctuation
for x in word_text:
    if x.isalpha():
        word_no_punc.append(x.lower())
print(word_no_punc)

#removing stopwords
from nltk.corpus import stopwords

stopword=stopwords.words("english")

print(stopword)
clean_words=[]
for w in word_no_punc:
    if w not in stopword:
        clean_words.append(w)
print(len(clean_words))