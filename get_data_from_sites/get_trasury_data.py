import requests
import pandas as pd
from bs4 import BeautifulSoup

def get_treasury_data(record_num):
    url = 'https://www.treasury.gov/resource-center/data-chart-center/interest-rates/Pages/TextView.aspx?data=yield'
    treasury_response = requests.get(url).content
    soup = BeautifulSoup(treasury_response, features="lxml")
    treasury_data = soup.find("table", {"class": "t-chart"}).prettify()
    treasury_data = pd.read_html(treasury_data)[0]
    treasury_data = treasury_data.set_index('Date')
    treasury_data = treasury_data[['1 yr', '10 yr']]
    treasury_data = treasury_data.iloc[0:record_num]

    return treasury_data
print(get_treasury_data(7))