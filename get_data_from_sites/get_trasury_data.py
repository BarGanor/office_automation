import requests
import pandas as pd
from bs4 import BeautifulSoup
from datetime import date


def get_treasury_data(record_num):
    todays_year = date.today().year
    url = 'https://www.treasury.gov/resource-center/data-chart-center/interest-rates/Pages/TextView.aspx?data=yieldYear&year=' + str(todays_year)
    treasury_response = requests.get(url).content
    soup = BeautifulSoup(treasury_response, features="lxml")
    treasury_data = soup.find("table", {"class": "t-chart"}).prettify()
    treasury_data = pd.read_html(treasury_data)[0]
    treasury_data = treasury_data.set_index('Date')
    treasury_data = treasury_data[['1 yr', '10 yr']]
    treasury_data = treasury_data.iloc[-record_num:]
    treasury_data.index = pd.to_datetime(treasury_data.index)
    treasury_data = treasury_data.sort_index()
    treasury_data.index = treasury_data.index.strftime('%d/%m/%Y')

    return treasury_data


