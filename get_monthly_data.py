from pandas import ExcelWriter

from get_monthy_data.get_cdata_monthly import *
from get_monthy_data.get_ft_data_monthly import *
from get_monthy_data.get_edata_monthly import *
from get_monthy_data.get_xdata_monthly import *
from get_monthy_data.get_ldata_nomthly import *

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


def get_cdata_monthly(record_num):
    print('Getting C_Data')
    function_dict = {'D-H': cols_d_to_h(), 'I-K': cols_i_to_k(), 'L': col_l(), 'T-V': cols_t_to_v(), 'W-X': cols_w_to_x(), 'Y': col_y(), 'Z-AA': cols_z_to_aa(), 'AB-AH': cols_ab_to_ah(), 'AK': col_ak(), 'BE-BG': cols_be_to_bg()}

    df = pd.DataFrame()

    for cols in function_dict.keys():
        try:
            cols_df = function_dict.get(cols)
            df = pd.concat([df, cols_df], axis=1)
        except Exception as e:
            print('There was a problem concatenating columns:' + cols + ' for cdata.')
            print('The error: ' + str(e))

    df.index = pd.to_datetime(df.index, format="%m/%Y")
    df = df.sort_index()
    df.index = pd.to_datetime(df.index).strftime('%m/%Y')
    return df.iloc[-record_num:]


def get_edata_monthly(record_num):
    print('Getting E_Data')
    function_dict = {'Z': col_z(), 'AA': col_aa(), 'AB': col_ab(), 'AC': col_ac(), 'BJ': col_bj(), 'bp-bq': col_bp_to_bq()}

    df = pd.DataFrame()

    for cols in function_dict.keys():
        try:
            cols_df = function_dict.get(cols)
            df = pd.concat([df, cols_df], axis=1)
        except Exception as e:
            print('There was a problem concatenating columns:' + cols + ' for edata.')
            print('The error: ' + str(e))

    df.index = pd.to_datetime(df.index, format="%m/%Y")
    df = df.sort_index()
    df.index = pd.to_datetime(df.index).strftime('%m/%Y')
    return df.iloc[-record_num:]


def get_xdata_monthly(record_num):
    print('Getting X_Data')
    function_dict = {'D-H': cols_d_to_h_xdata(), 'I-K': col_i_to_k_xdata(), 'L-N': col_l_to_n(), 'P': col_p()}

    df = pd.DataFrame()

    for cols in function_dict.keys():
        try:
            cols_df = function_dict.get(cols)
            df = pd.concat([df, cols_df], axis=1)
        except Exception as e:
            print('There was a problem concatenating columns:' + cols + ' for xdata.')
            print('The error: ' + str(e))

    df.index = pd.to_datetime(df.index, format="%m/%Y")
    df = df.sort_index()
    df.index = pd.to_datetime(df.index).strftime('%m/%Y')
    return df.iloc[-record_num:]


def get_ldata_monthly(record_num):
    print('Getting L_Data')
    function_dict = {'C-J': cols_c_to_j_ldata(), 'K-R': cols_k_to_r_ldata(), 'X-BA': cols_x_to_ba_ldata(),
                     'BF': col_bf_ldata(),
                     'BG': col_bg_ldata(), 'BH-BY': col_bh_to_by_ldata(),
                     'BZ': cols_bz_ldata(), 'CA': cols_ca_ldata(), 'CB-CG': cols_cb_to_cg_ldata(),
                     'CH-CU': cols_ch_to_cu_ldata(), 'CV-CX': col_cv_to_cx_ldata()}

    df = pd.DataFrame()

    for cols in function_dict.keys():
        try:
            cols_df = function_dict.get(cols)
            df = pd.concat([df, cols_df], axis=1)
        except Exception as e:
            print('There was a problem concatenating columns:' + cols + ' for ldata.')
            print('The error: ' + str(e))

    df.index = pd.to_datetime(df.index, format="%m/%Y")
    df = df.sort_index()
    df.index = pd.to_datetime(df.index).strftime('%m/%Y')
    return df.iloc[-record_num:]


def get_monthly_data(record_num):
    func_dict = {'cdata': get_cdata_monthly(record_num), 'ftdata': get_ft_data_monthly(record_num),
                 'edata': get_edata_monthly(record_num), 'xdata': get_xdata_monthly(record_num),
                 'ldata': get_ldata_monthly(record_num)}

    return func_dict
