import requests
import pandas as pd
from datetime import datetime, date, timedelta
from bs4 import BeautifulSoup
from dateutil.relativedelta import relativedelta
import time
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)


def get_curr_year_list_2_digit(year):
    curr_year = date.today().year
    list_of_numbers = list(str(year))
    curr_year_list_2_digit = list_of_numbers[2] + list_of_numbers[3]
    return curr_year_list_2_digit


def get_message_number_tourist(year,monthName):
    url = f'https://www.cbs.gov.il/en/mediarelease/Pages/{year}/Visitor-Arrivals-to-Israel-in-{monthName}-{year}.aspx'
    resp = requests.get(url)
    soup = BeautifulSoup(resp.content.decode('utf-8'), features='lxml')
    tags = soup.find(class_="articleDetails")
    br_tags = tags.text.strip().split()
    message_number = br_tags[3].split("/")[0]
    return message_number


def get_roman_number(number):
    roman_month = {1: 'I',2:'II',3:'III' ,4:'IV' ,5:'V' ,6:'VI' ,7:'VII' ,8:'VIII' ,9:'IX' ,10:'X' ,11:'XI' ,12:'XII'}
    return roman_month.get(number)


def get_key_by_value(roman_number):
    roman_month = {1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V',
                   6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX', 10: 'X', 11:'XI',
                   12 :'XII'}
    return [name for name, age in roman_month.items() if age == roman_number][0]


def col_z_edata():
    try:
        curr_year = date.today().year

        curr_month = date.today().month
        two_months_ago = (datetime.today() + relativedelta(months=-2)).month
        two_months_ago_name = (datetime.today() + relativedelta(months=-2)).strftime("%B")
        if two_months_ago in ['1', '2']:
            url = f'https://www.cbs.gov.il/he/mediarelease/doclib/{curr_year - 1}/{get_message_number_tourist(curr_year - 1, two_months_ago_name)}/28_{get_curr_year_list_2_digit(curr_year - 1)}_{get_message_number_tourist(curr_year - 1, two_months_ago_name)}t2.xls'
            resp = requests.get(url)
            df = pd.read_excel(resp.content).dropna(how='all', axis=1).dropna(how='all', axis=0)
            df['TABLE 2. TOURIST ARRIVALS IN ISRAEL (1)'] = df['TABLE 2. TOURIST ARRIVALS IN ISRAEL (1)'].ffill()
            df = df.bfill(axis=1)
            df['date'] = df['Unnamed: 2'].map(str) + '/' + df['TABLE 2. TOURIST ARRIVALS IN ISRAEL (1)'].map(str)
            df.index = df['date']
            df = df.loc[f'I/{curr_year - 2}':f'{get_roman_number(two_months_ago)}/{curr_year}*',
                 ['Unnamed: 7', 'Unnamed: 4']]
            df = df.rename({'Unnamed: 4': 'אלפי תיירים, מנוכה עונתיות', 'Unnamed: 7': 'מקורי'}, axis=1)
            index_col = []
            for i in df.index:
                d = i.split("/")
                if d[1].isnumeric():
                    e = d[0].replace(d[0], str(get_key_by_value(d[0])))
                    r = e + "/" + d[1]
                    index_col.append(r)
                else:
                    d[1] = d[1].replace('*', "")
                    e = d[0].replace(d[0], str(get_key_by_value(d[0])))
                    r = e + "/" + d[1]
                    index_col.append(r)
            df.index = index_col
            return df
        else:
            url = f'https://www.cbs.gov.il/he/mediarelease/doclib/{curr_year}/{get_message_number_tourist(curr_year, two_months_ago_name)}/28_{get_curr_year_list_2_digit(curr_year)}_{get_message_number_tourist(curr_year, two_months_ago_name)}t2.xls'
            resp = requests.get(url)
            df = pd.read_excel(resp.content).dropna(how='all', axis=1).dropna(how='all', axis=0)
            df['TABLE 2. TOURIST ARRIVALS IN ISRAEL (1)'] = df['TABLE 2. TOURIST ARRIVALS IN ISRAEL (1)'].ffill()
            df = df.bfill(axis=1)
            df['date'] = df['Unnamed: 2'].map(str) + '/' + df['TABLE 2. TOURIST ARRIVALS IN ISRAEL (1)'].map(str)
            df.index = df['date']
            df = df.loc[f'I/{curr_year - 2}':f'{get_roman_number(two_months_ago)}/{curr_year}*',
                 ['Unnamed: 7', 'Unnamed: 4']]
            df = df.rename({'Unnamed: 4': 'אלפי תיירים, מנוכה עונתיות', 'Unnamed: 7': 'מקורי'}, axis=1)
            index_col = []
            for i in df.index:
                d = i.split("/")
                if d[1].isnumeric():
                    e = d[0].replace(d[0], str(get_key_by_value(d[0])))
                    r = e + "/" + d[1]
                    index_col.append(r)
                else:
                    d[1] = d[1].replace('*', "")
                    e = d[0].replace(d[0], str(get_key_by_value(d[0])))
                    r = e + "/" + d[1]
                    index_col.append(r)
            df.index = index_col
            return df
    except Exception as e:
        print('problem getting cols: Z-AA ' + str(e))


