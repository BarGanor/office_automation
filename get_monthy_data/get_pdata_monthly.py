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


def col_ap_pdata():
    try:
        url = 'https://fred.stlouisfed.org/graph/fredgraph.xls?bgcolor=%23e1e9f0&chart_type=line&drp=0&fo=open%20sans&graph_bgcolor=%23ffffff&height=450&mode=fred&recession_bars=on&txtcolor=%23444444&ts=12&tts=12&width=1168&nt=0&thu=0&trc=0&show_legend=yes&show_axis_titles=yes&show_tooltip=yes&id=SPCS10RSA&scale=left&cosd=1987-01-01&coed=2099-12-01&line_color=%234572a7&link_values=false&line_style=solid&mark_type=none&mw=3&lw=2&ost=-99999&oet=99999&mma=0&fml=a&fq=Monthly&fam=avg&fgst=lin&fgsnd=2020-02-01&line_index=1&transformation=lin&vintage_date=2099-03-06&revision_date=2099-03-06&nd=1987-01-01'
        resp = requests.get(url)
        df = pd.read_excel(resp.content,index_col=0)
        df = df.iloc[15:,].dropna(how='all')
        df.index = pd.to_datetime(df.index).strftime('%m/%Y')
        df.columns =['S&P/Case-Shiller 10-City Composite Home Price Index']

        return df
    except Exception as e:
        print('problem getting cols: AP: ' +str(e))


def col_aw_pdata():
    try:
        curr_year = date.today().year
        df = pd.DataFrame()

        for year in range(curr_year-4,curr_year+1,1):
            url = f'https://www.gov.il/BlobFolder/generalpage/fuel_price_historycal/he/stationprice{year}.xlsx'
            resp = requests.get(url)
            col = pd.read_excel(resp.content,engine='openpyxl', index_col=0,header=5)
            col = col.dropna(how='all').loc[:,"בנזין 95 אוקטן נטול עופרת"]
            col.index = pd.to_datetime(col.index).strftime('%m/%Y')
            df = pd.concat([df, col], axis=0)
        df.columns = ["בנזין 95 אוקטן נטול עופרת"]

        return df
    except Exception as e:
        print('problem getting cols: AW: ' + str(e))