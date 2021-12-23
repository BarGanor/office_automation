import requests
import pandas as pd
from datetime import datetime, date, timedelta
from bs4 import BeautifulSoup
from dateutil.relativedelta import relativedelta
import time
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)


def col_z():
    try:
        url = 'https://www.cbs.gov.il/he/mediarelease/doclib/2021/410/28_21_410t2.xls'
        df = pd.read_excel(url, index_col=-1)
        df = df.iloc[32:, 6].dropna(axis=0, how='all')
        df.index = df.index.fillna(0)
        df.index = df.index.astype(int)
        new_index = []
        curr_month = 1
        for ind in df.index:
            if ind != 0:
                curr_year = int(ind)
                curr_month = 1
                new_index.append(datetime(curr_year, curr_month, 1).strftime('%m/%Y'))
                curr_month += 1
            else:
                new_index.append(datetime(curr_year, curr_month, 1).strftime('%m/%Y'))
                curr_month += 1
        df.index = new_index
        df.name = 'אלפי תיירים, מנוכה עונתיות'
        return df
    except Exception as e:
        print('problem getting col: Z')


def col_aa():
    try:
        url = 'https://apis.cbs.gov.il/series/data/list?id=37615&format=json&download=false'
        resp = requests.get(url)
        resp = requests.get(url).json()
        data = resp['DataSet']['Series'][0]['obs']
        col = pd.DataFrame.from_records(data)
        col = col.set_index('TimePeriod')
        col.index = pd.to_datetime(col.index)
        col = col.sort_index()
        col.index = col.index.strftime('%m/%Y')
        col.name = 'מקורי'
        return col
    except Exception as e:
        print('problem getting col: AA')


def col_ab():
    try:
        url = 'https://www.cbs.gov.il/he/mediarelease/doclib/2021/400/28_21_400t1.xls'
        resp = requests.get(url)
        df = pd.read_excel(resp.content, index_col=-1)
        df = df.iloc[29:, -6].dropna(axis=0, how='all')
        df.index = df.index.fillna(0)
        df.index = df.index.astype(int)
        new_index = []
        curr_month = 1
        for ind in df.index:
            if ind != 0:
                curr_year = int(ind)
                curr_month = 1
                new_index.append(datetime(curr_year, curr_month, 1).strftime('%m/%Y'))
                curr_month += 1
            else:
                new_index.append(datetime(curr_year, curr_month, 1).strftime('%m/%Y'))
                curr_month += 1
        df.index = new_index
        df.name = 'תיירים זרים'
        return df
    except Exception as e:
        print('problem getting col: AB')


def col_ac():
    try:
        url = 'https://www.cbs.gov.il/he/mediarelease/doclib/2021/400/28_21_400t1.xls'
        resp = requests.get(url)
        df = pd.read_excel(resp.content, index_col=-1)
        df = df.iloc[29:, -7].dropna(axis=0, how='all')
        df.index = df.index.fillna(0)
        df.index = df.index.astype(int)
        new_index = []
        curr_month = 1
        for ind in df.index:
            if ind != 0:
                curr_year = int(ind)
                curr_month = 1
                new_index.append(datetime(curr_year, curr_month, 1).strftime('%m/%Y'))
                curr_month += 1
            else:
                new_index.append(datetime(curr_year, curr_month, 1).strftime('%m/%Y'))
                curr_month += 1
        df.index = new_index
        df.name = 'ישראלים'
        return df
    except Exception as e:
        print('problem getting col: AC')


def col_bj():
    try:
        url = 'https://tradingeconomics.com/israel/foreign-exchange-reserves'
        resp = requests.get(url)
        soup = BeautifulSoup(resp.content.decode('utf-8'), features='lxml')
        table = soup.find("table", {"class": 'table table-hover'}).prettify()
        df = pd.read_html(table, index_col=0)[0].dropna(axis=1, how='all')
        df[df.columns] = df[df.columns].replace({'\$': '', 'B': ''}, regex=True)
        df.index = pd.to_datetime(df.index)
        df = df.sort_index()
        df.index = df.index.strftime('%d/%m/%Y')
        df = df[["Actual"]].iloc[:-1, :]
        df = df.rename(columns={"Actual": "יתרות מט\"ח במיליוני דולרים"})
        new_index=[]
        date_format = '%d/%m/%Y'
        n = 1

        for i in range(0,2,1):
            dtObj = datetime.strptime(df.index[i], date_format)
            past_date = dtObj - relativedelta(months=n)
            past_date_str = past_date.strftime('%m/%Y')
            new_index.append(past_date_str)

        df.index = new_index
        df = df.apply(lambda x: x.str.replace('.',','))
        return df
    except Exception as e:
        print('problem getting col: BJ')


def col_bp_to_bq():
    try:
        today = datetime(date.today().year, date.today().month, date.today().day).strftime('%d/%m/%Y')
        dtObj = datetime.strptime(today, '%d/%m/%Y')
        index_col = [(dtObj - relativedelta(months=i)).date() for i in range(1,30,1)]
        df = pd.DataFrame(columns=['רכישות מט\"ח במליוני דולרים', 'שינוי ביתרות מט\"ח במיליוני דולרים'], index=index_col)
        df = df.fillna("").sort_index()
        df.index = pd.to_datetime(df.index).strftime('%m/%Y')
        return df
    except Exception as e:
        print('problem getting col: bp-bq')