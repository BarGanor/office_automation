from get_data_from_sites.get_investing_data import *
import pandas as pd
from datetime import datetime, date
from dateutil.relativedelta import relativedelta
import string

# Empty columns
def cols_d_to_s_daily_us_daily():
    try:
        today = datetime(date.today().year, date.today().month,
                                 date.today().day).strftime('%d/%m/%Y')
        dtObj = datetime.strptime(today, '%d/%m/%Y')
        index_col = [(dtObj - relativedelta(days=i)).date() for i in range(1, 30, 1)]
        cols_name = []
        for first_char in string.ascii_uppercase:
            if first_char <= 'S' and first_char >= 'D':
                cols_name.append(first_char)

        df = pd.DataFrame(columns=cols_name, index=index_col)
        df = df.fillna("").sort_index()
        df.index = pd.to_datetime(df.index).strftime('%d/%m/%Y')
        return df
    except Exception as e:
        print('problem getting cols: D-S' + str(e))


def get_col_t_daily_uk_daily(record_num):
    try:
        index_data = get_investing_data('FTSE').iloc[-record_num:]
        index_df = pd.DataFrame({'FTSE': index_data['Price']})

        return index_df

    except Exception as e:
        print('Problem getting col : T' + str(e))
