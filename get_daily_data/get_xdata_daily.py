from get_data_from_sites.get_boi_data import *


def get_xdata_daily(record_num):
    try:
        print('getting xdata')
        return get_boi_data(record_num, file_name='xdata')
    except Exception as e:
        print('Problem getting xdata: ' + str(e))
        return None