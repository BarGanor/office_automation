import requests
import pandas as pd
from datetime import datetime, date, timedelta
from bs4 import BeautifulSoup
from dateutil.relativedelta import relativedelta
import time
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)


def cols_d_to_e_mdata():
    now = date.today()
    year = now.year
    past_date = now - relativedelta(years=2)
    past_date_year = past_date.year
    year_list = [str(year) for year in range(past_date_year, year + 1, 1)]
    df = pd.DataFrame()
    try:
        for year in year_list:
            url = f'https://home.treasury.gov/resource-center/data-chart-center/interest-rates/daily-treasury-rates.csv/{year}/all?type=daily_treasury_yield_curve&field_tdr_date_value={year}&page&_format=csv'
            df1 = pd.read_csv(url, index_col=0)
            df1 = df1.loc[:,["1 Yr", "10 Yr"]]
            df1 = df1.groupby(pd.PeriodIndex(df1.index, freq="M")).mean()
            df = pd.concat([df, df1], axis=0)
        df = df.sort_index()
        df.index = df.index.strftime('%m/%Y')
        return df

    except Exception as e:
        print('problem getting cols: D-E' + str(e))