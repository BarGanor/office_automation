import requests
from bs4 import BeautifulSoup


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
    table_data = soup.find(id="curr_table")
    tel_bond_html = table_data.prettify()

    tel_bond_data = pd.read_html(tel_bond_html)[0]
    return tel_bond_data
