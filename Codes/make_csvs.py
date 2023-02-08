import numpy as np
import pandas as pd
path = './CSV_FOR_DATABASE'


cafe = pd.read_csv(f'{path}/Rates.csv')
# df_overal_rate = cafe[['rate']]
# df_overal_rate.replace('None',np.nan,inplace=True)
# df_overal_rate.dropna(inplace=True)
# df_overal_rate.to_csv(f'{path}/Overal_Rate.csv')
cafe.drop(columns=['cafe_id']).to_csv(f'{path}/Rates.csv',na_rep= None) 
