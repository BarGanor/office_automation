import requests
import pandas as pd
from bs4 import BeautifulSoup
from datetime import date


def get_treasury_data(record_num):
    todays_year = date.today().year
    df = pd.DataFrame()
    for year in [todays_year - 1, todays_year]:
        url = f"https://home.treasury.gov/resource-center/data-chart-center/interest-rates/daily-treasury-rates.csv/{year}/all?type=daily_treasury_yield_curve&field_tdr_date_value={year}&page&_format=csv"
        df1 = pd.read_csv(url, index_col=0)
        df1 = df1[['1 Yr', '10 Yr']]
        df1.index = pd.to_datetime(df1.index)
        df1 = df1.sort_index()
        df1.index = df1.index.strftime('%d/%m/%Y')
        df = pd.concat([df, df1], axis=0)

    df = df.iloc[-record_num:]
    return df


