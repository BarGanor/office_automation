import requests
import pandas as pd
from datetime import datetime, date, timedelta
from bs4 import BeautifulSoup
from dateutil.relativedelta import relativedelta
import time
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)


def cols_c_to_j_ldata():
    try:
        url = 'https://www.boi.org.il/he/DataAndStatistics/Lists/BoiTablesAndGraphs/heb_g06a.xls'
        resp = requests.get(url)
        df = pd.read_excel(resp.content, sheet_name='לוח ז-6 (1)', header=5, index_col=0)
        df = df.loc['נתונים חודשיים מקוריים': 'נתונים חודשיים מנוכי עונתיות'].dropna(how='all')
        df = df.loc[:,
             ['שירותים ציבוריים.1', 'מגזר עסקי.1', 'סה"כ.2', 'שירותים ציבוריים', 'מגזר עסקי', 'סה"כ.1', 'מזה: מגזר עסקי',
              'סה"כ']]
        df.index = pd.to_datetime(df.index)
        df = df.sort_index()
        df.index = df.index.strftime('%m/%Y')
        return df

    except Exception as e:
        print('problem getting col: C-J')


def cols_k_to_r_ldata():
    try:
        url = 'https://www.boi.org.il/he/DataAndStatistics/Lists/BoiTablesAndGraphs/heb_g06a.xls'
        resp = requests.get(url)
        df = pd.read_excel(resp.content, sheet_name='לוח ז-6 (1)', header=5, index_col=0)
        df = df.loc['נתונים חודשיים מנוכי עונתיות': 'השינוי באחוזים לעומת השנה הקודמת'].dropna(how='all')
        df = df.loc[:,
             ['שירותים ציבוריים.1', 'מגזר עסקי.1', 'סה"כ.2', 'שירותים ציבוריים', 'מגזר עסקי', 'סה"כ.1', 'מזה: מגזר עסקי',
              'סה"כ']]
        df.index = pd.to_datetime(df.index)
        df = df.sort_index()
        df.index = df.index.strftime('%m/%Y')
        return df

    except Exception as e:
        print('problem getting col: K-R')


def cols_x_to_ba_ldata():
    try:
        series_id = {'col_x': '40000', 'col_y': '40001', 'col_z': '40003', 'col_aa': '40005',
                     'col_ab': '40013', 'col_ac': '40009',
                     'col_ad': '40392', 'col_ae': '40051', 'col_af': '40053', 'col_ag': '41087',
                     'col_ah': '41089', 'col_ai': '41091', 'col_aj': '41097', 'col_ak': '41093',
                     'col_al': '41321', 'col_am': '41125', 'col_an': '41127', 'col_ao': '40341',
                     'col_ap': '40342', 'col_aq': '40344',
                     'col_ar': '40346', 'col_as': '40354', 'col_at': '40350', 'col_au': '40398',
                     'col_av': '41285', 'col_aw': '41287', 'col_ax': '41289', 'col_ay': '41295',
                     'col_az': '41291', 'col_ba': '41327'}
        df = pd.DataFrame()
        for id in series_id.keys():
            url = f'https://apis.cbs.gov.il/series/data/list?id={series_id.get(id)}&format=json&download=false'
            resp = requests.get(url).json()
            data = resp['DataSet']['Series'][0]['obs']
            col = pd.DataFrame.from_records(data)
            col = col.set_index('TimePeriod')
            col.index = pd.to_datetime(col.index)
            col = col.sort_index()
            col.index = col.index.strftime('%m/%Y')
            df = pd.concat([df, col], axis=1)
        df.columns = ['col_x', 'col_y', 'col_z', 'col_aa',
                     'col_ab', 'col_ac',
                     'col_ad', 'col_ae', 'col_af', 'col_ag',
                     'col_ah', 'col_ai', 'col_aj', 'col_ak',
                     'col_al', 'col_am', 'col_an', 'col_ao',
                     'col_ap', 'col_aq',
                     'col_ar', 'col_as', 'col_at', 'col_au',
                     'col_av', 'col_aw', 'col_ax', 'col_ay',
                     'col_az', 'col_ba']
        return df
    except Exception as e:
        print('problem getting col: X-BA')