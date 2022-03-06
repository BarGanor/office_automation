import requests
import pandas as pd
from datetime import datetime, date, timedelta
from bs4 import BeautifulSoup
from dateutil.relativedelta import relativedelta
import string
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)


def cols_g_to_t_pdata():
    try:
        series_id = {'col_g': '120010', 'col_h': '120040', 'col_i': '120020', 'col_j': '120030',
                     'col_k': '120450', 'col_l': '120520','col_m': '120660','col_n': '120850','col_o': '121050'
                    ,'col_p': '121230'
                    ,'col_q': '121320','col_r': '121430','col_s': '120050','col_t': '120043'}
        df = pd.DataFrame()
        for id in series_id.keys():
            url = f'https://api.cbs.gov.il/index/data/price?id={series_id.get(id)}&format=json&download=false'
            resp = requests.get(url).json()
            data = resp['month'][0]['date']
            col = pd.DataFrame.from_records(data)
            col['E'] = col['currBase'].apply(pd.Series).value
            col['Date'] =  col['month'].map(str) + '/' + col['year'].map(str)
            col = col[['Date','E']]
            col = col.set_index('Date')

            col.index = pd.to_datetime(col.index)
            col = col.sort_index()
            col.index = col.index.strftime('%m/%Y')
            df = pd.concat([df, col], axis=1)
        df.columns = ['מדד המחירים לצרכן-כללי(מקור)', 'מדד לצרכן- ירקות ופירות', 'מדד מחירים לצרכן - ללא ירקות ופירות', 'מדד לצרכן - מדד המחירים לצרכן - המדד הכללי ללא ירקות ופירות וללא דיור',
                     'מדד לצרכן - דיור', 'מדד לצרכן - אחזקת הדירה','מדד לצרכן - ריהוט וציוד לבית','מדד לצרכן - הלבשה והנעלה','מדד לצרכן - חינוך, תרבות ובידור','מדד לצרכן - בריאות'
                    ,'מדד לצרכן - תחבורה ותקשורת','מדד לצרכן - שונות','מדד לצרכן - מזון ללא ירקות ופירות','מדד לצרכן - ירקות ופירות - פירות טריים']
        return df
    except Exception as e:
        print('problem getting col: G-T ' + str(e))


# Empty columns
def cols_u_to_v_pdata():
    try:
        today = datetime(date.today().year, date.today().month,
                                 date.today().day).strftime('%m/%Y')
        dtObj = datetime.strptime(today, '%m/%Y')
        index_col = [(dtObj - relativedelta(months=i)).date() for i in range(1, 30, 1)]
        cols_name = []
        for first_char in string.ascii_uppercase:
            if first_char <= 'V' and first_char >= 'U':
                cols_name.append(first_char)

        df = pd.DataFrame(columns=cols_name, index=index_col)
        df = df.fillna("").sort_index()
        df.index = pd.to_datetime(df.index).strftime('%m/%Y')
        return df
    except Exception as e:
        print('problem getting col: U-V' + str(e))


def col_aa_pdata():
    try:
        url = 'https://beta.bls.gov/dataViewer/view/timeseries/CUSR0000SA0'
        resp = requests.get(url)
        soup = BeautifulSoup(resp.content.decode('utf-8'), features='lxml')
        table = soup.find("table", {"id": 'seriesDataTable1'}).prettify()
        df = pd.read_html(table, index_col=0)[0].dropna( how='all')
        df['date'] = df['Period'].map(str) + '/'+ df.index.map(str)
        df['date'] = df['date'].replace({'M':''}, regex = True)
        df.index = df['date']

        df = df.loc[:,"Value"]



        return df
    except Exception as e:
        print('problem getting cols: AA ' + str(e))


def col_ab_pdata():
    try:
        url = 'https://beta.bls.gov/dataViewer/view/timeseries/CUSR0000SA0L1E'
        resp = requests.get(url)
        soup = BeautifulSoup(resp.content.decode('utf-8'), features='lxml')
        table = soup.find("table", {"id": 'seriesDataTable1'}).prettify()
        df = pd.read_html(table, index_col=0)[0].dropna( how='all')
        df['date'] = df['Period'].map(str) + '/'+ df.index.map(str)
        df['date'] = df['date'].replace({'M': ''}, regex = True)
        df.index = df['date']
        df = df.loc[:, "Value"]

        return df
    except Exception as e:
        print('problem getting cols: AB ' + str(e))


def cols_ac_pdata():
    try:
        url = f'https://api.cbs.gov.il/index/data/price?id=40010&format=json&download=false'
        resp = requests.get(url).json()
        data = resp['month'][0]['date']
        col = pd.DataFrame.from_records(data)
        col['מדד מחירי דירות (1993 = 100) - אמצע התקופה הנסקרת'] = col['currBase'].apply(pd.Series).value
        col['Date'] =  col['month'].map(str) + '/' + col['year'].map(str)
        col = col[['Date','מדד מחירי דירות (1993 = 100) - אמצע התקופה הנסקרת']]
        col = col.set_index('Date')

        col.index = pd.to_datetime(col.index)
        col = col.sort_index()
        col.index = col.index.strftime('%m/%Y')
        return col

    except Exception as e:
        print('problem getting col: AC ' + str(e))