from get_data_from_sites.get_tase_data import *
from get_data_from_sites.get_investing_data import *
from get_data_from_sites.get_eia_data import *
import pandas as pd
from datetime import datetime, date
from dateutil.relativedelta import relativedelta
import string

# Empty columns
def cols_d_to_e_daily_us_daily():
    try:
        today = datetime(date.today().year, date.today().month,
                                 date.today().day).strftime('%d/%m/%Y')
        dtObj = datetime.strptime(today, '%d/%m/%Y')
        index_col = [(dtObj - relativedelta(days=i)).date() for i in range(1, 30, 1)]
        cols_name = []
        for first_char in string.ascii_uppercase:
            if first_char <= 'E' and first_char >= 'D':
                cols_name.append(first_char)

        df = pd.DataFrame(columns=cols_name, index=index_col)
        df = df.fillna("").sort_index()
        df.index = pd.to_datetime(df.index).strftime('%d/%m/%Y')
        return df
    except Exception as e:
        print('problem getting col: D-E' + str(e))


# Empty columns
def cols_i_daily_us_daily():
    try:
        today = datetime(date.today().year, date.today().month,
                                 date.today().day).strftime('%d/%m/%Y')
        dtObj = datetime.strptime(today, '%d/%m/%Y')
        index_col = [(dtObj - relativedelta(days=i)).date() for i in range(1, 30, 1)]
        cols_name = []
        for first_char in string.ascii_uppercase:
            if first_char <= 'I' and first_char >= 'I':
                cols_name.append(first_char)

        df = pd.DataFrame(columns=cols_name, index=index_col)
        df = df.fillna("").sort_index()
        df.index = pd.to_datetime(df.index).strftime('%d/%m/%Y')
        return df
    except Exception as e:
        print('problem getting col: I' + str(e))


# Empty columns
def cols_k_to_r_daily_us_daily():
    try:
        today = datetime(date.today().year, date.today().month,
                                 date.today().day).strftime('%d/%m/%Y')
        dtObj = datetime.strptime(today, '%d/%m/%Y')
        index_col = [(dtObj - relativedelta(days=i)).date() for i in range(1, 30, 1)]
        cols_name = []
        for first_char in string.ascii_uppercase:
            if first_char <= 'R' and first_char >= 'K':
                cols_name.append(first_char)

        df = pd.DataFrame(columns=cols_name, index=index_col)
        df = df.fillna("").sort_index()
        df.index = pd.to_datetime(df.index).strftime('%d/%m/%Y')
        return df
    except Exception as e:
        print('problem getting cols: K-R' + str(e))


def cols_s_daily_us_daily(record_num):
    try:
        daily_us_df = pd.DataFrame()
        index_data = get_investing_data('vix').iloc[-record_num:]
        index_df = pd.DataFrame({'vix': index_data['Price']})

        col_s = pd.concat([daily_us_df, index_df], axis=1)

        return col_s

    except Exception as e:
        print('problem getting col: S' + str(e))


def cols_f_to_x_daily_us_daily(record_num):
    try:
        daily_us = ['nasdaq', 'sp 500', 'EEM','vix']
        daily_us_df = pd.DataFrame()

        for daily in daily_us:
            index_data = get_investing_data(daily).iloc[-record_num:]
            index_df = pd.DataFrame({daily: index_data['Price']})

            daily_us_df = pd.concat([daily_us_df, index_df], axis=1)

        daily_us_df = pd.concat([daily_us_df, cols_i_daily_us_daily()], axis=1)
        daily_us_df["מנורמל ל1.01.07 נאסדק"] = (daily_us_df['nasdaq'] / 2423.16) * 100
        daily_us_df = pd.concat([daily_us_df, cols_k_to_r_daily_us_daily()], axis=1)
        daily_us_df = pd.concat([daily_us_df, cols_s_daily_us_daily(record_num)], axis=1)
        daily_us_df["מנורמל ל1.01.08 נאסדק"] = (daily_us_df['nasdaq'] / 2609.63) * 100
        daily_us_df["מנורמל ל1.01.08 S&P 500"] = (daily_us_df['sp 500'] / 1447.16) * 100
        daily_us_df["מנורמל לאפריל 2011 נאסדק"] = (daily_us_df['nasdaq'] / 2789.6) * 100
        daily_us_df["מנורמל לאפריל S&P 500"] = (daily_us_df['sp 500'] / 1332.41) * 100
        daily_us_df["מנורמל לאפריל 2011 EEM"] = (daily_us_df['EEM'] / 49.45) * 100

        return daily_us_df

    except Exception as e:
        print('problem getting col: F-X' + str(e))







