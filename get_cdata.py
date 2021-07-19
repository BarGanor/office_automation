import pandas as pd
from bs4 import BeautifulSoup
import requests


def get_investing_data(index_name):
    if index_name == 'EEM':
        url = 'http://investing.com/etfs/ishares-msci-emg-markets-historical-data'

    elif index_name == 'sp 500':
        url = 'https://investing.com/indices/us-spx-500-historical-data'

    elif index_name == 'nasdaq':
        url = 'https://investing.com/indices/nasdaq-composite-historical-data'

    elif index_name == 'FTSE':
        url = 'https://investing.com/indices/uk-100-historical-data'

    elif index_name == 'Stoxx':
        url = 'https://www.investing.com/indices/eu-stoxx50-historical-data'
    else:
        return 'Enter Valid Index'
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'}

    req = requests.get(url, headers=headers)

    soup = BeautifulSoup(req.content, "html.parser")
    table_data = soup.find(id="curr_table")
    tel_bond_html = table_data.prettify()

    tel_bond_data = pd.read_html(tel_bond_html)[0]
    return tel_bond_data


def get_tase_data(index_name):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'}
    url = 'https://api.tase.co.il/api/index/historyeod'

    if index_name == 'gov bond':
        req = requests.post(url, headers=headers, data={'pType': "1", 'TotalRec': 1, 'pageNum': 1, 'oId': "602", 'lang': "0"})

    elif index_name == 'tel aviv banks':
        req = requests.post(url, headers=headers, data={'pType': "1", 'TotalRec': 1, 'pageNum': 1, 'oId': "164", 'lang': "0"})

    elif index_name == 'tel bond 20':
        req = requests.post(url, headers=headers, data={'pType': "1", 'TotalRec': 1, 'pageNum': 1, 'oId': "707", 'lang': "0"})

    elif index_name == 'tel bond 40':
        req = requests.post(url, headers=headers, data={'pType': "1", 'TotalRec': 1, 'pageNum': 1, 'oId': "708", 'lang': "0"})

    elif index_name == 'tel bond 60':
        req = requests.post(url, headers=headers, data={'pType': "1", 'TotalRec': 1, 'pageNum': 1, 'oId': "709", 'lang': "0"})

    elif index_name == 'Tel 125':
        req = requests.post(url, headers=headers, data={'pType': "1", 'TotalRec': 1, 'pageNum': 1, 'oId': "137", 'lang': "0"})

    elif index_name == 'Tel 35':
        req = requests.post(url, headers=headers, data={'pType': "1", 'TotalRec': 1, 'pageNum': 1, 'oId': "142", 'lang': "0"})

    else:
        return 'Enter Valid Index'

    gov_bond_index_dict = req.json().get('Items')
    gov_bond_index_data = pd.DataFrame.from_records(gov_bond_index_dict)
    return gov_bond_index_data



