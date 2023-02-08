import numpy as np
import pandas as pd
import itertools 
import requests
from bs4 import BeautifulSoup
import re
import warnings
warnings.filterwarnings('ignore')

def get_data(link):
    link = 'https://fidilio.com/coffeeshops/lavan'
    r = requests.get(f'{link}')
    soup = BeautifulSoup(r.content, 'html.parser')
    s = soup.find_all('div', class_ = 'overview')
    try:
        reviwes = re.findall(r'\d+',str(s))
    except:
        print(link)
        reviwes = [np.nan,np.nan,np.nan,np.nan,np.nan]
    return reviwes

path = './CSV_FOR_DATABASE'
site = 'https://fidilio.com/'
place_type = 'coffeeshops'
# city = 'tehran'
link_base = f'{site}/{place_type}'
df_reviwes = pd.DataFrame(columns =['id','Name','Perfect','Good','Ok','Bad','Very Bad'])
df = pd.read_csv(f'{path}/Cafe.csv')
for ind in df.index:
    name = df['name_en'][ind]
    link = f'{link_base}/{name}'
    reviews = get_data(link)
    try:
        df_reviwes.loc[len(df_reviwes)] = [ind,name,reviews[0],reviews[1],reviews[2],reviews[3],reviews[4]]
    except: 
        print(link)

df_reviwes.to_csv(f'{path}/reviews.csv')
df_reviwes[237:].to_csv(f'{path}/reviews(tehran).csv')