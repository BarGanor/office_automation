import requests
import pandas as pd
from bs4 import BeautifulSoup

def get_eia_column(url, table_name, record_num):
    eia_response = requests.get(url).content
    soup = BeautifulSoup(eia_response, parser='html.parser', features='lxml')
    eia_data = soup.find("table", {"summary": table_name}).prettify()
    return pd.read_html(eia_data)[0]

def get_eia_data(urls, table_names, record_num):
    eia_data = pd.DataFrame()
    for i in range(len(urls)):
        eia_column = get_eia_column(urls[i], table_names[i], record_num)
        eia_data = pd.concat([eia_data,eia_column], axis=1)
    return eia_data


urls = ['https://www.eia.gov/dnav/pet/hist/rbrteD.htm','https://www.eia.gov/dnav/pet/hist/rwtcD.htm']
table_names = ['Europe Brent Spot Price FOB  (Dollars per Barrel)', 'Cushing, OK WTI Spot Price FOB  (Dollars per Barrel)']
print(get_eia_data(urls = urls, table_names=table_names, record_num=7))

