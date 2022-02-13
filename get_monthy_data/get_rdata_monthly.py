import requests
import pandas as pd
from datetime import datetime, date, timedelta
from bs4 import BeautifulSoup
from dateutil.relativedelta import relativedelta
import time
import string

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)


def cols_c_to_d_rdata():
    try:
        series_id = {'col_c': '3979', 'col_d': '3971'}
        df = pd.DataFrame()
        for id in series_id.keys():
            url = f'https://apis.cbs.gov.il/series/data/list?id={series_id.get(id)}&format=json&download=false'
            resp = requests.get(url).json()
            data = resp['DataSet']['Series'][0]['obs']
            col = pd.DataFrame.from_records(data)
            col = col.set_index('TimePeriod')
            col.index = pd.to_datetime(col.index)
            col = col.sort_index()
            col.index = col.index.strftime('%m/%Y')
            df = pd.concat([df, col], axis=1)
        df.columns = ['מדדי ערך סל המכירות של רשתות השיווק במחירים קבועים ללא דלק וכולל מזון (מחירים קבועים בסיס(100=2020), מנוכה', 'מדדי ערך סל המכירות של רשתות השיווק במחירים קבועים ללא דלק וכלל מזון (100=2020), מקורי']
        return df
    except Exception as e:
        print('problem getting col: C-D' + str(e))


def cols_e_to_r_rdata():
    try:
        series_id = {'col_e': '3644', 'col_f': '3614', 'col_g': '3617', 'col_h': '3629',
                     'col_i': '3611', 'col_j': '3610','col_k': '3546','col_l': '3554','col_m': '625084'
                    ,'col_n': '625085'
                    ,'col_o': '625109','col_p': '625112','col_q': '625115','col_r': '625118'}
        df = pd.DataFrame()
        for id in series_id.keys():
            url = f'https://apis.cbs.gov.il/series/data/list?id={series_id.get(id)}&format=json&download=false'
            resp = requests.get(url).json()
            data = resp['DataSet']['Series'][0]['obs']
            col = pd.DataFrame.from_records(data)
            col = col.set_index('TimePeriod')
            col.index = pd.to_datetime(col.index)
            col = col.sort_index()
            col.index = col.index.strftime('%m/%Y')
            df = pd.concat([df, col], axis=1)
        df.columns = ['col_e', 'col_f', 'col_g', 'col_h',
                     'col_i', 'col_j','col_k','col_l','col_m','col_n'
                    ,'col_o','col_p','col_q','col_r']
        return df
    except Exception as e:
        print('problem getting col: E-R' + str(e))


# I used iloc method -- It's better to use loc method instead of iloc, but i didn't succeed. (Eliya Picard)
def col_s_rdata():
    try:
        url = 'https://www.boi.org.il/he/Research/Documents/indexheb.xls'
        resp = requests.get(url)
        df = pd.read_excel(resp.content, sheet_name="חלק א",index_col=0)
        df = df.iloc[5:,-2].dropna(how='all')
        df.index = pd.to_datetime(df.index).strftime('%m/%Y')
        df = df[~df.index.duplicated(keep='first')]
        df.name = "המדד המשולב למצב המשק"

        return df
    except Exception as e:
        print('problem getting cols: S: ' +str(e))


def cols_t_to_u_rdata():
    try:
        series_id = {'col_t': '574086', 'col_u': '574088'}
        df = pd.DataFrame()
        for id in series_id.keys():
            url = f'https://apis.cbs.gov.il/series/data/list?id={series_id.get(id)}&format=json&download=false'
            resp = requests.get(url).json()
            data = resp['DataSet']['Series'][0]['obs']
            col = pd.DataFrame.from_records(data)
            col = col.set_index('TimePeriod')
            col.index = pd.to_datetime(col.index)
            col = col.sort_index()
            col.index = col.index.strftime('%m/%Y')
            if series_id.get(id)=='574086':
                col = col*12 # Annually
            df = pd.concat([df, col], axis=1)
        df.columns = ['דירות שנמכרו מנוכי עונתיות בקצב שנתי', 'דירות למכירה בסוף תקופה מנוכה עונתיות']
        return df
    except Exception as e:
        print('problem getting col: T-U' + str(e))


# Empty columns
def cols_v_to_cf_rdata():
    try:
        today = datetime(date.today().year, date.today().month,
                         date.today().day).strftime('%d/%m/%Y')
        dtObj = datetime.strptime(today, '%d/%m/%Y')
        index_col = [(dtObj - relativedelta(months=i)).date() for i in range(1, 30, 1)]
        cols_name = []
        single_letters = [letter for letter in string.ascii_uppercase if letter >= 'V']
        for letter in single_letters:
            cols_name.append(letter)
        for first_char in string.ascii_uppercase:
            if first_char < 'C':
                for second_char in string.ascii_uppercase:
                    cols_name.append(first_char + second_char)
            if first_char == 'C':
                for second_char in string.ascii_uppercase:
                    if second_char <= 'F':
                        cols_name.append(first_char + second_char)

        df = pd.DataFrame(columns=cols_name, index=index_col)
        df = df.fillna("").sort_index()
        df.index = pd.to_datetime(df.index).strftime('%m/%Y')
        return df
    except Exception as e:
        print('problem getting col: V-CF' + str(e))


