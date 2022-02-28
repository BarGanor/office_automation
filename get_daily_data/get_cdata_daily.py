from get_data_from_sites.get_tase_data import *
import pandas as pd
from datetime import datetime, date
from dateutil.relativedelta import relativedelta
import string


# Empty columns
def cols_d_to_y_cdata_daily():
    try:
        today = datetime(date.today().year, date.today().month,
                         date.today().day).strftime('%d/%m/%Y')
        dtObj = datetime.strptime(today, '%d/%m/%Y')
        index_col = [(dtObj - relativedelta(months=i)).date() for i in range(1, 30, 1)]
        cols_name = []
        for first_char in string.ascii_uppercase:
            if first_char <= 'Y' and first_char >= 'D':
                cols_name.append(first_char)

        df = pd.DataFrame(columns=cols_name, index=index_col)
        df = df.fillna("").sort_index()
        df.index = pd.to_datetime(df.index).strftime('%m/%Y')
        return df
    except Exception as e:
        print('problem getting col: D-Y' + str(e))


def cols_z_to_aa_cdata_daily():
    try:
        index_names = ['tel bond 20', 'tel bond 40']

        cols_z_to_aa_cdata_daily_df = pd.DataFrame()
        for index in index_names:
            index_data = get_tase_data(index)
            index_df = pd.DataFrame({index: index_data})

            cols_z_to_aa_cdata_daily_df = pd.concat([cols_z_to_aa_cdata_daily_df, index_df], axis=1)

        return cols_z_to_aa_cdata_daily_df
    except Exception as e:
        print('problem getting cols: Z-AA' + str(e))


# Empty columns
def cols_ab_to_ah_cdata_daily():
    try:
        today = datetime(date.today().year, date.today().month,
                         date.today().day).strftime('%d/%m/%Y')
        dtObj = datetime.strptime(today, '%d/%m/%Y')
        index_col = [(dtObj - relativedelta(months=i)).date() for i in range(1, 30, 1)]
        cols_name = []
        for first_char in string.ascii_uppercase:
            if first_char == 'A':
                for second_char in string.ascii_uppercase:
                    if second_char <= 'H' and second_char >= 'B':
                        cols_name.append(first_char + second_char)

        df = pd.DataFrame(columns=cols_name, index=index_col)
        df = df.fillna("").sort_index()
        df.index = pd.to_datetime(df.index).strftime('%m/%Y')
        return df
    except Exception as e:
        print('problem getting col: AB-AH' + str(e))


def cols_ai_cdata_daily():
    try:
        index_names = ['gov bond']

        cols_ai_cdata_daily_df = pd.DataFrame()
        for index in index_names:
            index_data = get_tase_data(index)
            index_df = pd.DataFrame({index: index_data})

            cols_ai_cdata_daily_df = pd.concat([cols_ai_cdata_daily_df, index_df], axis=1)

        return cols_ai_cdata_daily_df
    except Exception as e:
        print('problem getting cols: AI' + str(e))


# Empty columns
def cols_aj_to_ak_cdata_daily():
    try:
        today = datetime(date.today().year, date.today().month,
                         date.today().day).strftime('%d/%m/%Y')
        dtObj = datetime.strptime(today, '%d/%m/%Y')
        index_col = [(dtObj - relativedelta(months=i)).date() for i in range(1, 30, 1)]
        cols_name = []
        for first_char in string.ascii_uppercase:
            if first_char == 'A':
                for second_char in string.ascii_uppercase:
                    if second_char <= 'K' and second_char >= 'J':
                        cols_name.append(first_char + second_char)

        df = pd.DataFrame(columns=cols_name, index=index_col)
        df = df.fillna("").sort_index()
        df.index = pd.to_datetime(df.index).strftime('%m/%Y')
        return df
    except Exception as e:
        print('problem getting col: AJ-AK' + str(e))


def cols_al_to_am_cdata_daily():
    try:
        index_names = ['tel aviv banks', 'tel bond 60']

        cols_al_to_am_cdata_daily_df = pd.DataFrame()
        for index in index_names:
            index_data = get_tase_data(index)
            index_df = pd.DataFrame({index: index_data})

            cols_al_to_am_cdata_daily_df = pd.concat([cols_al_to_am_cdata_daily_df, index_df], axis=1)

        return cols_al_to_am_cdata_daily_df
    except Exception as e:
        print('problem getting cols: AL-AM' + str(e))


