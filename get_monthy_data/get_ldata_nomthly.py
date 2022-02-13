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
        print('problem getting col: C-J' + str(e))


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
        print('problem getting col: K-R' + str(e))


def cols_s_ldata():
    try:
        df = cols_k_to_r_ldata()['סה"כ'] - cols_k_to_r_ldata()['מזה: מגזר עסקי']
        df.name = 'סקטור שירותים ציבוריים'
        return df
    except Exception as e:
        print('problem getting col: S' + str(e))


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
        print('problem getting col: X-BA' + str(e))


def col_bf_ldata():
    try:
        url = 'https://fred.stlouisfed.org/graph/fredgraph.csv?bgcolor=%23e1e9f0&chart_type=line&drp=0&fo=open%20sans&graph_bgcolor=%23ffffff&height=450&mode=fred&recession_bars=off&txtcolor=%23444444&ts=12&tts=12&width=1168&nt=0&thu=0&trc=0&show_legend=yes&show_axis_titles=yes&show_tooltip=yes&id=LRHUTTTTEZM156S&scale=left&cosd=2020-10-01&coed=2021-10-01&line_color=%234572a7&link_values=false&line_style=solid&mark_type=none&mw=3&lw=2&ost=-99999&oet=99999&mma=0&fml=a&fq=Monthly&fam=avg&fgst=lin&fgsnd=2020-02-01&line_index=1&transformation=lin&vintage_date=2022-01-16&revision_date=2022-01-16&nd=1990-07-01.csv'
        df = pd.read_csv(url, index_col=0)
        df.index = pd.to_datetime(df.index)
        df.index = df.index.strftime('%m/%Y')
        df.columns = ['שיעור אבטלה בגוש האירו']

        return df
    except Exception as e:
        print('problem getting cols: BF' + str(e))


def col_bg_ldata():
    try:
        url = 'https://data.bls.gov/timeseries/LNS14000000'
        resp = requests.get(url)
        soup = BeautifulSoup(resp.content.decode('utf-8'), features='lxml')
        table = soup.find("table", {"class": 'regular-data'}).prettify()
        df = pd.read_html(table, index_col=0)[0].dropna( how='all')
        df2_index = df.index
        df2 = df.iloc[-2:-1,:].transpose()
        df = df.iloc[-1:,:].transpose()
        df2.index = [f"{i} {df2_index[-2]}" for i in df2.index]
        df.index = [f"{i} {df2_index[-1]}" for i in df.index]
        df2.columns = df.columns
        df = pd.concat([df2, df], axis=0)
        df.index = pd.to_datetime(df.index)
        df.index = df.index.strftime('%m/%Y')
        df.columns = ["שיעור אבטלה בארה'ב"]

        return df
    except Exception as e:
        print('problem getting cols: BG' + str(e))


def col_bh_to_by_ldata():
    try:
        today = datetime(date.today().year, date.today().month, date.today().day).strftime('%d/%m/%Y')
        dtObj = datetime.strptime(today, '%d/%m/%Y')
        index_col = [(dtObj - relativedelta(months=i)).date() for i in range(1,30,1)]
        df = pd.DataFrame(columns=[ "ציבורי","עסקי","סה'כ","ציבורי","עסקי","סה'כ" ,"ציבורי","עסקי","סה'כ","מנוכה עונתיות","מקורי","תביעות חדשות","תביעות מתמשכות","סה'כ","תביעות חדשות","תביעות ממשיכות","סה'כ"], index=index_col)
        df = df.fillna("").sort_index()
        df.index = pd.to_datetime(df.index).strftime('%m/%Y')
        return df
    except Exception as e:
        print('problem getting col: BH-BY' + str(e))


def cols_bz_ldata():
    try:
            url = f'https://apis.cbs.gov.il/series/data/list?id=91018&format=json&download=false'
            resp = requests.get(url).json()
            data = resp['DataSet']['Series'][0]['obs']
            col = pd.DataFrame.from_records(data)
            col = col.set_index('TimePeriod')
            col.index = pd.to_datetime(col.index)
            col = col.sort_index()
            col.index = col.index.strftime('%m/%Y')
            col.columns = {'value': 'משרות פנויות (אלפים)'}
            return col
    except Exception as e:
        print('problem getting col: BZ' + str(e))


def cols_ca_ldata():
    try:
        url = f'https://apis.cbs.gov.il/series/data/list?id=91018&format=json&download=false'
        resp = requests.get(url).json()
        data = resp['DataSet']['Series'][0]['obs']
        col = pd.DataFrame.from_records(data)
        col = col.set_index('TimePeriod')
        col.index = pd.to_datetime(col.index)
        col = col.sort_index()
        col.index = col.index.strftime('%m/%Y')
        col.columns = {'value': 'סהכ משרות = מועסקים (מנוכה עונתיות)+ משרות'}

        url1 = f'https://apis.cbs.gov.il/series/data/list?id=41089&format=json&download=false'
        resp1 = requests.get(url1).json()
        data1 = resp1['DataSet']['Series'][0]['obs']
        col1 = pd.DataFrame.from_records(data1)
        col1 = col1.set_index('TimePeriod')
        col1.index = pd.to_datetime(col1.index)
        col1 = col1.sort_index()
        col1.index = col1.index.strftime('%m/%Y')
        col1.columns = col.columns

        df = col1.add(col, fill_value=0)

        return df
    except Exception as e:
        print('problem getting col: CA' + str(e))


def cols_cb_to_cg_ldata():
    try:
        series_id = {'col_cb': '613067', 'col_cc': '613048', 'col_cd': '613010', 'col_ce': '613384',
                     'col_cf': '613346', 'col_cg': '613232'}
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
        df.columns = ['col_cb', 'col_cc', 'col_cd', 'col_ce',
                     'col_cf', 'col_cg']
        return df
    except Exception as e:
        print('problem getting col: CB-CG' + str(e))


def cols_ch_to_cu_ldata():
    try:
        series_id = {'col_ch': '47682', 'col_ci': '47650', 'col_cj': '47673', 'col_ck': '47641',
                     'col_cl': '47675', 'col_cm': '47643',
                     'col_cn': '47676', 'col_co': '47644', 'col_cp': '47677', 'col_cq': '47645',
                     'col_cr': '47686', 'col_cs': '47654', 'col_ct': '47687', 'col_cu': '47655'}
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
        df.columns = ['col_ch', 'col_ci', 'col_cj', 'col_ck',
                     'col_cl', 'col_cm',
                     'col_cn', 'col_co', 'col_cp', 'col_cq',
                     'col_cr', 'col_cs', 'col_ct', 'col_cu']
        return df
    except Exception as e:
        print('problem getting col: CH-CU' + str(e))


def col_cv_to_cx_ldata():
    try:
        today = datetime(date.today().year, date.today().month, date.today().day).strftime('%d/%m/%Y')
        dtObj = datetime.strptime(today, '%d/%m/%Y')
        index_col = [(dtObj - relativedelta(months=i)).date() for i in range(1,30,1)]
        df = pd.DataFrame(columns=[ "חיפשו עבודה בהמשך","לא עבדו ב-12 החודשים (מקורי)","לא עבדו ב-12 החודשים (מנוכה)"], index=index_col)
        df = df.fillna("").sort_index()
        df.index = pd.to_datetime(df.index).strftime('%m/%Y')
        return df
    except Exception as e:
        print('problem getting col: CV-CX' + str(e))