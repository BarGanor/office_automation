import pandas as pd
from get_data_from_sites.get_tase_data import *
from get_data_from_sites.get_investing_data import *
from get_data_from_sites.get_boi_data import *


def get_cdata_daily(record_num):
    index_names = ['tel bond 20', 'tel bond 40', 'gov bond', 'tel aviv banks', 'tel bond 60']

    cdata_daily_df = pd.DataFrame()
    for index in index_names:
        index_data = get_tase_data(index).iloc[0:record_num - 1].set_index('TradeDate')
        index_df = pd.DataFrame({index: index_data['BaseRate']})

        cdata_daily_df = pd.concat([cdata_daily_df, index_df], axis=1)

    return cdata_daily_df


def get_htdata_daily(record_num):
    daily_il = ['Tel 35', 'Tel 125']
    daily_us = ['nasdaq', 'sp 500', 'EEM', 'vix']
    daily_uk = ['FTSE']
    daily_all = [daily_il, daily_us, daily_uk]

    daily_il_df = pd.DataFrame()
    daily_us_df = pd.DataFrame()
    daily_uk_df = pd.DataFrame()

    for daily in daily_all:
        for index in daily:

            if daily is daily_il:
                index_data = get_tase_data(index).iloc[0:record_num]
                index_data = index_data.set_index('TradeDate')
                index_df = pd.DataFrame({index: index_data['BaseRate']})

                daily_il_df = pd.concat([daily_il_df, index_df], axis=1)

            else:
                index_data = get_investing_data(index).iloc[0:record_num]
                index_data['Date'] = pd.to_datetime(index_data['Date'])
                index_data = index_data.set_index('Date')
                index_df = pd.DataFrame({index: index_data['Price']})

                if daily is daily_us:
                    daily_us_df = pd.concat([daily_us_df, index_df], axis=1)
                else:
                    daily_uk_df = pd.concat([daily_uk_df, index_df], axis=1)

    return daily_il_df, daily_us_df.sort_index(ascending=False), daily_uk_df.sort_index(ascending=False)


def get_xdata_daily(record_num):
    return get_boi_data(8)
