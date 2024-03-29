
# Bar's get_daily_data

from get_data_from_sites.get_tase_data import *
from get_data_from_sites.get_investing_data import *
from get_data_from_sites.get_boi_data import *
from get_data_from_sites.get_trasury_data import *
from get_data_from_sites.get_eia_data import *

from pandas import ExcelWriter


def save_xls(dict_df, path):
    writer = ExcelWriter(path)
    for key in dict_df:
        try:
            dict_df[key].to_excel(writer, key)
        except:
            print('had a problem sending sheet to excel. sheet name: ' + key)

    writer.save()


def get_cdata_daily(record_num):
    try:
        print('getting cdata')
        index_names = ['tel bond 20', 'tel bond 40', 'gov bond', 'tel aviv banks', 'tel bond 60']

        cdata_daily_df = pd.DataFrame()
        for index in index_names:
            index_data = get_tase_data(index).iloc[-record_num:]
            index_df = pd.DataFrame({index: index_data})

            cdata_daily_df = pd.concat([cdata_daily_df, index_df], axis=1)

        return cdata_daily_df
    except Exception as e:
        print('problem getting cdata:' + str(e))
        return None


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


        daily_il_df["מנורמל לאפריל 2011 ת'א 100"] = (daily_il_df['Tel 125']/1215.49)*100
        return {'daily_il': daily_il_df, 'daily_us': daily_us_df, 'daily_uk': daily_uk_df}
    except Exception as e:
        print('Problem getting htdata: ' + str(e))
        return  None


def get_xdata_daily(record_num):
    try:
        print('getting xdata')
        return get_boi_data(record_num, file_name='xdata')
    except Exception as e:
        print('Problem getting xdata: ' + str(e))
        return None


def get_pdata_daily(record_num):
    try:
        print('getting pdata')
        index_names = ['foodstuffs', 'industrials', 'textiles', 'metals']
        urls = ['https://www.eia.gov/dnav/pet/hist/rbrteD.htm', 'https://www.eia.gov/dnav/pet/hist/rwtcD.htm']
        table_names = ['Europe Brent Spot Price FOB  (Dollars per Barrel)', 'Cushing, OK WTI Spot Price FOB  (Dollars per Barrel)']

        result_df = pd.DataFrame()
        eia_data = get_eia_data(urls=urls, table_names=table_names, record_num=7)
        result_df = pd.concat([result_df, eia_data], axis=1)

        return result_df
    except Exception as e:
        print('Problem getting pdata:' + str(e))
        return None

def get_mdata_daily(record_num):
    try:
        print('getting mdata')
        return get_treasury_data(record_num)
    except Exception as e:
        print('problem getting mdata: ' + str(e))
        return None

def get_daily_data(record_num):
    # Create a Pandas Excel writer using XlsxWriter as the engine.
    htdata_dict = get_htdata_daily(record_num)
    func_dict = {'cdata': get_cdata_daily(record_num), 'daily_il': htdata_dict.get('daily_il'), 'daily_us': htdata_dict.get('daily_us'),
                 'daily_uk': htdata_dict.get('daily_uk'), 'mdata': get_mdata_daily(record_num), 'xdata': get_xdata_daily(record_num),
                 'pdata': get_pdata_daily(10)}
    return func_dict



def cols_t_to_v():
    try:
        url = 'https://www.boi.org.il/Lists/BoiChapterTablesFiles/n110.xls'
        resp = requests.get(url)
        df = pd.read_excel(resp.content, index_col=-14)
        df = df.iloc[:, -16:-13]

        ### Get column index ###
        temp = df.loc['תאריך':]
        temp = temp.loc[pd.isna(temp.index)]

        col_index = []
        for i in range(3):
            col = temp.iloc[:, i]
            col_index.append(col.fillna(' ').str.cat(sep=' '))
        # #########################

        df.columns = col_index
        df = df[df.index.notnull()]
        df = df.loc['Date':].iloc[1:31, :]
        df = df.dropna(how='all')
        df = df.sort_index()
        df.index = pd.to_datetime(df.index).strftime('%m/%Y')
        df = df[df.columns[::-1]]
        return df
    except Exception as e:
        print('problem getting cols: T-V: ' + str(e))

#####################


import camelot

file = "https://www.gov.il/BlobFolder/dynamiccollectorresultitem/weekly_prices_report_10_march_2022/he/weekly_prices_weekly%20prices%20report_10_mar_2022.pdf"
tables = camelot.read_pdf(file)
print(tables[0].df)


