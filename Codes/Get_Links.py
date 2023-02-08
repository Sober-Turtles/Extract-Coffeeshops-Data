import requests
from bs4 import BeautifulSoup
import re
import warnings
warnings.filterwarnings('ignore')
import numpy as np

def find_cities(path = 'https://fidilio.com/', place_type = 'coffeeshops'):
    r = requests.get(f'{path}/{place_type}/')
    soup = BeautifulSoup(r.content, 'html.parser')
    s = soup.find('select', id = 'cityClass')
    options = s.find_all('option')
    cities = []
    for option in options:
        cities.append(option["value"])
    return list(set(cities))

def find_count_of_pages(city, path = 'https://fidilio.com/', place_type = 'coffeeshops'):
    r = requests.get(f'{path}/{place_type}/in/{city}')
    soup = BeautifulSoup(r.content, 'html.parser')
    s = soup.find('div', class_ = 'pagination')
    to_find = s.find_all('a')[-1]['href']
    count_of_pages = int(to_find[to_find.find('=')+1:len(to_find)])+1
    return count_of_pages

def find_links_of_city(city, page, path = 'https://fidilio.com' , place_type = 'coffeeshops'):
    r = requests.get(f'{path}/{place_type}/in/{city}/?p={page}')
    soup = BeautifulSoup(r.content, 'html.parser')
    s = soup.find('div', class_ = 'restaurant-list-container')
    places = s.find_all('a')
    links = []
    for place in places:
        link = place['href']
        links.append(f'{path}{link}')
    return links



cities = find_cities()
save_path = 'Links_by_City'
for city in cities:
    datas = []
    for i in range(find_count_of_pages(city)):
        links = find_links_of_city(city,i)
        for link in links:
            m = re.search('coffeeshops/(.+?)/', link)
            if m:
                name = m.group(1)
            else:
                name = ''
            x = {'City': city ,'Name': name ,'Link': link }
            datas.append(x)
    to_save = np.array(datas)
    np.save(f'{save_path}/{city}_links_names',to_save)

cities = np.array(cities)
np.save('All_cities',cities)