def col_aa():
    try:
        url = 'https://apis.cbs.gov.il/series/data/list?id=37615&format=json&download=false'
        resp = requests.get(url).json()
        data = resp['DataSet']['Series'][0]['obs']
        col = pd.DataFrame.from_records(data)
        col = col.set_index('TimePeriod')
        col.index = pd.to_datetime(col.index)
        col = col.sort_index()
        col.index = col.index.strftime('%m/%Y')
        col.name = 'מקורי'
        return col
    except Exception as e:
        print('problem getting col: AA' + str(e))


def col_ab():
    try:
        url = 'https://www.cbs.gov.il/he/mediarelease/doclib/2021/400/28_21_400t1.xls'
        resp = requests.get(url)
        df = pd.read_excel(resp.content, index_col=-1)
        df = df.iloc[29:, -6].dropna(axis=0, how='all')
        df.index = df.index.fillna(0)
        df.index = df.index.astype(int)
        new_index = []
        curr_month = 1
        for ind in df.index:
            if ind != 0:
                curr_year = int(ind)
                curr_month = 1
                new_index.append(datetime(curr_year, curr_month, 1).strftime('%m/%Y'))
                curr_month += 1
            else:
                new_index.append(datetime(curr_year, curr_month, 1).strftime('%m/%Y'))
                curr_month += 1
        df.index = new_index
        df.name = 'תיירים זרים'
        return df
    except Exception as e:
        print('problem getting col: AB' + str(e))


def col_ac():
    try:
        url = 'https://www.cbs.gov.il/he/mediarelease/doclib/2021/400/28_21_400t1.xls'
        resp = requests.get(url)
        df = pd.read_excel(resp.content, index_col=-1)
        df = df.iloc[29:, -7].dropna(axis=0, how='all')
        df.index = df.index.fillna(0)
        df.index = df.index.astype(int)
        new_index = []
        curr_month = 1
        for ind in df.index:
            if ind != 0:
                curr_year = int(ind)
                curr_month = 1
                new_index.append(datetime(curr_year, curr_month, 1).strftime('%m/%Y'))
                curr_month += 1
            else:
                new_index.append(datetime(curr_year, curr_month, 1).strftime('%m/%Y'))
                curr_month += 1
        df.index = new_index
        df.name = 'ישראלים'
        return df
    except Exception as e:
        print('problem getting col: AC' + str(e))


def col_bj():
    try:
        url = 'https://tradingeconomics.com/israel/foreign-exchange-reserves'
        resp = requests.get(url)
        soup = BeautifulSoup(resp.content.decode('utf-8'), features='lxml')
        table = soup.find("table", {"class": 'table table-hover'}).prettify()
        df = pd.read_html(table, index_col=0)[0].dropna(axis=1, how='all')
        df[df.columns] = df[df.columns].replace({'\$': '', 'B': ''}, regex=True)
        df.index = pd.to_datetime(df.index)
        df = df.sort_index()
        df.index = df.index.strftime('%d/%m/%Y')
        df = df[["Actual"]].iloc[:-1, :]
        df = df.rename(columns={"Actual": "יתרות מט\"ח במיליוני דולרים"})
        new_index=[]
        date_format = '%d/%m/%Y'
        n = 1

        for i in range(0,2,1):
            dtObj = datetime.strptime(df.index[i], date_format)
            past_date = dtObj - relativedelta(months=n)
            past_date_str = past_date.strftime('%m/%Y')
            new_index.append(past_date_str)

        df.index = new_index
        df = df.apply(lambda x: x.str.replace('.',','))
        return df
    except Exception as e:
        print('problem getting col: BJ' + str(e))


def col_bp_to_bq():
    try:
        today = datetime(date.today().year, date.today().month, date.today().day).strftime('%d/%m/%Y')
        dtObj = datetime.strptime(today, '%d/%m/%Y')
        index_col = [(dtObj - relativedelta(months=i)).date() for i in range(1,30,1)]
        df = pd.DataFrame(columns=['רכישות מט\"ח במליוני דולרים', 'שינוי ביתרות מט\"ח במיליוני דולרים'], index=index_col)
        df = df.fillna("").sort_index()
        df.index = pd.to_datetime(df.index).strftime('%m/%Y')
        return df
    except Exception as e:
        print('problem getting col: bp-bq' + str(e))