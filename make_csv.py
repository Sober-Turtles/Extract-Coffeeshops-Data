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

df_cafe = pd.DataFrame(columns = ['name_en', 'name_fa','address_id','city_id','price_class','rate'])
df_address = pd.DataFrame(columns = ['detail'])
df_phone = pd.DataFrame(columns=['phone_number'])
df_city = pd.DataFrame(columns=['name'])

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

                df_cafe.loc[len(df_cafe.index)] = [df_features_cafe['Name'][ind],
                                                    df_features_cafe['Persian Name'][ind],
                                                    len(df_cafe.index),city_id,df_features_cafe['Price_Class'][ind],
                                                    df_features_cafe['Rate'][ind]]

                df_address.loc[len(df_address.index)] = [df_features_cafe['Address'][ind]]
                df_phone.loc[len(df_phone.index)] = [df_features_cafe['Phone Number'][ind]]

    else:
        df_city.loc[len(df_city.index)] = [city]

        df_features_cafe = pd.read_csv(f'{path}/{city}_info.csv', dtype = {'Phone Number' : str})
        df_features_cafe.rename(columns={'Unnamed: 0': 'Name'}, inplace=True)
        for ind in df_features_cafe.index:
            city_dict.update({df_features_cafe['Name'][ind]:len(df_cafe.index)})
            df_cafe.loc[len(df_cafe.index)] = [df_features_cafe['Name'][ind],
                                                df_features_cafe['Persian Name'][ind],
                                                len(df_cafe.index),
                                                city_id,df_features_cafe['Price_Class'][ind],
                                                df_features_cafe['Rate'][ind]]

            df_address.loc[len(df_address.index)] = [df_features_cafe['Address'][ind]]
            df_phone.loc[len(df_phone.index)] = [df_features_cafe['Phone Number'][ind]]
    

df_cafe.to_csv(f'{save_path}/Cafe.csv') 
df_address.to_csv(f'{save_path}/Address.csv')    
df_phone.to_csv(f'{save_path}/Phone_number.csv') 
df_city.to_csv(f'{save_path}/City.csv') 

#___FEATURES 

features_tabel,features_dict = make_features()
features_tabel.to_csv(f'{save_path}/Features.csv') 

df_features_cafe = pd.DataFrame(columns = ['cafe_name', 'feature_id'])
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

df_features_cafe.to_csv(f'{save_path}/Features_Cafe.csv') 

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
                    df_rate.loc[len(df_rate.index)] = [datas_rate['Food'][ind],
                                                        datas_rate['Servic'][ind],
                                                        datas_rate['Worth(Price)'][ind],
                                                        datas_rate['Design'][ind]] 

    else:
        datas_rate = pd.read_csv(f'{path}/{city}_rates.csv')
        datas_rate.rename(columns={'Unnamed: 0': 'Name'}, inplace=True)

        for ind in datas_rate.index:
            if datas_rate['Name'][ind] in exist_names:
                df_rate.loc[len(df_rate.index)] = [datas_rate['Food'][ind],
                                                    datas_rate['Servic'][ind],
                                                    datas_rate['Worth(Price)'][ind],
                                                    datas_rate['Design'][ind]] 

                
df_rate.to_csv(f'{save_path}/Rates.csv') 