import re
import urllib.request
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/Artificial_intelligence'
try:
    pg = urllib.request.urlopen(url)
except:
    print('ERROR!')
S = BeautifulSoup(pg,'html.parser')
#print(pg.read())
#print(S)

expression = re.compile('^tocsection-')
contentlist = S.find_all('li',attrs = {'class':expression})
#print(contentlist)

content = []
for li in contentlist:
    content.append(li.getText().split('\n')[0])
#print(content)

expression0 = 'div-col columns column-width'
seealsolist = S.find('div', attrs = {'class':expression0})
seealsolist =  seealsolist.find_all('li')
#print(seealsolist)

seealso = []
for li in seealsolist:
    linktag = li.find('a',href = True, attrs = {'title':True,'class':False})
    if linktag:
        href = linktag['href']
        text = linktag.getText()
    seealso.append([href,text])
#print(seealso)

with open("SeeAlso.csv",'w') as file:
    for i in seealso:
        file.write(','.join(i) + '\n')
file0 = open("SeeAlso.csv",'r')
print(file0.read())
file.close()
file0.close()





