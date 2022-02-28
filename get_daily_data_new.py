from pandas import ExcelWriter

from get_daily_data.get_daily_uk_daily import *
from get_daily_data.get_daily_us_daily import *
from get_daily_data.get_dailyil_daily import *
from get_daily_data.get_cdata_daily import *
from get_daily_data.get_pdata_daily import *

from get_data_from_sites.get_trasury_data import *
from get_data_from_sites.get_boi_data import *



pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)


def save_xls(dict_df, path):
    writer = ExcelWriter(path)
    for key in dict_df:
        try:
            dict_df[key].to_excel(writer, key)
        except:
            print('had a problem sending sheet to excel. sheet name: ' + key)

    writer.save()


def get_cdata_daily(record_num):
    print('Getting C_Data')
    function_dict = {'D-Y': cols_d_to_y_cdata_daily(), 'Z-AA': cols_z_to_aa_cdata_daily(),
                     'AB-AH': cols_ab_to_ah_cdata_daily(), 'AI': cols_ai_cdata_daily(),
                     'AJ-AK': cols_aj_to_ak_cdata_daily(), 'AL-AM': cols_al_to_am_cdata_daily()}

    df = pd.DataFrame()

    for cols in function_dict.keys():
        try:
            cols_df = function_dict.get(cols)
            df = pd.concat([df, cols_df], axis=1)
        except Exception as e:
            print('There was a problem concatenating columns:' + cols + ' for cdata.')
            print('The error: ' + str(e))

    df.index = pd.to_datetime(df.index, format='%d/%m/%Y')
    df = df.sort_index()
    df.index = pd.to_datetime(df.index).strftime('%d/%m/%Y')
    return df.iloc[-record_num:]


def get_xdata_daily(record_num):
    try:
        print('getting xdata')
        return get_boi_data(record_num, file_name='xdata')
    except Exception as e:
        print('Problem getting xdata: ' + str(e))
        return None


def get_pdata_daily(record_num):
    print('Getting P_Data')
    function_dict = {'D-E': cols_d_to_e_pdata_daily(record_num),
                     'F-V': cols_f_to_v_pdata_daily()}

    df = pd.DataFrame()

    for cols in function_dict.keys():
        try:
            cols_df = function_dict.get(cols)
            df = pd.concat([df, cols_df], axis=1)
        except Exception as e:
            print('There was a problem concatenating columns:' + cols + ' for pdata.')
            print('The error: ' + str(e))

    df.index = pd.to_datetime(df.index, format='%d/%m/%Y')
    df = df.sort_index()
    df.index = pd.to_datetime(df.index).strftime('%d/%m/%Y')
    return df.iloc[-record_num:]


def get_mdata_daily(record_num):
    try:
        print('getting mdata')
        return get_treasury_data(record_num)
    except Exception as e:
        print('problem getting mdata: ' + str(e))
        return None


def get_dailyil_daily(record_num):
    print('Getting Dailyil_Data')
    function_dict = {'D-I': cols_d_to_i_dailyil_daily(record_num)}

    df = pd.DataFrame()

    for cols in function_dict.keys():
        try:
            cols_df = function_dict.get(cols)
            df = pd.concat([df, cols_df], axis=1)
        except Exception as e:
            print('There was a problem concatenating columns:' + cols + ' for DAILY_IL data.')
            print('The error: ' + str(e))

    df.index = pd.to_datetime(df.index, format='%d/%m/%Y')
    df = df.sort_index()
    df.index = pd.to_datetime(df.index).strftime('%d/%m/%Y')
    return df.iloc[-record_num:]


def get_daily_us_daily(record_num):
    print('Getting Daily_us_Data')
    function_dict = {'D-E': cols_d_to_e_daily_us_daily(),
                     'F-X': cols_f_to_x_daily_us_daily(record_num)}

    df = pd.DataFrame()

    for cols in function_dict.keys():
        try:
            cols_df = function_dict.get(cols)
            df = pd.concat([df, cols_df], axis=1)
        except Exception as e:
            print('There was a problem concatenating columns:' + cols + ' for DAILY_US data.')
            print('The error: ' + str(e))

    df.index = pd.to_datetime(df.index, format='%d/%m/%Y')
    df = df.sort_index()
    df.index = pd.to_datetime(df.index).strftime('%d/%m/%Y')
    return df.iloc[-record_num:]


def get_daily_uk_daily(record_num):
    print('Getting Daily_uk_Data')
    function_dict = {'D-S': cols_d_to_s_daily_us_daily(),
                     'T': get_col_t_daily_uk_daily(record_num)}

    df = pd.DataFrame()

    for cols in function_dict.keys():
        try:
            cols_df = function_dict.get(cols)
            df = pd.concat([df, cols_df], axis=1)
        except Exception as e:
            print('There was a problem concatenating columns:' + cols + ' for DAILY_UK data.')
            print('The error: ' + str(e))

    df.index = pd.to_datetime(df.index, format='%d/%m/%Y')
    df = df.sort_index()
    df.index = pd.to_datetime(df.index).strftime('%d/%m/%Y')
    return df.iloc[-record_num:]


def get_daily_data(record_num):
    # Create a Pandas Excel writer using XlsxWriter as the engine.
    func_dict = {'cdata': get_cdata_daily(record_num),
                 'daily_il': get_dailyil_daily(record_num),
                 'daily_us': get_daily_us_daily(record_num),
                 'daily_uk': get_daily_uk_daily(record_num),
                 'mdata': get_mdata_daily(record_num),
                 'xdata': get_xdata_daily(record_num),
                 'pdata': get_pdata_daily(record_num)}
    return func_dict

