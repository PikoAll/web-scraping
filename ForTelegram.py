# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 18:59:44 2021

@author: peppi
"""

import requests
from bs4 import BeautifulSoup as bs

r = requests.get("https://www.ilmeteo.it/meteo/Roma") #r sara uguaale a tutta la pagina html del link
print(len(r.text))

contenuto=bs(r.text)
print('1\n',contenuto.title)        #per ottenere il titlono in html
print('2\n',contenuto.title.string)  #per ottenere stringa titolo

#per ottenere paragrafi e link della pagina
print('3')
print(contenuto.p)
print('4')
print(contenuto.a)

#per accedere a una cosa piu specifica
print('5')
print(contenuto.a["href"])

#per ottenere tutti i tag 'a'
for link in contenuto.findAll("a"):
    print(link.get("href"))
    
    
'''
Ora vediamo come ottenere un dato specifico da una pagina. Nella maggior parte dei casi vogliamo ottenere un dato
 proveniente da un tag specifico che abbia un id o classe specifica. Dopo aver ispezionato il sito di ilmeteo.it 
 possiamo vedere che le temperature della settimana sono presente all’interno di un tag “span” con classe = “temps”
'''


temps = contenuto.findAll("span", {"class": "tmax"})
for temp in temps:
    print(temp.text)