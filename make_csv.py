import numpy as np
import pandas as pd
import itertools 

def make_features():
    path = './Features_Numpy'
    cities = np.load('All_cities.npy',allow_pickle = True)
    x = []
    names = []
    for city in cities:
        if city == 'tehran':
            for i in range(0,20):
                datas = np.load(f'{path}/{city}_{i+1}_feature.npy',allow_pickle = True)
                for data in datas:
                    x.append(data[1])
        else:
            datas = np.load(f'{path}/{city}_feature.npy',allow_pickle = True)
            for data in datas:
                x.append(data[1])
        # x.append(array[1])

    features = set(list(itertools.chain.from_iterable(x)))

    features_tabel = pd.DataFrame(features,columns= ['feature_name'])

    features_dict = {}
    i = 0
    for feature in features:
        features_dict.update({feature : i})
        i = i+1

    return features_tabel,features_dict


cities = np.load('All_cities.npy',allow_pickle = True)

#___INFORMATIONS

df_cafe = pd.DataFrame(columns = ['name_en', 'name_fa','city_id','price_class','rate'])
df_address = pd.DataFrame(columns = ['city_id','detail'])
df_phone = pd.DataFrame(columns=['phone_number'])
df_city = pd.DataFrame(columns=['name'])
df_is_open = pd.DataFrame(columns=['cafe_id','open','close'])

save_path = './CSV_FOR_DATABASE'
path = './CSVs_informations'

city_dict = {}
for city in cities:
    city_id = int(np.where(cities == city)[0])
    if city == 'tehran':
        df_city.loc[len(df_city.index)] = [city]
        for i in range(0,20):
            df_features_cafe = pd.read_csv(f'{path}/{city}_{i+1}_info.csv', dtype = {'Phone Number' : str})
            df_features_cafe.rename(columns={'Unnamed: 0': 'Name'}, inplace=True)

            for ind in df_features_cafe.index:
                city_dict.update({df_features_cafe['Name'][ind]:len(df_cafe.index)})

                if df_features_cafe['Address'][ind]:
                    df_address.loc[len(df_address.index)] = [city_id,df_features_cafe['Address'][ind]]

                if df_features_cafe['Phone Number'][ind]:
                    df_phone.loc[len(df_phone.index)] = [df_features_cafe['Phone Number'][ind]]

                if df_features_cafe['Is Open'][ind] != np.nan:
                    for i in str(df_features_cafe['Is Open'][ind]).split('/'):
                        df_is_open['cafe_id'][len(df_is_open.index)] = len(df_cafe.index)
                        time = str(i).split('-')
                        try :
                            df_is_open.loc[len(df_is_open.index)] = [len(df_cafe.index), time[0], time[1]]
                        except IndexError:
                            pass

                df_cafe.loc[len(df_cafe.index)] = [df_features_cafe['Name'][ind],
                                        df_features_cafe['Persian Name'][ind],
                                        city_id,df_features_cafe['Price_Class'][ind],
                                        df_features_cafe['Rate'][ind]]

    else:
        df_city.loc[len(df_city.index)] = [city]

        df_features_cafe = pd.read_csv(f'{path}/{city}_info.csv', dtype = {'Phone Number' : str})
        df_features_cafe.rename(columns={'Unnamed: 0': 'Name'}, inplace=True)
        for ind in df_features_cafe.index:
            city_dict.update({df_features_cafe['Name'][ind]:len(df_cafe.index)})

            if df_features_cafe['Address'][ind] != np.nan:
                df_address.loc[len(df_address.index)] = [city_id,df_features_cafe['Address'][ind]]

            if df_features_cafe['Phone Number'][ind] != np.nan:
                df_phone.loc[len(df_phone.index)] = [df_features_cafe['Phone Number'][ind]]

            if df_features_cafe['Is Open'][ind] != np.nan:
                    for i in str(df_features_cafe['Is Open'][ind]).split('/'):
                        time = str(i).split('-')
                        try :
                            df_is_open.loc[len(df_is_open.index)] = [len(df_cafe.index), time[0], time[1]]
                        except IndexError:
                            pass

            df_cafe.loc[len(df_cafe.index)] = [df_features_cafe['Name'][ind],
                                    df_features_cafe['Persian Name'][ind],
                                    city_id,df_features_cafe['Price_Class'][ind],
                                    df_features_cafe['Rate'][ind]]
    
