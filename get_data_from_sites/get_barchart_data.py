import requests
import pandas as pd
from http.cookies import SimpleCookie
from bs4 import BeautifulSoup

url = 'https://www.barchart.com/futures/quotes/BWY00/price-history/historical?orderBy=tradeTime&orderDir=desc'

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36',}
barchart_response = requests.get(url, headers=headers)
# print(barchart_response.content)
soup = BeautifulSoup(barchart_response.content, parser='html.parser', features='lxml')

for table in soup.findAll("table"):
    print(pd.read_html(table.prettify()))
