import requests
import pandas as pd
from datetime import datetime


def cols_d_to_h():
    url = "https://info.tase.co.il/Heb/Statistics/StatRes/2021/Stat_202_l02_2021.xlsx"
    resp = requests.get(url)
    df = pd.read_excel(resp.content, index_col=0, header=3)
    df = df.loc[: 'הערות לטבלה:'].iloc[:-2]
    return df[['מניות והמירים(1) סה"כ', 'אג"ח ממשלתי סה"כ הנפקות(2)', 'אג"ח ממשלתי פדיונות(3)', 'אג"ח ממשלתי גיוס נטו', 'אג"ח חברות סה"כ']]


def cols_i_to_j():

    current_month = datetime.today().month
    current_year = datetime.today().year

    for month in range(current_month, 0, -1):
        if month < 10:
            month = '0' + str(month)
        else:
            month = str(month)

        url = "https://www.cbs.gov.il/he/publications/doclib/" + str(current_year) + "/yarhon" + month + str(current_year % 100) + "/i2.xls"
        resp = requests.get(url)
        try:
            df = pd.read_excel(resp.content, index_col=0)
            df = df.dropna(how='all')
            df.columns = df.iloc[7].fillna('').str.cat(' ' + df.iloc[8].fillna(''))
            break
        except:
            print('No Data For Month - ' + str(month))

    if df is not None:
        df = df.loc[current_year - 1:]
        df = df[['Total ']]
        df.columns = ['מטבע ישראלי', 'מטבע חוץ']
        col_i = df['מטבע ישראלי']
        col_h = df['מטבע חוץ']
        result_df = pd.concat([col_i, col_h], axis=1).dropna(how='all')

        temp = []
        current_month = 1
        for i in result_df.index:
            if (pd.notna(i)) & (type(i) is int):
                curr_year = int(i)
                current_month = 1
            if type(i) is not str:
                temp.append(datetime(curr_year, current_month, 1).strftime('%m/%Y'))
                current_month += 1
        result_df.index = temp

    return result_df


