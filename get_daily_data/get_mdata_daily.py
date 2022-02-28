from get_data_from_sites.get_trasury_data import *


def get_mdata_daily(record_num):
    try:
        print('getting mdata')
        return get_treasury_data(record_num)
    except Exception as e:
        print('problem getting mdata: ' + str(e))
        return None