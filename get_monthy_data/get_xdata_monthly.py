import requests
import pandas as pd
from datetime import datetime, date, timedelta
from bs4 import BeautifulSoup
from dateutil.relativedelta import relativedelta
import time
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)


def currancy_column(currancy):
    now = date.today()
    year = now.year
    past_date = now - relativedelta(years=2)
    past_date_year = past_date.year
    year_list = [str(year) for year in range(past_date_year, year + 1, 1)]
    year_list_2_digit = [int(year[2:]) for year in year_list]
    df = pd.DataFrame()
    try:
        for year in year_list_2_digit:
            url = f'https://www.boi.org.il/he/Markets/DocLib/yazav{year}.xlsx'
            resp = requests.get(url)
            df1 = pd.read_excel(resp.content, header=3, index_col=1)
            df1 = df1.iloc[1:, 2:].dropna(axis=1, how='all').transpose()
            if currancy == 'U.S. DOLLAR':
                currancy1 = df1.iloc[:-1, 0]
            elif currancy == 'EURO':
                currancy1 = df1.iloc[:-1, -5]
            elif currancy == 'BRITISH POUND':
                currancy1 = df1.iloc[:-1, 1]
            elif currancy == 'JAPANESE YEN':
                currancy1 = df1.iloc[:-1, 2]
            elif currancy == 'SWISS FRANC':
                currancy1 = df1.iloc[:-1, 3]
            df = pd.concat([df, currancy1], axis=0)

        df.columns = [currancy]
        return df

    except:
        year_list = [str(year) for year in range(past_date_year, year, 1)]
        year_list_2_digit = [int(year[2:]) for year in year_list]
        for year in year_list_2_digit:
            url = f'https://www.boi.org.il/he/Markets/DocLib/yazav{year}.xlsx'
            resp = requests.get(url)
            df1 = pd.read_excel(resp.content, header=3, index_col=1)
            df1 = df1.iloc[1:, 2:].dropna(axis=1, how='all').transpose()
            if currancy == 'U.S. DOLLAR':
                currancy1 = df1.iloc[:-1, 0]
            elif currancy == 'EURO':
                currancy1 = df1.iloc[:-1, -5]
            elif currancy == 'BRITISH POUND':
                currancy1 = df1.iloc[:-1, 1]
            elif currancy == 'JAPANESE YEN':
                currancy1 = df1.iloc[:-1, 2]
            elif currancy == 'SWISS FRANC':
                currancy1 = df1.iloc[:-1, 3]
            df = pd.concat([df, currancy1], axis=0)

        df.columns = [currancy]
        return df


def cols_d_to_h_xdata():
    currancy_names = ['U.S. DOLLAR', 'EURO', 'BRITISH POUND', 'JAPANESE YEN', 'SWISS FRANC']
    df_all_currancy = pd.DataFrame()
    for currancy in currancy_names:
        df_all_currancy = pd.concat([df_all_currancy, currancy_column(currancy)], axis=1)

    return df_all_currancy


def col_i_to_k_xdata():
    try:
        url = 'http://stats.oecd.org/index.aspx?queryid=169'
        resp = requests.get(url)
        soup = BeautifulSoup(resp.content.decode('utf-8'), features='lxml')
        table = soup.find("table", {"class": 'DataTable'}).prettify()
        df3 = pd.read_html(table, index_col=1, header=2)[0].dropna( how='all')
        df3 = df3.iloc[2:,4:].transpose()
        df3 = df3.iloc[5:, :].loc[:,['Euro area (19 countries)','United Kingdom','Japan']]
        df3.index = pd.to_datetime(df3.index)
        df3.index = df3.index.strftime('%m/%Y')

        return df3
    except Exception as e:
        print('problem getting cols: I-K' + str(e))


def col_l_to_n():
    try:
        today = datetime(date.today().year, date.today().month, date.today().day).strftime('%d/%m/%Y')
        dtObj = datetime.strptime(today, '%d/%m/%Y')
        index_col = [(dtObj - relativedelta(months=i)).date() for i in range(1,30,1)]
        df = pd.DataFrame(columns=[ 'Base 1990','Base 2000','reer_avg index (2005=100)'], index=index_col)
        df = df.fillna("").sort_index()
        df.index = pd.to_datetime(df.index).strftime('%m/%Y')
        return df
    except Exception as e:
        print('problem getting col: L-N' + str(e))


def col_p():
    try:
        url = f'https://www.bis.org/statistics/eer/broad.xlsx'
        resp = requests.get(url)
        df = pd.read_excel(resp.content, sheet_name='Real', header=3, index_col=0)
        df = df.loc['01-2020':, 'Israel']
        df.name = 'BIS-REER'
        new_index = []
        for ind in df.index:
            new_index.append(ind.strftime('%m/%Y'))
        df.index = new_index

        return df
    except Exception as e:
        print('problem getting col: p' + str(e))
