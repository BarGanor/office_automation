import requests
import pandas as pd
from datetime import datetime, date, timedelta
from bs4 import BeautifulSoup
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)


def cols_d_to_h():
    try:
        try:
            result_df = pd.DataFrame()
            for i in range(2, -1, -1):
                year = str(datetime.today().year - i)
                url = "https://info.tase.co.il/Heb/Statistics/StatRes/" + year + "/Stat_202_l02_" + year + ".xlsx"
                resp = requests.get(url)
                df = pd.read_excel(resp.content, index_col=0, header=3)
                df = df.loc[: 'הערות לטבלה:'].iloc[:-2]
                index_lst = [x for x in df.index if not type(x) is int]
                index_lst = [x for x in index_lst if len(str(x)) >7]
                index_lst = [x for x in index_lst if not x.isnumeric()]
                year_df = df.iloc[-len(index_lst):]
                year_df.index = [str(x) + '/' + year for x in range(1, len(index_lst) +1)]
                year_df = year_df[['מניות והמירים(1) סה"כ', 'אג"ח ממשלתי סה"כ הנפקות(2)', 'אג"ח ממשלתי פדיונות(3)', 'אג"ח ממשלתי גיוס נטו', 'אג"ח חברות סה"כ']]
                year_df.index = ['0' + x if x.find('/') == 1 else x for x in year_df.index]
                result_df = result_df.append(year_df)
            return result_df

        except: ### If there is no data for current year
            result_df = pd.DataFrame()
            for i in range(2, 0, -1):
                year = str(datetime.today().year - i)
                url = "https://info.tase.co.il/Heb/Statistics/StatRes/" + year + "/Stat_202_l02_" + year + ".xlsx"
                resp = requests.get(url)
                df = pd.read_excel(resp.content, index_col=0, header=3)
                df = df.loc[: 'הערות לטבלה:'].iloc[:-2]
                index_lst = [x for x in df.index if not type(x) is int]
                index_lst = [x for x in index_lst if len(str(x)) >7]
                index_lst = [x for x in index_lst if not x.isnumeric()]
                year_df = df.iloc[-len(index_lst):]
                year_df.index = [str(x) + '/' + year for x in range(1, len(index_lst) +1)]
                year_df = year_df[['מניות והמירים(1) סה"כ', 'אג"ח ממשלתי סה"כ הנפקות(2)', 'אג"ח ממשלתי פדיונות(3)', 'אג"ח ממשלתי גיוס נטו', 'אג"ח חברות סה"כ']]
                year_df.index = ['0' + x if x.find('/') == 1 else x for x in year_df.index]
                result_df = result_df.append(year_df)
            return result_df
    except Exception as e:
        print('problem getting cols: D-H' + str(e))


def cols_i_to_k_cdata():
    try:
        try:
            current_month = datetime.today().month
            current_year = datetime.today().year

            for month in range(current_month, 0, -1):
                if month < 10:
                    month = '0' + str(month)
                else:
                    month = str(month)

                url = f"https://www.cbs.gov.il/he/publications/doclib/{current_year}/yarhon{month}{str(current_year % 100)}/i2.xls"
                resp = requests.get(url)
                try:
                    df = pd.read_excel(resp.content, index_col=0)
                    df = df.dropna(how='all')
                    df.columns = df.iloc[7].fillna('').str.cat(' ' + df.iloc[8].fillna(''))
                    break
                except Exception as e:
                    print('cols i-k: No Data For Month - ' + str(month))

            df.index = df.index.fillna('').astype('string')
            if df is not None:
                df = df.loc[str(current_year - 1):]
                df = df[['Total ']]
                df.columns = ['בנקים מסחריים ישראלים במטבע חוץ', 'בנקים מסחריים- מטבע ישראלי']
                col_i = df['בנקים מסחריים- מטבע ישראלי']
                col_j = df['בנקים מסחריים ישראלים במטבע חוץ']
                col_k = col_i + col_j
                col_k.name = 'סך הכל אשראי ציבור'

                result_df = pd.concat([col_i, col_j, col_k], axis=1).dropna(how='all')

                temp = []
                current_month = 1
                for i in result_df.index:
                    if (i.isnumeric()):
                        curr_year = int(i)
                        current_month = 1
                        temp.append(datetime(curr_year, current_month, 1).strftime('%m/%Y'))
                        current_month += 1
                    else:
                        temp.append(datetime(curr_year, current_month, 1).strftime('%m/%Y'))
                        current_month += 1
                result_df.index = temp
            return result_df.astype('int64')

        except:
            current_month = datetime.today().month
            current_year = datetime.today().year

            for month in range(current_month, 0, -1):
                if month < 10:
                    month = '0' + str(month)
                else:
                    month = str(month)

                url = f"https://www.cbs.gov.il/he/publications/doclib/{current_year - 1}/yarhon12{str((current_year - 1) % 100)}/i2.xls"
                resp = requests.get(url)
                try:
                    df = pd.read_excel(resp.content, index_col=0)
                    df = df.dropna(how='all')
                    df.columns = df.iloc[7].fillna('').str.cat(' ' + df.iloc[8].fillna(''))
                    break
                except Exception as e:
                    print('cols i-k: No Data For Month - ' + str(month))

            df.index = df.index.fillna('').astype('string')
            if df is not None:
                df = df.loc[str(current_year - 1):]
                df = df[['Total ']]
                df.columns = ['בנקים מסחריים ישראלים במטבע חוץ', 'בנקים מסחריים- מטבע ישראלי']
                col_i = df['בנקים מסחריים- מטבע ישראלי']
                col_j = df['בנקים מסחריים ישראלים במטבע חוץ']
                col_k = col_i + col_j
                col_k.name = 'סך הכל אשראי ציבור'

                result_df = pd.concat([col_i, col_j, col_k], axis=1).dropna(how='all')

                temp = []
                current_month = 1
                for i in result_df.index:
                    if (i.isnumeric()):
                        curr_year = int(i)
                        current_month = 1
                        temp.append(datetime(curr_year, current_month, 1).strftime('%m/%Y'))
                        current_month += 1
                    else:
                        temp.append(datetime(curr_year, current_month, 1).strftime('%m/%Y'))
                        current_month += 1
                result_df.index = temp
            return result_df.astype('int64')
    except Exception as e:
        print('problem getting cols: I-K: ' + str(e))


