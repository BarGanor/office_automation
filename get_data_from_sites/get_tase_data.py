import requests
import pandas as pd

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

