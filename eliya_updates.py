import requests
import pandas as pd
from datetime import datetime, date, timedelta
from bs4 import BeautifulSoup
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)

# edata_monthly


def col_z():
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
    return df


def col_aa():
    url = 'https://apis.cbs.gov.il/series/data/list?id=37615&format=json&download=false'
    resp = requests.get(url)
    resp = requests.get(url).json()
    data = resp['DataSet']['Series'][0]['obs']
    col = pd.DataFrame.from_records(data)
    col = col.set_index('TimePeriod')
    col.index = pd.to_datetime(col.index)
    col = col.sort_index()
    col.index = col.index.strftime('%m/%Y')

    return col


def col_ab():
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
    return df


def col_ac():
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
    return df


def col_bj():
    url = 'https://www.boi.org.il/he/NewsAndPublications/PressReleases/Pages/7-12-21.aspx'
    resp = requests.get(url)
    soup = BeautifulSoup(resp.content.decode('utf-8'), features='lxml')
    table = soup.find("table",{"class":'MsoNormalTable'}).prettify()
    df = pd.read_html(table)[0]
    return ['סך הכול  יתרות מטבע החוץ']