def col_l():
    try:
        url = 'https://www.boi.org.il/Lists/BoiChapterTablesFiles/d010.xls'
        resp = requests.get(url)
        df = pd.read_excel(resp.content, index_col=-1)
        df = df.loc['נתוני סוף תקופה (במיליוני ש"ח)':].iloc[:, -1].dropna()

        df.index = pd.to_datetime(df.index)
        df = df.sort_index()
        df.index = df.index.strftime('%m/%Y')
        df.name = 'סך הכל אשראי לציבור'

        return df
    except Exception as e:
        print('problem getting cols: L: ' +str(e))


def cols_t_to_v():
    try:
        url = 'https://www.boi.org.il/Lists/BoiChapterTablesFiles/n110.xls'
        resp = requests.get(url)
        df = pd.read_excel(resp.content, index_col=-1)
        df = df.iloc[:, -3:]
        df = df.dropna().iloc[3:50, :]
        df = df.sort_index()
        df.index = pd.to_datetime(df.index).strftime('%m/%Y')

        df = df[df.columns[::-1]]
        df.columns = ['סכום האשראי בריבית קבועה Amount of credit at fixed interest',
                      'סכום האשראי בריבית משתנה Amount of credit at variable interest',
                      'Cpi - indexed segment סה"כ Total']
        return df

    except Exception as e:
        print('problem getting cols: T-V: ' + str(e))


def cols_w_to_x():
    try:
        url = 'https://www.boi.org.il/he/BankingSupervision/Data/Documents/pribmash.xls'
        resp = requests.get(url)
        df = pd.read_excel(resp.content, sheet_name='RESULT').dropna(axis=1, how='all')
        df.columns = df.iloc[0]
        df.index = df.iloc[:, -1]
        df = df.loc['month of return':].iloc[1:, :]
        result_df = df[['ממוצע', 'מעל 25 ']]
        result_df = result_df.sort_index()
        result_df.index = pd.to_datetime(result_df.index).strftime('%m/%Y')
        return result_df.astype('string') + '%'
    except Exception as e:
        print('problem getting cols: W-X: '+ str(e))


def col_y():
    try:
        url = 'https://www.boi.org.il/he/DataAndStatistics/Lists/BoiTablesAndGraphs/tnc01_h.xls'
        resp = requests.get(url)
        df = pd.read_excel(resp.content, sheet_name='נתונים שוטפים', index_col=1)
        df.columns = df.loc['התקופה']
        df = df.loc['התקופה':].iloc[7:, :]
        df = df.dropna(axis=0, how='all')
        df = df.dropna(axis=1, how='all')
        df.index = pd.to_datetime(df.index).strftime('%m/%Y')
        result_df = df['סה"כ7']
        result_df.name = 'שווי תיק הנכסים של הציבור, מיליארד ₪ מחירים שוטפים'
        return result_df
    except Exception as e:
        print('problem getting cols: Y: ' + str(e))


def cols_z_to_aa():
    try:
        import dateutil.relativedelta
        index_lst = []
        today = date.today().replace(day=1)

        df_dict = {'תל בונד 20 (מחושב)':[], 'תל בונד 40 (מחושב)':[]}

        for i in range(24):
            month = today - dateutil.relativedelta.relativedelta(months=i)
            index_lst.append(month.strftime('%m/%Y'))

            df_dict.get('תל בונד 20 (מחושב)').append('')
            df_dict.get('תל בונד 40 (מחושב)').append('')

        df = pd.DataFrame.from_dict(df_dict)
        df.index = pd.to_datetime(index_lst)
        df = df.sort_index()
        df.index = df.index.strftime('%m/%Y')

        return df
    except Exception as e:
        print('problem getting cols: Z-AA: ' + str(e))


