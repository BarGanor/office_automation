import requests
import pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime, timedelta


def get_eia_table(url, table_name):
    eia_response = requests.get(url).content
    soup = BeautifulSoup(eia_response, parser='html.parser', features='lxml')
    eia_data = soup.find("table", {"summary": table_name}).prettify()
    return pd.read_html(eia_data)[0]


def get_dt_lst(row):
    first_date = row.values[0][:row.values[0].find('to') - 1]
    dt_lst = []
    for i in range(5):
        temp_dt = datetime.strptime(first_date, '%Y %b-%d') + timedelta(days=i)
        dt_lst.append(temp_dt)
    return dt_lst


def row_to_df(row):
    dt_lst = get_dt_lst(row)
    rowDf = row[1:]
    rowDf.index = dt_lst
    return rowDf


def get_eia_column(url, table_name):
    table = get_eia_table(url, table_name)[-10:].dropna(how='all')
    df = pd.DataFrame()
    for row in range(len(table)):
        df = pd.concat([df, row_to_df(table.iloc[row])], axis=0)
    return df.dropna()


def get_eia_data(urls, table_names, record_num):
    eia_data = pd.DataFrame()
    for i in range(len(urls)):
        eia_column = get_eia_column(urls[i], table_names[i])
        eia_column.columns = [table_names[i]]
        eia_data = pd.concat([eia_data, eia_column], axis=1)

    eia_data.index= pd.to_datetime(eia_data.index)
    eia_data = eia_data.sort_index()
    eia_data.index = eia_data.index.strftime('%d/%m/%Y')
    return eia_data.dropna(axis=0)[-record_num:]



