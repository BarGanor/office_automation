from get_data_from_sites.get_tase_data import *
from get_data_from_sites.get_eia_data import *
import pandas as pd
from datetime import datetime, date
from dateutil.relativedelta import relativedelta
import string


# Empty columns
def cols_f_to_h_dailyil_daily():
    try:
        today = datetime(date.today().year, date.today().month,
                                 date.today().day).strftime('%d/%m/%Y')
        dtObj = datetime.strptime(today, '%d/%m/%Y')
        index_col = [(dtObj - relativedelta(days=i)).date() for i in range(1, 30, 1)]
        cols_name = []
        for first_char in string.ascii_uppercase:
            if first_char <= 'H' and first_char >= 'F':
                cols_name.append(first_char)

        df = pd.DataFrame(columns=cols_name, index=index_col)
        df = df.fillna("").sort_index()
        df.index = pd.to_datetime(df.index).strftime('%d/%m/%Y')
        return df
    except Exception as e:
        print('problem getting col: F-H' + str(e))


def cols_d_to_i_dailyil_daily(record_num):
    try:
        daily_il = ['Tel 35', 'Tel 125']
        daily_il_df = pd.DataFrame()

        for daily in daily_il:
            index_data = get_tase_data(daily).iloc[-record_num:]
            index_df = pd.DataFrame({daily: index_data})

            daily_il_df = pd.concat([daily_il_df, index_df], axis=1)

        daily_il_df = pd.concat([daily_il_df, cols_f_to_h_dailyil_daily()], axis=1)

        daily_il_df["מנורמל לאפריל 2011 ת'א 100"] = (daily_il_df['Tel 125'] / 1215.49) * 100
        return daily_il_df
    except Exception as e:
        print('problem getting col: D-I' + str(e))

