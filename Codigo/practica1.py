# -*- coding: utf-8 -*-
""" Editor de Spyder

pd.read

"""
import requests
from bs4 import BeautifulSoup

'url_a_scrapear= 'https://www.sindicom.gva.es/va/badespav1'
url_a_scrapear='https://www.volcanodiscovery.com'
'url_a_scrapear='https://en.wikipedia.org/wiki/Python_(programming_language)'

'Página con la que vamos a trabajar'
req = requests.get(url_a_scrapear)

'En soup tengo toda la página web'
soup=BeautifulSoup(req.content, features="lxml")

tags= soup('a')

for tag in tags:
    print (tag.name)
    print (tag.get('href'))
    print (tag.get('target'))
    print('-------------')

tags= soup ('a')

table=soup.find('table')
currentIndex=0
for row in table.findAll("tr"):
    cells=row.findAll("td")
    if (currentIndex>0)
    
    
tags.name

for tag in tags:
    print (tag.lang)
    print (tag.style)
    print('-------------')


'Título de la página'
print(soup.title)
print(soup.title.name)
print (soup.title.string)

soup.p
soup.body

soup.h2['class']
soup.h2.attrs
'Todas las entradas con etiqueta h2'
for sub_heading in soup.find_all('h2'):
    print (sub_heading.text)
    print (sub_heading.content)

for child in soup.h2.children:
    print (child.name)

'COntinuar en "son útiles sólo cuando quieres accedea los descendientes directos de
'la página 'https://code.tutsplus.com/es/tutorials/scraping-webpages-in-python-with-beautiful-soup-the-basics--cms-28211

print(soup.p.parent.name)

for parent in soup.p.parents:
    print(parent.name)
    
soup.h1
soup.h2
soup.a
soup.p

for child in soup.p.children:
    print (child.name)