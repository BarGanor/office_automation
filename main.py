import pandas as pd
from bs4 import BeautifulSoup
import requests


def get_telbond_data(bond_number):
    url = 'https://investing.com/indices/telbond' + str(bond_number) + '-historical-data'
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'}

    req = requests.get(url, headers=headers)

    soup = BeautifulSoup(req.content, "html.parser")
    table_data = soup.find(id="curr_table")
    tel_bond_html = table_data.prettify()

    tel_bond_data = pd.read_html(tel_bond_html)[0]
    return tel_bond_data

def get_gov_bond_data():
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'}
    url = 'https://api.tase.co.il/api/index/historyeod'
    req = requests.post(url, headers=headers, data={'pType': "1", 'TotalRec': 1, 'pageNum': 1, 'oId': "602", 'lang': "0"})
    gov_bond_index_dict = req.json().get('Items')
    gov_bond_index_data = pd.DataFrame.from_records(gov_bond_index_dict)
    return gov_bond_index_data


print(get_telbond_data(bond_number='20'))
print(get_telbond_data(bond_number='40'))
print(get_gov_bond_data())

