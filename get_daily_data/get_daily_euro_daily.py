import requests_html
import pandas as pd


def get_daily_euro_daily(record_num):
    url = "https://finance.yahoo.com/quote/%5ESTOXX50E/history?p=%5ESTOXX50E"
    r = requests_html.HTMLSession().get(url)
    table = r.html.find("table", first=True)
    lst1 = []
    for items in table.find("tr")[2:]:
        data = [item.text for item in items.find("th,td")[:-1]]
        lst1.append(data)
    df = pd.DataFrame(columns=['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close'], data=lst1)
    df = df.set_index('Date')
    df.index = pd.to_datetime(df.index)
    df = df.sort_index()
    df.index = df.index.strftime('%d/%m/%Y')
    df = df.loc[:, "Close"].iloc[-record_num:]

    return df