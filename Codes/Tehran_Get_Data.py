import requests
from bs4 import BeautifulSoup
import re
import warnings
warnings.filterwarnings('ignore')
import numpy as np
import pandas as pd

def get_data(link):
    r = requests.get(f'{link}')
    soup = BeautifulSoup(r.content, 'html.parser')
    try:
        try:
            persian_name = soup.select('h1')[0].text.strip()
        except AttributeError:
            persian_name = ''  
        try:
            informations = soup.find('div', class_ = 'informations-body').find_all('span', class_ = 'note')
        except AttributeError:
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


path = 'Links_by_City'
datas = np.load(f'{path}/tehran_links_names.npy',allow_pickle = True)
datas_splited = np.array_split(datas, 20)
save_path = 'CSVs_informations'
def get_tehran_data(batch_no, datas = datas_splited):
    city = 'tehran'
    df = pd.DataFrame(columns = ['Persian Name', 'Address', 'Phone Number', 'Is Open','Price_Class', 'Rate'])
    for data in datas[batch_no]:
        link = data['Link']
        name = data['Name']
#         city = data['City']
        df.loc[name] = get_data(link)
    df.to_csv(f'{save_path}/{city}_{batch_no+1}_info.csv') 
    
for i in range(0,20):
    get_tehran_data(1)