df_address = df_address.dropna()
df_phone = df_phone.dropna()
df_is_open = df_is_open.dropna()


for ind in df_is_open.index:
    if ':' not in df_is_open['open'][ind]:
        df_is_open['open'][ind] =  str(df_is_open['open'][ind]) + ':00'
    if ':' not in df_is_open['close'][ind]:
        df_is_open['close'][ind] =  str(df_is_open['close'][ind]) + ':00'

df_cafe.drop(columns=['rate']).to_csv(f'{save_path}/Cafe.csv',na_rep= None) 
df_address.to_csv(f'{save_path}/Address.csv',na_rep= None)    
df_phone.to_csv(f'{save_path}/Phone_number.csv',na_rep= None) 
df_is_open.to_csv(f'{save_path}/Time_table.csv',na_rep= None)
df_city.to_csv(f'{save_path}/City.csv') 

#___FEATURES 

features_tabel,features_dict = make_features()
features_tabel.to_csv(f'{save_path}/Features.csv') 

df_features_cafe = pd.DataFrame(columns = ['cafe_id', 'feature_id'])
path = './Features_Numpy'

for city in cities:
    if city == 'tehran':
        for i in range(0,20):
            path = './Features_Numpy'
            datas_feature = np.load(f'{path}/{city}_{i+1}_feature.npy',allow_pickle=True)
            for data in datas_feature:
                for feature in data[1]:
                    try:
                        df_features_cafe.loc[len(df_features_cafe.index)] = [city_dict[data[0]],
                                                                            features_dict[feature]] 
                    except KeyError:
                        pass

    else:
        datas_feature = np.load(f'{path}/{city}_feature.npy',allow_pickle= True)
        for data in datas_feature:
            for feature in data[1]:
                try:
                    df_features_cafe.loc[len(df_features_cafe.index)] = [city_dict[data[0]],
                                                                        features_dict[feature]] 
                except KeyError:
                    pass

# df_features_cafe = df_features_cafe.astype(object).where(pd.notnull(df_features_cafe), None)
df_features_cafe.to_csv(f'{save_path}/Features_Cafe.csv',na_rep= None) 

#__RATE

exist_names = np.array(df_cafe['name_en'])
path = './Rates'
df_rate = pd.DataFrame(columns=['food_rate','servic_rate','worth','design_rate'])
for city in cities:
    if city == 'tehran':
        for i in range(0,20):
            path = './Rates'
            datas_rate = pd.read_csv(f'{path}/{city}_{i+1}_rates.csv')
            datas_rate.rename(columns={'Unnamed: 0': 'Name'}, inplace=True)

            for ind in datas_rate.index:
                if datas_rate['Name'][ind] in exist_names:
                    cafe_id = len(df_rate.index)
                    # if (datas_rate['Food'][ind] != np.nan 
                    #             and datas_rate['Servic'][ind] != np.nan
                    #             and datas_rate['Worth(Price)'][ind] != np.nan
                    #             and datas_rate['Design'][ind] != np.nan ):
                    df_rate.loc[len(df_rate.index)] = [datas_rate['Food'][ind],
                                                        datas_rate['Servic'][ind],
                                                        datas_rate['Worth(Price)'][ind],
                                                        datas_rate['Design'][ind]]

    else:
        datas_rate = pd.read_csv(f'{path}/{city}_rates.csv')
        datas_rate.rename(columns={'Unnamed: 0': 'Name'}, inplace=True)

        for ind in datas_rate.index:
            if datas_rate['Name'][ind] in exist_names:
                cafe_id = len(df_rate.index)
                # if (datas_rate['Food'][ind] != np.nan 
                #             and datas_rate['Servic'][ind] != np.nan
                #             and datas_rate['Worth(Price)'][ind] != np.nan
                #             and datas_rate['Design'][ind] != np.nan ):
                df_rate.loc[len(df_rate.index)] = [datas_rate['Food'][ind],
                                                    datas_rate['Servic'][ind],
                                                    datas_rate['Worth(Price)'][ind],
                                                    datas_rate['Design'][ind]]

df_overal_rate = df_cafe[['rate']]
df_overal_rate.replace('None',np.nan,inplace=True)
df_overal_rate.dropna(inplace=True)
df_rate.dropna(inplace=True)

df_rate.to_csv(f'{save_path}/Rates.csv',na_rep= None) 
