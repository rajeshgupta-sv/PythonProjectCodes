from bs4 import BeautifulSoup
 
import urllib.request
import nltk
import matplotlib.pyplot
from nltk.corpus import stopwords

import datetime
now = datetime.datetime.now()

print ("Prog Started at :" + str(now))

F = open("TestFile.html","rt") 
#print (F.read()) 
 
#response = urllib.request.urlopen('http://php.net/')
#html = response.read()
 
html = F.read()


 
soup = BeautifulSoup(html,"lxml")
 
text = soup.get_text(strip=True)
 
tokens = [t for t in text.split()]
 
clean_tokens = tokens[:]
 
sr = stopwords.words('english')
 
for token in tokens:
 
    if token in stopwords.words('english'):
 
        clean_tokens.remove(token)
 
freq = nltk.FreqDist(clean_tokens)
 
for key,val in freq.items():
 
    print (str(key) + ':' + str(val))
  

now = datetime.datetime.now()  
print ("Prog Got Token Count at :" +str(now))


freq.plot(20, cumulative=False)


