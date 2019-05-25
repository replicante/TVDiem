#!/usr/bin/env python 
# -*- coding: utf-8 -*-
'''
Scrape release date of all the episodes of a Tv Series from IMDB
'''
from bs4 import BeautifulSoup
import requests
import json
from time import sleep

def show_name(url):
    url_get = requests.get(url)
    soup = BeautifulSoup(url_get.content, 'html.parser')
    name = (soup.find('title').text).split(' ', 1)[0]
    print(f'--Air date of {name} show:')
    
def show_date(url):    
    episodes = []
    dates = []
    try:
        for season in range(1,20):
            # if you follow The Simpsons maybe you want to increase the range or
            # use intertools for the loop
            r = requests.get(url, params={'season': season})
            soup = BeautifulSoup(r.text, 'html.parser')
            listing = soup.find('div', class_='eplist')
            for i, j in enumerate(listing.find_all('div', recursive=False)):
                episode = "{}.{}".format(season, i +1)
                date = j.find(class_='airdate')
                dates = date.get_text(strip=True)
                if dates == '':
                    break
                elif dates.isdigit() == False: 
                    episodes.append(episode)
                    print('Episode:', episode, '-- date:', dates)
                
    except (IndexError, ValueError):
        episode = 'null'

with open('titles.csv', 'r') as f:
    urls = [line.strip() for line in f]
for url in urls:
    show_name(''.join(url.split(',')[:-1]))
    show_date(''.join(url.split(',')[:-1]))
    sleep(10)
           
        



        

       
        

