from pandas import ExcelWriter

from get_monthy_data.get_pdata_monthly import *
from get_monthy_data.get_cdata_monthly import *
from get_monthy_data.get_ft_data_monthly import *
from get_monthy_data.get_edata_monthly import *
from get_monthy_data.get_xdata_monthly import *
from get_monthy_data.get_ldata_nomthly import *
from get_monthy_data.get_rdata_monthly import *

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
    function_dict = {'D-H': cols_d_to_h(), 'I-K': cols_i_to_k_cdata(), 'L': col_l(), 'T-V': cols_t_to_v(), 'W-X': cols_w_to_x(), 'Y': col_y(), 'Z-AA': cols_z_to_aa(), 'AB-AH': cols_ab_to_ah(), 'AK': col_ak(), 'BE-BG': cols_be_to_bg()}

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
    function_dict = {'Z': col_z_edata(), 'AA': col_aa(), 'AB': col_ab(), 'AC': col_ac(), 'BJ': col_bj(), 'bp-bq': col_bp_to_bq()}

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
    function_dict = {'C-J': cols_c_to_j_ldata(), 'K-R': cols_k_to_r_ldata(), 'S': cols_s_ldata(),
                     'X-BA': cols_x_to_ba_ldata(), 'BF': col_bf_ldata(),
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


def get_rdata_monthly(record_num):
    print('Getting R_Data')
    function_dict = {'C-D': cols_c_to_d_rdata(), 'E-R': cols_e_to_r_rdata(),
                     'S': col_s_rdata(),
                     'T-U': cols_t_to_u_rdata(), 'V-CF': cols_v_to_cf_rdata(),
                     'CG-CH': cols_cg_to_ch_rdata(), 'CI-CL': cols_ci_to_cl_rdata(),
                     'CM': cols_cm_rdata(), 'CN-CY': cols_cn_to_cy_rdata(),
                     'CZ-DB': cols_cz_to_db_rdata()}

    df = pd.DataFrame()

    for cols in function_dict.keys():
        try:
            cols_df = function_dict.get(cols)
            df = pd.concat([df, cols_df], axis=1)
        except Exception as e:
            print('There was a problem concatenating columns:' + cols + ' for rdata.')
            print('The error: ' + str(e))

    df.index = pd.to_datetime(df.index, format="%m/%Y")
    df = df.sort_index()
    df.index = pd.to_datetime(df.index).strftime('%m/%Y')
    return df.iloc[-record_num:]


def get_pdata_monthly(record_num):
    print('Getting P_Data')
    function_dict = {'G-T': cols_g_to_t_pdata(),
                     'AA': col_aa_pdata(),
                     'AB': col_ab_pdata(),
                     'AC': cols_ac_pdata(),
                     'AP': col_ap_pdata(),
                     'AW': col_aw_pdata()}

    df = pd.DataFrame()

    for cols in function_dict.keys():
        try:
            cols_df = function_dict.get(cols)
            df = pd.concat([df, cols_df], axis=1)
        except Exception as e:
            print('There was a problem concatenating columns:' + cols + ' for pdata.')
            print('The error: ' + str(e))

    df.index = pd.to_datetime(df.index, format="%m/%Y")
    df = df.sort_index()
    df.index = pd.to_datetime(df.index).strftime('%m/%Y')
    return df.iloc[-record_num:]


def get_ftdata_monthly(record_num):
    print('Getting FT_Data')
    function_dict = {'C-BI': cols_c_to_bi_rdata(),
                     'CB': col_cb_ftdata(),
                     'DG': col_dg_ftdata(),
                     'DH-EV': cols_dh_to_ev_ftdata()}

    df = pd.DataFrame()

    for cols in function_dict.keys():
        try:
            cols_df = function_dict.get(cols)
            df = pd.concat([df, cols_df], axis=1)
        except Exception as e:
            print('There was a problem concatenating columns:' + cols + ' for ftdata.')
            print('The error: ' + str(e))

    df.index = pd.to_datetime(df.index, format="%m/%Y")
    df = df.sort_index()
    df.index = pd.to_datetime(df.index).strftime('%m/%Y')
    return df.iloc[-record_num:]


def get_monthly_data(record_num):
    func_dict = {'cdata': get_cdata_monthly(record_num), 'ftdata': get_ftdata_monthly(record_num),
                 'edata': get_edata_monthly(record_num), 'xdata': get_xdata_monthly(record_num),
                 'ldata': get_ldata_monthly(record_num), 'pdata': get_pdata_monthly(record_num),
                 'rdata': get_rdata_monthly(record_num)}

    return func_dict
