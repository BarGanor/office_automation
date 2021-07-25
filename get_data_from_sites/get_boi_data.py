import requests
from datetime import datetime, timedelta
import xml.etree.ElementTree as ET
import pandas as pd
from lxml import etree


def get_boi_data(record_num):
    currency_dict = {'01': 'U.S. Dollar', '27': 'EURO', '02': 'BRITISH POUND', '31': '100 JAPANESE YEN', '05': 'SWISS FRANK'}
    today_date = datetime.today()
    exchange_lst = []
    for i in range(record_num):
        curr_date = today_date - timedelta(days=i)
        curr_date = curr_date.date().strftime('%Y-%m-%d')
        exchange_dict = {'Date': curr_date}

        for currency in currency_dict.keys():
            url = 'https://www.boi.org.il/currency.xml?rdate=' + curr_date.replace('-', '') + '&curr=' + currency
            exchange_xml = requests.get(url).content
            root = ET.fromstring(exchange_xml)

            for child in root:
                for attr in child:
                    if attr.tag == 'RATE':
                        exchange_dict[currency_dict.get(currency)] = attr.text
        exchange_lst.append(exchange_dict)

    exchange_df = pd.DataFrame(exchange_lst).set_index('Date')
    exchange_df = exchange_df.dropna(how='all')
    return exchange_df