def cols_ab_to_ah():
    try:
        url = 'https://www.boi.org.il/he/DataAndStatistics/Lists/BoiTablesAndGraphs/shce14_h.xls'
        resp = requests.get(url)
        df = pd.read_excel(resp.content, index_col=0)

        df = df.dropna(axis=0, how='all')
        df.columns = df.iloc[0].fillna('').str.cat(' ' + df.iloc[1].fillna(''))
        df = df.dropna(axis=1, how='all')
        df = df.dropna(axis=0, how='all')
        df = df.loc['התקופה':].iloc[2:]

        total = df[' סך כל הנכסים ']
        total.name = 'סה"כ נכסים'

        gov_bond = df.loc[:, 'אג"ח פרטיות3 סחירות':].iloc[:, :2]
        gov_bond.columns = ['אג"ח פרטי סחיר', 'אג"ח פרטי לא סחיר']

        stock = df.loc[:, 'מניות סחירות':].iloc[:, :2]
        stock.columns = ['מניות סחיר', 'מניות לא-סחיר']

        out_of_bond = ((gov_bond.iloc[:, 0] + gov_bond.iloc[:, 1]) / 100) * total
        out_of_bond.name = 'מזה: אגח פרטי'
        out_of_stock = ((stock.iloc[:, 0] + stock.iloc[:, 1]) / 100) * total
        out_of_stock.name = 'מזה: מניות'

        df = pd.concat([total, gov_bond, stock, out_of_bond, out_of_stock], axis=1)
        df.index = pd.to_datetime(df.index).strftime('%m/%Y')

        return df
    except Exception as e:
        print('problem getting cols: AB-AH: ' + str(e))


def col_ak():
    try:
        try:
            result_df = pd.DataFrame()
            for i in range(2, -1, -1):
                year = str(datetime.today().year - i)
                url = 'https://www.boi.org.il/he/BankingSupervision/Data/_layouts/boi/handlers/WebPartHandler.aspx?wp=ItemsAggregator&PageId=150&CqfDateFrom=01%2F01%2F' + year + '&CqfDateTo=31%2F12%2F' + year + '&_=1633337318236'
                resp = requests.get(url)
                soup = BeautifulSoup(resp.content.decode('utf-8'), features='lxml')
                tab = soup.find("table", {"class": "s4-wpTopTable"})
                year_df = pd.read_html(tab.prettify())[1]
                year_df = year_df.drop_duplicates()
                result_df = result_df.append(year_df, ignore_index=True)

            result_df = result_df.set_index('תאריך')
            return result_df
        except: ### If there is no data for current year
            result_df = pd.DataFrame()
            for i in range(2, 0, -1):
                year = str(datetime.today().year - i)
                url = 'https://www.boi.org.il/he/BankingSupervision/Data/_layouts/boi/handlers/WebPartHandler.aspx?wp=ItemsAggregator&PageId=150&CqfDateFrom=01%2F01%2F' + year + '&CqfDateTo=31%2F12%2F' + year + '&_=1633337318236'
                resp = requests.get(url)
                soup = BeautifulSoup(resp.content.decode('utf-8'), features='lxml')
                tab = soup.find("table", {"class": "s4-wpTopTable"})
                year_df = pd.read_html(tab.prettify())[1]
                year_df = year_df.drop_duplicates()
                result_df = result_df.append(year_df, ignore_index=True)

            result_df = result_df.set_index('תאריך')
            return result_df


    except Exception as e:
        print('problem getting cols: AK: ' + str(e))


def cols_be_to_bg():
    try:
        url = 'https://www.boi.org.il/he/DataAndStatistics/Lists/BoiTablesAndGraphs/itrashrh.xlsx'
        resp = requests.get(url)
        df = pd.read_excel(resp.content, sheet_name='ארוך טווח אשראי חודשי - אומדנים', header=7, index_col=0)

        df = df.iloc[:, -36:].transpose()
        df.index = [x.replace('-', '/20') for x in df.index]
        df.index = ['0' + x if x.find('/') == 1 else x for x in df.index]

        total_credit_to_business = df.loc[:, 'סך האשראי במשק':].iloc[:, 1]
        total_credit_to_household = df.loc[:, 'סך האשראי במשק':].iloc[:, 6]
        total_credit_for_residency = df.loc[:, 'סך האשראי מהבנקים':].iloc[:, 2]

        result_df = pd.concat([total_credit_to_business, total_credit_to_household, total_credit_for_residency], axis=1)

        return result_df
    except Exception as e:
        print('problem getting cols: BE-BG: ' + str(e))

