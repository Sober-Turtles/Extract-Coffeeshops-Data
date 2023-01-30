import requests
from bs4 import BeautifulSoup
import re
import warnings
warnings.filterwarnings('ignore')
import numpy as np
import pandas as pd
import threading

def get_data(link):
    r = requests.get(f'{link}')
    soup = BeautifulSoup(r.content, 'html.parser')
    try:
        try:
            persian_name = soup.select('h1')[0].text.strip()
        except AttributeError:
            persian_name = ''  
        informations = soup.find_all('span', class_ = 'note')
        try:
            address = informations[0].text.strip()
        except IndexError:
            address = 'null'
        try:
            phone_number = informations[1].text.strip()
        except IndexError:
            phone_number = 'null'
        try:
            is_open_str = informations[2].text.strip()
            is_open = is_open_str[14:len(is_open_str)]
        except IndexError:
            is_open = 'null'
        price_class = len(soup.find_all('span', class_ = 'active'))
        try:
            rate = float(soup.find('span', property = 'ratingValue').text.strip())
        except AttributeError:
            rate = 'null'
        output = [persian_name,address,phone_number,is_open,price_class,rate]
    except IndexError:
        output = ['null','null','null','null','null','null']
    return output

def get_data_city(city,path = 'Links_by_City'):
    datas = np.load(f'{path}/{city}_links_names.npy',allow_pickle = True)
    df = pd.DataFrame(columns = ['Persian Name', 'Address', 'Phone Number', 'Is Open','Price_Class', 'Rate'])
    for data in datas:
        link = data['Link']
        name = data['Name']
#         city = data['City']
        df.loc[name] = get_data(link)
        get_data(link)
    return df

def for_threading(city):
    save_path = 'CSVs_informations2'
    get_data_city(city).to_csv(f'{save_path}/{city}_info.csv')
        

cities = np.load('All_cities.npy',allow_pickle = True)
t1 = threading.Thread(target=for_threading, args=(cities[0],))
t2 = threading.Thread(target=for_threading, args=(cities[1],))
t3 = threading.Thread(target=for_threading, args=(cities[2],))
t4 = threading.Thread(target=for_threading, args=(cities[3],))
t5 = threading.Thread(target=for_threading, args=(cities[4],))
t6 = threading.Thread(target=for_threading, args=(cities[5],))
t7 = threading.Thread(target=for_threading, args=(cities[6],))
t8 = threading.Thread(target=for_threading, args=(cities[7],))
t9 = threading.Thread(target=for_threading, args=(cities[8],))
t10 = threading.Thread(target=for_threading, args=(cities[9],))
t11 = threading.Thread(target=for_threading, args=(cities[10],))
t12 = threading.Thread(target=for_threading, args=(cities[11],))
t13 = threading.Thread(target=for_threading, args=(cities[12],))
t14 = threading.Thread(target=for_threading, args=(cities[13],))
t15 = threading.Thread(target=for_threading, args=(cities[14],))
t16 = threading.Thread(target=for_threading, args=(cities[15],))
t17 = threading.Thread(target=for_threading, args=(cities[16],))

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
t7.start()
t8.start()
t9.start()
t10.start()
t11.start()
t12.start()
t13.start()
t14.start()
t15.start()
t16.start()
t17.start()

t1.join()
t2.join()
t3.join()
t4.join()
t5.join()
t6.join()
t7.join()
t8.join()
t9.join()
t10.join()
t11.join()
t12.join()
t13.join()
t14.join()
t15.join()
t16.join()
t17.join()