from get_data_from_sites.get_eia_data import *
import pandas as pd
from datetime import datetime, date
from dateutil.relativedelta import relativedelta
import string


def cols_d_to_e_pdata_daily(record_num):
    try:
        urls = ['https://www.eia.gov/dnav/pet/hist/rwtcD.htm','https://www.eia.gov/dnav/pet/hist/rbrteD.htm']
        table_names = ['Cushing, OK WTI Spot Price FOB  (Dollars per Barrel)','Europe Brent Spot Price FOB  (Dollars per Barrel)']

        result_df = pd.DataFrame()
        eia_data = get_eia_data(urls=urls, table_names=table_names, record_num=record_num)
        result_df = pd.concat([result_df, eia_data], axis=1)

        return result_df
    except Exception as e:
        print('problem getting col: D-E' + str(e))


# Empty columns
def cols_f_to_v_pdata_daily():
    try:
        today = datetime(date.today().year, date.today().month,
                         date.today().day).strftime('%d/%m/%Y')
        dtObj = datetime.strptime(today, '%d/%m/%Y')
        index_col = [(dtObj - relativedelta(months=i)).date() for i in range(1, 30, 1)]
        cols_name = []
        for first_char in string.ascii_uppercase:
            if first_char <= 'V' and first_char >= 'F':
                cols_name.append(first_char)

        df = pd.DataFrame(columns=cols_name, index=index_col)
        df = df.fillna("").sort_index()
        df.index = pd.to_datetime(df.index).strftime('%m/%Y')
        return df
    except Exception as e:
        print('problem getting col: F-V' + str(e))