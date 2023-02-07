import numpy as np
import pandas as pd
import itertools 
import requests
from bs4 import BeautifulSoup
import re
import warnings
warnings.filterwarnings('ignore')

def get_data(link):
    r = requests.get(f'{link}')
    soup = BeautifulSoup(r.content, 'html.parser')
    s = soup.find('a', class_ = 'navigation-link')
    try:
        index = s['href'].rfind('=')+1
        location = s['href'][index:len(s['href'])].split(',')
    except TypeError:
        print(link)
        location = [np.nan,np.nan]
    return location


path = './CSV_FOR_DATABASE'
links = []
site = 'https://fidilio.com/'
place_type = 'coffeeshops'
city = 'tehran'
link_base = f'{site}/{place_type}'
df_location = pd.DataFrame(columns =['id','Name','Latitude','Longitude'])
df = pd.read_csv(f'{path}/Cafe.csv')
cafe_names = df['name_en']
for ind in df.index:
    name = df['name_en'][ind]
    link = f'{link_base}/{name}'
    latitude,longitude = get_data(link)
    df_location.loc[len(df_location)] = [ind,name,latitude,longitude]

df_location.dropna(inplace=True)
df_location.to_csv(f'{path}/location.csv')
df_location[237:].to_csv(f'{path}/location(tehran).csv')