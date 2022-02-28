from get_data_from_sites.get_tase_data import *
from get_data_from_sites.get_investing_data import *
from get_data_from_sites.get_eia_data import *


def get_htdata_daily(record_num):
    try:
        print('getting htdata')
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
                    index_data = get_tase_data(index).iloc[-record_num:]
                    index_df = pd.DataFrame({index: index_data})

                    daily_il_df = pd.concat([daily_il_df, index_df], axis=1)
                else:
                    index_data = get_investing_data(index).iloc[-record_num:]
                    index_df = pd.DataFrame({index: index_data['Price']})

                    if daily is daily_us:
                        daily_us_df = pd.concat([daily_us_df, index_df], axis=1)
                    else:
                        daily_uk_df = pd.concat([daily_uk_df, index_df], axis=1)

        daily_il_df["מנורמל לאפריל 2011 ת'א 100"] = (daily_il_df['Tel 125'] / 1215.49) * 100
        return {'daily_il': daily_il_df, 'daily_us': daily_us_df, 'daily_uk': daily_uk_df}
    except Exception as e:
        print('Problem getting htdata: ' + str(e))
        return None