def cols_cg_to_ch_rdata():
    try:
        today = datetime(date.today().year, date.today().month,
                         date.today().day).strftime('%d/%m/%Y')
        dtObj = datetime.strptime(today, '%d/%m/%Y')
        index_col = [(dtObj - relativedelta(months=i)).date() for i in range(1, 30, 1)]
        cols_name = ['מדד מנהלי הרכש (PMI) מנוכה עונתיות', 'מדד אמון הצרכנים- בנק הפועלים']
        df = pd.DataFrame(columns=cols_name, index=index_col)
        df.index = pd.to_datetime(df.index)
        for i in df.columns:
            if i == 'מדד אמון הצרכנים- בנק הפועלים':
                df[i] = 'נתון נשלח במייל ללב ונפתלי'

            else:
                df[i] = 'להזין ידנית!'
        df= df.sort_index()
        df.index = pd.to_datetime(df.index).strftime('%m/%Y')
        return df
    except Exception as e:
        print('problem getting col: CG-CH' + str(e))


# Empty columns
def cols_ci_to_cl_rdata():
    try:
        today = datetime(date.today().year, date.today().month,
                         date.today().day).strftime('%d/%m/%Y')
        dtObj = datetime.strptime(today, '%d/%m/%Y')
        index_col = [(dtObj - relativedelta(months=i)).date() for i in range(1, 30, 1)]
        cols_name = []
        for first_char in string.ascii_uppercase:
            if first_char == 'C':
                for second_char in string.ascii_uppercase:
                    if second_char <= 'L' and second_char >= 'Y':
                        cols_name.append(first_char + second_char)

        df = pd.DataFrame(columns=cols_name, index=index_col)
        df = df.fillna("").sort_index()
        df.index = pd.to_datetime(df.index).strftime('%m/%Y')
        return df
    except Exception as e:
        print('problem getting col: CI-CL' + str(e))


def cols_cm_rdata():
    try:
        url = f'https://apis.cbs.gov.il/series/data/list?id=3526&format=json&download=false'
        resp = requests.get(url).json()
        data = resp['DataSet']['Series'][0]['obs']
        col = pd.DataFrame.from_records(data)
        col = col.set_index('TimePeriod')
        col.index = pd.to_datetime(col.index)
        col = col.sort_index()
        col.index = col.index.strftime('%m/%Y')
        col.columns = ['מדד פדיון ענפי המשק (מקורי) 100=2011']
        return col
    except Exception as e:
        print('problem getting col: CM' + str(e))


# Empty columns
def cols_cn_to_cy_rdata():
    try:
        today = datetime(date.today().year, date.today().month,
                         date.today().day).strftime('%d/%m/%Y')
        dtObj = datetime.strptime(today, '%d/%m/%Y')
        index_col = [(dtObj - relativedelta(months=i)).date() for i in range(1, 30, 1)]
        cols_name = []
        for first_char in string.ascii_uppercase:
            if first_char == 'C':
                for second_char in string.ascii_uppercase:
                    if second_char <= 'Y' and second_char >= 'N':
                        cols_name.append(first_char + second_char)

        df = pd.DataFrame(columns=cols_name, index=index_col)
        df = df.fillna("").sort_index()
        df.index = pd.to_datetime(df.index).strftime('%m/%Y')
        return df
    except Exception as e:
        print('problem getting col: CN-CY' + str(e))


def cols_cz_to_db_rdata():
    try:
        today = datetime(date.today().year, date.today().month,
                         date.today().day).strftime('%d/%m/%Y')
        dtObj = datetime.strptime(today, '%d/%m/%Y')
        index_col = [(dtObj - relativedelta(months=i)).date() for i in range(1, 30, 1)]
        cols_name = ['חודש', 'רבעון', 'שנה']
        df = pd.DataFrame(columns=cols_name, index=index_col)
        df.index = pd.to_datetime(df.index)
        for i in df.columns:
            if i == 'שנה':
                df[i] = df.index.year

            elif i == 'חודש':
                df[i] = df.index.month

            else:
                df[i] = df.index.quarter

        df = df.sort_index()
        df.index = pd.to_datetime(df.index).strftime('%m/%Y')
        return df
    except Exception as e:
        print('problem getting col: CZ-DB' + str(e))