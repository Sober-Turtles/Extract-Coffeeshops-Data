import requests
from bs4 import BeautifulSoup
import re
import warnings
warnings.filterwarnings('ignore')
import numpy as np
import pandas as pd
import json

def get_tehran_rate(batch_no, datas = datas_splited):
    df = pd.DataFrame(columns = ['Food', 'Servic', 'Worth(Price)', 'Design'])
    for data in datas[batch_no]:
        link = data['Link']
        name = data['Name']
        df.loc[name] = get_rate(link)
        df.to_csv(f'{save_path}/tehran_{batch_no+1}_rates.csv')   

def get_rate(link):
    r = requests.get(f'{link}')
    soup = BeautifulSoup(r.content, 'html.parser')
    features = []
    try:
        rate = float(soup.find('span', property = 'ratingValue').text.strip())
        s = soup.find('div', class_ = 'rate-body')
        rates = s.find_all('div', class_ = 'rate-it')
        try:
            food = rates[0]['data-rateit-value']
            servic = rates[1]['data-rateit-value']
            worth = rates[2]['data-rateit-value']
            design = rates[3]['data-rateit-value']
            output = [food,servic,worth,design]
        except IndexError:
            output = ['null','null','null','null']
        
    except AttributeError:
        output = ['null','null','null','null']
    return output


path = 'Links_by_City'
save_path = './Rates'
cities = np.load('All_cities.npy',allow_pickle = True)
cities = cities[cities != 'tehran']
for city in cities:
    datas = np.load(f'{path}/{city}_links_names.npy',allow_pickle = True)
    df = pd.DataFrame(columns = ['Food', 'Servic', 'Worth(Price)', 'Design'])
    for data in datas:
        link = data['Link']
        name = data['Name']
        df.loc[name] = get_rate(link)
        df.to_csv(f'{save_path}/{city}_rates.csv') 


datas = np.load(f'{path}/tehran_links_names.npy',allow_pickle = True)
datas_splited = np.array_split(datas, 20)

for i in range(0,20):
    get_tehran_rate(i)