import warnings
warnings.filterwarnings('ignore')
import numpy as np
import pandas as pd

path = './CSVs_informations'

cities = np.load('All_cities.npy',allow_pickle = True)
cities = cities[cities != 'tehran']
hard_code = 'متاسفانه خطایی رخ داده است. در صورت تکرار لطفا از طریق صفحه تماس با ما مشکل را گزارش کنید'

for city in cities:
    df = pd.read_csv(f'{path}/{city}_info.csv', dtype = str)
    df.fillna('null',inplace = True)
    df_filtered = df[df['Persian Name'] == hard_code]
    df.drop(df_filtered.index[:], axis='index' ,inplace=True)
    df_filtered = df[df['Persian Name'] == hard_code]
    df.replace('', 60)
    df.rename(columns={'Unnamed: 0': 'Name'}, inplace=True)
    df.set_index('Name', inplace=True)
    df.to_csv(f'{path}/{city}_info.csv') 
    
    
city = 'tehran'

for i in range(1,21):
    df = pd.read_csv(f'{path}/{city}_{i}_info.csv', dtype = str)
    df.fillna('null',inplace = True)
    df_filtered = df[df['Persian Name'] == hard_code]
    df.drop(df_filtered.index[:], axis='index' ,inplace=True)
    df_filtered = df[df['Persian Name'] == hard_code]
    df.rename(columns={'Unnamed: 0': 'Name'}, inplace=True)
    df.set_index('Name', inplace=True)
    df.to_csv(f'{path}/{city}_{i}_info.csv')