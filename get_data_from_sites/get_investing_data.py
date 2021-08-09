import requests
from bs4 import BeautifulSoup
import pandas as pd


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

    elif index_name == 'vix':
        url = 'https://www.investing.com/indices/volatility-s-p-500-historical-data'

    else:
        return 'Enter Valid Index'
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'}

    req = requests.get(url, headers=headers)

    soup = BeautifulSoup(req.content, "html.parser")
    index_data = soup.find(id="curr_table")
    index_html = index_data.prettify()

    index_data = pd.read_html(index_html)[0]

    index_data = index_data.set_index('Date')
    index_data.index = pd.to_datetime(index_data.index)
    index_data = index_data.sort_index()
    index_data.index = index_data.index.strftime('%d/%m/%Y')
    return index_data

