import requests
import pandas as pd
from datetime import datetime, date, timedelta


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

# def col_bj():
    import tradingeconomics as te
    te.login('Your_Key:Your_Secret')
    te.getHistoricalData(country='Israel', indicators='Foreign Exchange Reserves', initDate='2015-01-01')