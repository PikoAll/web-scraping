# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 22:51:15 2021

@author: peppi
"""

import requests
from bs4 import BeautifulSoup as bs

def trovaFilm(nomeFilm):
    
    #https://altadefinizione.la/scrittore-per-caso-streaming/
    #https://altadefinizione.la/pazzo-per-lei-streaming-4k/
    ALTADEFINIZIONE='https://altadefinizione.la/'
    
    #https://cineblog01.bid/cb01-streaming/17055-le-morti-di-ian-stone-streaming-cb01.html
    #https://cineblog01.bid/cb01-streaming/17052-scooby-doo-la-spada-e-lo-scoob-streaming-cb01.html
    CINEBLOG='https://cineblog01.bid/cb01-streaming/'
    
    #https://www.ilgeniodellostreaming.icu/film/la-caccia-dei-lupi-2021-streaming/
    #https://www.ilgeniodellostreaming.icu/film/bar-giuseppe-2019-streaming/  # gli anni si possono provare con un incremento
    ILGENIO='https://www.ilgeniodellostreaming.icu/film/'
    
    
        
    nomeFilm=nomeFilm.replace(' ','-')
    count=0
    ############################################################################# AltaDefinizione
    print('1')
    try:
        
        link=ALTADEFINIZIONE+nomeFilm+'-streaming/'
        r = requests.get(link) 
        print(link)
        count=count+1
        
    except:
        x=0
        
    try:
        
        link=ALTADEFINIZIONE+nomeFilm+'-streaming-4K/'
        r = requests.get(link) 
        print(link)
        count=count+1
        
    except:
        x=0
        
    ####################### CINEBLOG
    '''
    print('2')
    for i in range(65000):
        link=CINEBLOG+str(i)+'-'+nomeFilm+'-streaming-cb01.html'
        print(i)
        try:
        
            r = requests.get(link) 
            print(link)
            count=count+1
        
        except:
            x=0
    '''
     ######################## IL GENIO DELLO STREAMIN
    print('3')
    i=1990
    while(i<2025):
       print(i)
       link=ILGENIO+nomeFilm+'-'+str(i)+'-streaming/'
        
       try:
        
            r = requests.get(link) 
            print(link)
            count=count+1
        
       except:
            x=0
       i=i+1
        
    print(count)

            
            
            
# da aggiustare il genio dello streaming
trovaFilm('rambo I')