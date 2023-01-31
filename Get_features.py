import requests
from bs4 import BeautifulSoup
import re
import warnings
warnings.filterwarnings('ignore')
import numpy as np
import pandas as pd
import json

def get_data(link):
    r = requests.get(f'{link}')
    soup = BeautifulSoup(r.content, 'html.parser')
    features = []
    try:
        features_raw = soup.find_all('span', class_ = 'feature-title')
        for feature_raw in (features_raw):
            features.append(feature_raw.text.strip())
    except AttributeError:
        pass
    return features

def get_tehran_data(batch_no, datas = datas_splited):
    city = 'tehran'
    city_based_features = {}
    for data in datas[batch_no]:
        name = data['Name']
        city_based_features[f'{name}'] = get_data(data['Link'])
        to_save = np.array(list(city_based_features.items()))
    np.save(f'{save_path}/{city}_{batch_no+1}_feature',to_save)
    
path = 'Links_by_City'
save_path = './Features_Numpy'
cities = np.load('All_cities.npy',allow_pickle = True)
cities = cities[cities != 'tehran']

for city in cities:
    datas = np.load(f'{path}/{city}_links_names.npy',allow_pickle = True)
    city_based_features = {}
    for data in datas:
        name = data['Name']
        city_based_features[f'{name}'] = get_data(data['Link'])
    to_save = np.array(list(city_based_features.items()))
    np.save(f'{save_path}/{city}_feature',to_save)

datas = np.load(f'{path}/tehran_links_names.npy',allow_pickle = True)
datas_splited = np.array_split(datas, 20)

for i in range(0,20):
    get_tehran_data(i)