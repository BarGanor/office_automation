import pandas as pd
import requests


id_dict = {'col_c':'624440', 'col_d': '79','col_e':'624477','col_f':'17',  'col_g':'78', 'col_h':'51317','col_j':'51315',
          'col_k':'51306','col_l':'51316', 'col_m':'51305', 'col_n':'51314', 'col_o':'51285','col_p':'99','col_s':'51297',
          'col_t':'51298', 'col_w':'624426', 'col_x':'624355', 'col_aa':['624350','624196'], 'col_ab':'624429', 'col_ac':'624427',
          'col_ad':'624430','col_ae':['624158','624153'], 'col_af':'624407','col_ag':'624431', 'col_ai':'624432', 'col_ak':'624433',
          'col_al':'624343','col_an':'624351', 'col_ao':'624324', 'col_ap':'624417','col_aq':'624419', 'col_ar':'624418',
          'col_as':'624416','col_at':['624417','624419'],'col_au':['624418','624416'],'col_ay': '11207', 'col_az':'11200'}


def get_col_data(url):
    resp = requests.get(url).json()
    data = resp['DataSet']['Series'][0]['obs']
    col = pd.DataFrame.from_records(data)
    col = col.set_index('TimePeriod')
    return col

def get_ft_data_monthly(record_num):
    print('Getting FT_Data')
    problem_getting = []
    df = pd.DataFrame()

    for series_id in id_dict.keys():
        try:

            if type(id_dict.get(series_id)) is str:

                url = 'https://apis.cbs.gov.il/series/data/list?id=' + id_dict.get(series_id) + '&format=json&download=false'
                col = get_col_data(url)

            elif type(id_dict.get(series_id)) is list:

                col = pd.DataFrame()
                for i in id_dict.get(series_id):
                    url = 'https://apis.cbs.gov.il/series/data/list?id=' + i + '&format=json&download=false'
                    col = get_col_data(url)

            else:
                col = pd.DataFrame({series_id: range(len(df))})

        except:
            problem_getting.append(id)
            col = pd.DataFrame({series_id: range(len(df))})

        df = pd.concat([df, col], axis=1)

    if len(problem_getting)>0:
        print('Had trouble getting the following columns: ' + str(problem_getting))
        
    df.columns = id_dict.keys()
    return df.iloc[:record_num]

#test